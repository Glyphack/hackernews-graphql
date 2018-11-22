from django.contrib.auth import get_user_model

from graphene_django import DjangoObjectType
import graphene


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class CreateUser:
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String()
        password = graphene.String()
        email = graphene.String()

    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username = username,
            email = email
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


class Query(graphene.AbstractType):
    users = graphene.List()
    me = graphene.Field()

    def resolve_users(self, info):
        return get_user_model().objects.all()

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in')

        return user
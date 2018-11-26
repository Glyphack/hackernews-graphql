from django.contrib.auth import get_user_model

from django.db import models


class Link(models.Model):
    posted_by = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    url = models.URLField()
    description = models.TextField(blank=True)


class Vote(models.Model):
    url = models.ForeignKey(Link, related_name='vote', on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


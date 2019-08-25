CREATE_LINK_MUTATION = """
mutation CreateLink($url: String!, $desc: String!){
  createLink(description: $desc, url: $url){
    id,
    url,
    description
  }
}
"""
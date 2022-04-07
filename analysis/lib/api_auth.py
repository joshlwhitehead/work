from pathlib import Path
from python_graphql_client import GraphqlClient
import graphql_queries as qry

endpoint = 'https://dev-graph.idmo.dev/v1/graphql'
unauthApi = GraphqlClient(endpoint=endpoint)

# Get your refresh token at https://youtest.idmo.dev and click on account.
f = open(Path(__file__).parent / 'refresh.token')
refreshToken = f.read()


def getIdTokenHeaders(refreshToken):
  variables = {
    'refreshToken': refreshToken
  }

  response = unauthApi.execute(query=qry.idTokenQuery, variables=variables)
  id = response['data']['token_from_refresh']['idToken']
  return {
    'Authorization': f'Bearer {id}'
  }

def getApiClient():
  return GraphqlClient(endpoint=endpoint, headers=getIdTokenHeaders(refreshToken))




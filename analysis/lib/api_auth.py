from pathlib import Path
from python_graphql_client import GraphqlClient
import graphql_queries as qry

endpoint = 'https://api.co-dx.io/v1/graphql'
unauthApi = GraphqlClient(endpoint=endpoint)

# Get your refresh token at https://youtest.idmo.dev and click on account.
# f = open(Path(__file__).parent / 'refresh.token')
# print(Path(__file__).parent)
# refreshToken = f.read()
refreshToken = 'AOEOulbhRL-qqXYQuPfN7PiH7ZWvew-5z34HRX8KG4ADdYRJjjEw78qmTMhmDe7PEGCmp3Tf5Z2aYbyEzBG2eQx3RqswihxlqJXpKLN70Ip01jJ_iRdynkJahORDd6glHfzwosCKD6F3P9_QKSl9KBTgvEZwRxmAvd8Xeu6OCRw0zRlzhP38t-LH8_KKZULrAEr8Hwq63jnDWd4_Mh2iQOJvulTOwXLwYAtmhS4u8-jNC2URzXgRNMANE8QlgUnruIZPOEOdXQBgvTNqZJeLi_nhJvhXLRURappolfEEO5u_iFet-5ZNeobrGWifp_wMHPjYJmquW8TC'


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




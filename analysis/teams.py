import msal, atexit, urllib 
import os
from requests import get, put

date = '20210907'

########    FOR TEAMS ACCESS    ###########
folder_path = ''.join(['General/Experiments-MolBio/Maverick_',date])

TENANT_ID = '61c2eea7-516f-42d8-8438-f39479fd5d0c'
CLIENT_ID = 'b98adc8f-e366-49cf-aa48-fbead29fd0fb'
SHAREPOINT_HOST_NAME = 'idahomolecularinc.sharepoint.com'
SITE_NAME = 'MaverikProject'

AUTHORITY = ''.join(['https://login.microsoftonline.com/',TENANT_ID])
ENDPOINT = 'https://graph.microsoft.com/v1.0'

SCOPES = [
    'Files.ReadWrite.All',
    'Sites.ReadWrite.All',
    'User.Read',
    'User.ReadBasic.All'
]
#############   FUNCTIONS FOR TEAMS     ########################
cache = msal.SerializableTokenCache()
if os.path.exists('token_cache.bin'):
    cache.deserialize(open('token_cache.bin', 'r').read())

atexit.register(lambda: open('token_cache.bin', 'w').write(cache.serialize()) if cache.has_state_changed else None)

app = msal.PublicClientApplication(CLIENT_ID, authority=AUTHORITY, token_cache=cache)

accounts = app.get_accounts()
result = None

if len(accounts) > 0:
    result = app.acquire_token_silent(SCOPES, account=accounts[0])
# print(result)
if result is None:
    flow = app.initiate_device_flow(scopes=SCOPES)
    if 'user_code' not in flow:
        raise Exception('Failed to create device flow')
        
    print(flow['message'])
    result = app.acquire_token_by_device_flow(flow)
    # print('x')


if 'access_token' in result:
    access_token = result['access_token']
    headers={'Authorization':''.join(['Bearer ',access_token])}
    
    
    ### site info ###
    result = get(f'{ENDPOINT}/sites/{SHAREPOINT_HOST_NAME}:/sites/{SITE_NAME}', headers=headers)
    result.raise_for_status()
    site_info = result.json()
    site_id = site_info['id']
    
    
    ### drive info ###
    result = get(f'{ENDPOINT}/sites/{site_id}/drive', headers=headers)
    result.raise_for_status()
    drive_info = result.json()
    drive_id = drive_info['id']
    
    ### folder info ###
    # replace this with the folder you want to list
    folder_url = urllib.parse.quote(folder_path)
    result = get(f'{ENDPOINT}/drives/{drive_id}/root:/{folder_url}', headers=headers)
    result.raise_for_status()
    folder_info = result.json()
    folder_id = folder_info['id']
    
    
    ### folder contents ###
    result = get(f'{ENDPOINT}/drives/{drive_id}/items/{folder_id}/children', headers=headers)
    result.raise_for_status()
    children = result.json()['value']
    # for item in children:
    #    print(item['name'])
        



    ### download file ###
    ### file info ###
    def download(file):           
        file_path = ''.join([folder_path,'/',file,'.csv'])
        file_url = urllib.parse.quote(file_path)
        result = get(f'{ENDPOINT}/drives/{drive_id}/root:/{file_url}', headers=headers)
        file_info = result.json()
        file_id = file_info['id']
    
        result = get(f'{ENDPOINT}/drives/{drive_id}/items/{file_id}/content', headers=headers)
        result.raise_for_status()
        open(file_info['name'], 'wb').write(result.content)
    
    
    ### upload file ###
    def upload(filename):

        # check to see if file exists
        path_url = urllib.parse.quote(f'{folder_path}/{filename}')
        result = get(f'{ENDPOINT}/drives/{drive_id}/root:/{path_url}', headers=headers)
        if result.status_code == 200:
            # file exists, replace its contents
            file_info = result.json()
            file_id = file_info['id']
            result = put(
                f'{ENDPOINT}/drives/{drive_id}/items/{file_id}/content',
                headers={
                    'Authorization':''.join(['Bearer ',access_token]),
                    'Content-type': 'application/binary'
                },
                data=open(filename, 'rb').read()
            )

        elif result.status_code == 404:
            # file does not exist, create a new item
            folder_url = urllib.parse.quote(folder_path)
            result = get(f'{ENDPOINT}/drives/{drive_id}/root:/{folder_url}', headers=headers)
            result.raise_for_status()
            folder_info = result.json()
            folder_id = folder_info['id']

            file_url = urllib.parse.quote(filename)
            result = put(
                f'{ENDPOINT}/drives/{drive_id}/items/{folder_id}:/{file_url}:/content',
                headers={
                    'Authorization':''.join(['Bearer ',access_token]),
                    'Content-type': 'application/binary'
                },
                data=open(filename, 'rb').read()
            )
    
else:
    raise Exception('no access token in result')

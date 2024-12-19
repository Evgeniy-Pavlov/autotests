import json
import requests

def read_conn_params(file):
    with open(file, 'r') as f:
        data = json.load(f)
    return data

def get_token_admin(base_url):
    with open('admin_cred.json', 'r') as f:
        data = json.load(f)
    session = requests.Session()
    result = session.post(f'{base_url}/index.php?route=api/login', data=data).text
    return result


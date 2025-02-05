import json
import random
from string import ascii_lowercase
from hashlib import sha256
import requests


def read_conn_params(file):
    with open(file, 'r') as f:
        data = json.load(f)
    return data


def get_token_admin(base_url):
    with open('admin_cred.json', 'r') as f:
        data = json.load(f)
    session = requests.Session()
    return session.post(f'{base_url}/api/login', data=data).cookies["OCSESSID"]

def generante_random_string():
    rand_len = random.randint(5, 10)
    return ''.join([ascii_lowercase[random.randint(0, len(ascii_lowercase)-1)] for x in rand_len])

def generate_random_password():
    return sha256(generante_random_string()).hexdigest()
import json


def read_conn_params(file):
    with open(file, 'r') as f:
        data = json.load(f)
    return data

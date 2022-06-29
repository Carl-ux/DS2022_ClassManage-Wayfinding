'''
Date: 2022-06-13 17:13:01
LastEditors: Azus
LastEditTime: 2022-06-13 17:33:11
FilePath: /DS/backend/Server/client.py
'''

import requests 
SERVER_ADDR = 'http://127.0.0.1:5000/'
def postStudent(): 
    payload = {
        "name": "example"
    }
    res = requests.post(SERVER_ADDR+'api/student', payload)
    print(res)

postStudent()

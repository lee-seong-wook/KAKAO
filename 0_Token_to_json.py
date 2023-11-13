#나에게 보내기 Token 저장 코드

import requests
import json

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = 'REST API 키'
redirect_uri = 'https://example.com/oauth'
authorize_code = '주소에서 받은 Access Token값'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# Token저장
with open(r"파일을 저장할 저장경로/Token.json","w") as fp:
    json.dump(tokens, fp)

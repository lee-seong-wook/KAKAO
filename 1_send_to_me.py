import requests
import json

with open(r"파일을 저장해 놓은 경로/Token.json","r") as fp:
    tokens = json.load(fp)

url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

headers={
    "Authorization" : "Bearer " + tokens["access_token"]
}

data={
    "template_object": json.dumps({
        "object_type":"text",
        "text":"메시지가 도착했습니다. 확인해주세요.",
        "link":{
            "web_url":"www.google.com"
        }
    })
}

response = requests.post(url, headers=headers, data=data)
response.status_code

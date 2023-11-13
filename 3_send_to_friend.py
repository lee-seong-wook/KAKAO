import requests
import json

with open(r"파일을 저장해 놓은 경로/Token.json","r") as fp:
    tokens = json.load(fp)

friend_url = "https://kapi.kakao.com/v1/api/talk/friends"


headers={"Authorization" : "Bearer " + tokens["access_token"]}

result = json.loads(requests.get(friend_url, headers=headers).text)
friends_list = result.get("elements")
print(friends_list)
print("\n")
friend_id = friends_list[0].get("uuid")
print(friend_id)

send_url= "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"

data={
    'receiver_uuids': '["{}"]'.format(friend_id),
    "template_object": json.dumps({
        "object_type":"text",
        "text":"테스트 전송 성공",
        "link":{
            "web_url":"www.google.com",
        },
        "button_title": "지금 확인"
    })
}

response = requests.post(send_url, headers=headers, data=data)
response.status_code

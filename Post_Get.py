import json
import requests
import base64


'''
with open("img.txt") as f:
    data = f.read()

data = base64.b64decode(data)

with open("img.png","wb") as f:
    f.write(data)


'''
msg_dict = {}
with open("id_rsa.pub") as f:
    msg_dict["key"] = f.read()

post_data = json.dumps(msg_dict)

url = 'https://pandora.sumsc.xin/ssh'


header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    'Content-Type':'application/json'

}

req = requests.post(url=url,data=json.dumps(msg_dict),headers=header)

print(req.text)

import sys
sys.stdout.reconfigure(encoding='utf-8')

import os
import urllib.parse

# get / post 요청 구분
method = os.environ.get('REQUEST_METHOD','GET')

if method == 'POST':
    length = int(os.environ.get('CONTENT_LENGTH', 0))
    body = sys.stdin.read(length)

else:       # get 일 때 
    body = sys.environ.get('QUERY_STRING','')

params = urllib.parse.parse_qs(body)

irum = params.get('name', [''])[0]
junhwa = params.get('phone', [''])[0]
gen = params.get('gen', [''])[0]

## 파이썬으로 작업하다가 출력을 html로 하는 것.
print('Content-Type:text/html; charset=utf-8')

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>friends</title>
</head>
<body>
    <b>친구 정보</b>
    <br/>
    일반 사용자가 전송한 값 : 이름은 {0}, 전화는 {1}, 성별은 {2}
    <br/>
    <a href='../index.html'>메인으로</a>
</body>
</html>
""".format(irum, junhwa, gen))
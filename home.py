#!/usr/local/bin/python3
#-*-Encoding: UTF-8 -*-#
print("Content-Type: text/html")
print()

import cgi

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()

print('''<!doctype html>
<html>
<head>
  <title>AQUI :: 굿노트 커뮤니티</title>
  <meta charset="utf-8">
  <link rel="stylesheet" href="aqui.css">
</head>
<body>
  <div id="logo"><a href="home.py" tatget="blank">
  <p align="center"><img border="0" src="./image/aqui_logo.jpg" width="150"></p></a></div>

  <span id="list">
  <ul>
    <a href="download.py">굿노트 스티커</a>
    <a href="youtube.py">다꾸 영상</a>
  </ul>
  </span>

  <div id="homeBody">
  <p>굿노트 커뮤니티 AQUI에 오신 것을 환영합니다!</p>
  </div>
</body>
</html>
''')

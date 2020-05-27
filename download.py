#!/usr/local/bin/python3
#-*-Encoding: UTF-8 -*-#
print("Content-Type: text/html")
print()

import cgi, os, thumbList

thumbList = thumbList.list()

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('postBody/'+pageId, 'r').read()
else:
    pageId = ''
    description = '''
    <div class="postListBody">
      <ul>
          <li style="background:url(/post/yewon_20feb.jpg); background-size:cover">
          <a href="download.py?id=yewon_20feb"><img src="./image/dummy300.png" width="100%" alt="yewon_20feb"></a>
          </li>
          <li style="background:url(/post/mountain.jpg); background-size:cover"><img src="./image/dummy300.png" width="100%" alt="po">
          </li>
          <li style="background:url(/post/po.jpg); background-size:cover"><a href="download.py?id=po"><img src="./image/dummy300.png" width="100%" alt="po"></a>
          </li>
          <li style="background:url(/post/po.jpg); background-size:cover"><a href="download.py?id=po"><img src="./image/dummy300.png" width="100%" alt="po"></a>
          </li>
      </ul>
    </div>
    '''

print('''<!doctype html>
<html>
<head>
  <title>AQUI : 굿노트 스티커</title>
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
  <p>{desc}</p>

</body>
</html>
'''.format(title=pageId, desc=description))

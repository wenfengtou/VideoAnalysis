# coding=utf-8

import os	#Python�ı�׼���е�osģ������ձ�Ĳ���ϵͳ����
import re	#����������ʽ����
import urllib	#���ڶ�URL���б����
import guiClass
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler  #����HTTP������ص�ģ��
from urllib import unquote

#�Զ��崦��������ڴ���HTTP����
class TestHTTPHandler(BaseHTTPRequestHandler):
	#����GET����
    def do_GET(self):
		#ҳ�����ģ���ַ���
        templateStr = '''
<html>  
<head>  
<title>QR Link Generator</title>  
</head>  
<body>  
%s
<br>  
<br>  
<form action="/qr" name=f method="GET"><input maxLength=1024 size=70  
name=s value="" title="Text to QR Encode"><input type=submit  
value="Show QR" name=qr>  
</form>
</body>
</html> '''

	app = guiClass.GUI()
	app.version = 'Video Downloader Beta 0.9.4 r(20161221)'
	app.appVer = 0.94
	app.appUrl = 'http://evilcult.github.io/Video-Downloader'
	app.gitUrl = 'https://github.com/EvilCult/Video-Downloader'
	app.feedUrl = 'https://github.com/EvilCult/Video-Downloader/issues'

	#print(app.fileList)
	# ��������ʽ�����Pattern����
	pattern = re.compile(r'/qr\?s=(.*?)\&qr=Show\+QR')
	#/qr?s=http://v.youku.com/v_show/id_XMjY4NzYyNDgwOA==.html?spm=a2hww.20023042.ykRecommend.5~5!2~5~5~A&qr=Show+QR
	# ʹ��Patternƥ���ı������ƥ�������޷�ƥ��ʱ������None
	print("path = "+unquote(self.path))
	match = pattern.match(self.path)
	qrImg = ''	
	items=re.findall(pattern,unquote(self.path))
	if len(items):
		print("items = "+items[0])
		app.initUrl = items[0]
	else:
		app.initUrl = 'http://v.youku.com/v_show/id_XMjY4ODc1OTU5Mg==.html?spm=a2hww.20023042.m_230771.5~5!2~5~5!4~5~5~A'

	app.getUrl()

	if len(app.fileList):
		downloadlink = '<a href="'+app.fileList[0] +'" target="_blank" title="��������">'+ app.fileList[0] +'</a>'
	else:
		downloadlink = 'null'

	print("downloadlink = "+downloadlink)
	#if match:
		# ʹ��Match��÷�����Ϣ
	#	qrImg = '<img src="http://chart.apis.google.com/chart?chs=300x300&cht=qr&choe=UTF-8&chl=' + match.group(1) + '" /><br />' + urllib.unquote(match.group(1)) 

	self.protocal_version = 'HTTP/1.1'	#����Э��汾
	self.send_response(200)	#������Ӧ״̬��
	self.send_header("Welcome", "Contect")	#������Ӧͷ
	self.end_headers()
	#self.wfile.write(templateStr % qrImg)	#�����Ӧ����
	self.wfile.write(templateStr % downloadlink)	#�����Ӧ����
	
#����������
def start_server(port):
    http_server = HTTPServer(('', int(port)), TestHTTPHandler)
    http_server.serve_forever()	#����һֱ��������������

#os.chdir('static')	#�ı乤��Ŀ¼�� static Ŀ¼
start_server(8000)	#�������񣬼���8000�˿�
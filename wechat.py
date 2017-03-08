
import itchat
import time
from PIL import ImageGrab

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
	massage=["send 'screen' to get current screen. or send 'detail' to get details"]
	if msg['Text'] == "screen":
		im=ImageGrab.grab()
		localtime=str(time.time())
		im.save(localtime+".jpg")
		itchat.send_image(localtime+".jpg",toUserName='filehelper')
		return localtime
	elif msg['Text'] == "detail":
		f=open('info.log','r')
		detail=f.readlines()
		print len(detail),detail[len(detail)-1]
		itchat.send(detail[len(detail)-1], toUserName='filehelper')
	else:
		itchat.send(massage[0], toUserName='filehelper')

itchat.auto_login(hotReload=True)
itchat.run()
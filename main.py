#-*- coding:utf-8 -*-
import itchatmp

itchatmp.update_config(itchatmp.WechatConfig(
    token='iloveyy1314',
    appId = 'wx9e77f84e28b0a204',
    appSecret = '68c024da4eed3a948a3f2c0a0b6d5f72'))
'''
@itchatmp.msg_register(itchatmp.content.TEXT)
def text_reply(msg):
    return msg


if __name__ == '__main__':
    itchatmp.run()
'''

infoDict = {
    'Title' : u'exploit',
    'Description' : u'exploit windows7 through winrar', }
r = itchatmp.messages.upload(itchatmp.content.IMAGE, 'a.jpg',
    additionalDict=infoDict, permanent=True)
if r:
    print(r['media_id'])
else:
    print('Failed: \n%s' % r)
#-*- coding:utf-8 -*-
from pytube import YouTube

yt = YouTube("http://www.youtube.com/watch?v=Ik-RsDGPI5Y")

# Once set, you can see all the codec and quality options YouTube has made
# available for the perticular video by printing videos.

print(yt.get_videos())
#!/usr/bin/env python
import sys
import pafy


pafy.set_api_key('youtubeapikeygoeshere')

url = sys.argv[1:]
url = (", ".join(url))#wtf python!  *--8=====D~~
print(url)
video = pafy.new(url)
print(unicode(video.title))
bestaudio = video.getbestaudio(preftype="m4a")
bestaudio.download()
#bestvideo = video.getbest(preftype="webm")
bestvideo = video.getbest()
bestvideo.download()

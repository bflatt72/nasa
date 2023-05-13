#!/usr/bin/env python3


import re
import os
import time
import json
import requests
import urllib.request

URL = "https://api.nasa.gov/planetary/apod?api_key=745JJhk2mOmebvwPrnAT6jS0V0MIrtglP94Xfan1"

try:
	image_data = json.loads(requests.get(URL).text)
	image_url = image_data['url']
	image_hd_url = image_data['hdurl']
	image_name = image_data['title'].split()[0] + '.jpg'
	file_path = os.environ['HOME'] + '/Pictures/' + image_name
	if(os.path.exists(file_path)) is False:
		try:
			urllib.request.urlretrieve(image_hd_url, filename=file_path)
			image_desc = image_hd_url
		except urllib.error.HTTPError:
			urllib.request.urlretrieve(image_url, filename=file_path)
			image_desc = image_url

		command = 'gsettings set org.gnome.desktop.background picture-uri file://'+file_path
		os.system(command)
		notify = 'notify-send -u critical "Wallpaper for the Day updated!" "' + image_desc + '"'
		os.system(notify)
	else:
		notify = 'notify-send -u critical "NASA Wallpaper" "Wallpaper for the day has been updated already!"'
		os.system(notify)
except:
	notify = 'notify-send -u critical "NASA Wallpaper" "Wallpaper can\'t be updated!"'
	os.system(notify)

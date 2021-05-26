import os
import requests
import urllib.request
url = "https://api.bluelytics.com.ar/v2/latest"

file = urllib.request.urlopen(url)


for line in file:

	decoded_line = line.decode("utf-8")

	print(decoded_line)

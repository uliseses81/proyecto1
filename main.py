#publicacion diaria del precio del dolar
#https://api.bluelytics.com.ar/v2/latest
import os
from instabot import Bot
import shutil
import json
import Iterable

#from .prepare import delete_credentials, get_credentials
#import uuid
try:
    os.rename("garnier.jpg.REMOVE_ME","garnier.jpg")
except Exception as e:
    print("gg")

shutil.rmtree("/home/ulises/Documents/insta-bot/config")



mi_bot=Bot()
print("iniciando sesion")
mi_bot.login(username='pakoteomuerte',
password='ulicagon123')
print("sesion iniciada")
dolar_api= exec(open("./readApi.py").read())
print('dolar_api')
dolar = json.loads(str(dolar_api))
photo = mi_bot.upload_photo("garnier.jpg", caption=dolar+" "+oficial +""+  value_avg)
print (photo)
_student=student()
_student.address()
_student.contact()
for post in all_posts:
    print(bot.get_media_info(post))

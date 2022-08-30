#google ドライブとつなぐためのライブラリ
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
#インターネットに公開するライブラリ
import streamlit as st
#画像を簡単に処理するライブラリ
from PIL import Image, ImageFilter
#数的処理するライブラリ
import numpy as np
import pickle
import os

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

name = st.text_input('name')
field = st.file_uploader('field',type = 'png')

#img_path2 = 'imgs'
st.markdown('#画像を保存するデモ')

#テキストをGoogleDriveに保存
#if field:
#    f = drive.CreateFile({'title':'test.txt'})
#    #im = Image.open(field)
#    #im = np.array(im)
#    f.SetContentString('test')
#    f.Upload()
#    st.text('アップロード完了')

st.text(os.getcwd())

import glob

files = glob.glob("./*")
for file in files:
    st.text(file)



if field:
    st.markdown(f'{field.name}をアップロードしました。')
    #img_path = os.path.join(img_path2,field.name)
    #st.text(img_path)
    st.text(os.getcwd())
    st.text(field.name)
    f = drive.CreateFile({'title':field.name,'mimeType':'image/png'})
    f.SetContentFile(field.name)
    f.Upload()
    #with open('field.png','wb') as f:
    #    f.write(field.read())

if field:
    #st.image(field)
    #st.text(type(field)) #
    im = Image.open(field)
    st.text(type(im)) #PIL image
    #im = np.array(im)
    #st.text(type(im)) #ndnarry型

close = st.file_uploader('close')
if close:
    im2 = Image.open(close)
    #im2 = np.array(im2)
    #st.text(type(im2))


if name and field and close:
    data = [name,im,im2] #ndarray でないとリストに入らないわけでない。
    st.image(data[1])
    #tt = Image.fromarray(data[2])
    st.image(data[2])
    #Image.open(tt)
    st.text(data[0])

IMG_PATH = 'img'

st.markdown('#画像を保存するデモ')


#with open('pickled.pkl', 'wb') as f:
#    pickle.dump(data, f)

#with open('pickled.pkl', 'rb') as f:
#    data2 = pickle.load(f)

#st.text(data2[0])

#データをドライブに入れる。
#f = drive.CreateFile({'title': 'TEST.TXT'})
#f.SetContentString('Hello')
#f.Upload()

#google ドライブとつなぐためのライブラリ
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
#インターネットに公開するライブラリ
import streamlit as st
#画像を簡単に処理するライブラリ
from PIL import Image, ImageFilter
#数的処理するライブラリ
import numpy as np

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

name = st.text_input('name')
field = st.file_uploader('field')

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
    data = [name,im,im2]
    tt = Image.fromarray(data[2])
    st.image(tt)
    #Image.open(tt)
    st.text(data[0])
    
#with open('pickle.data', 'wb') as f:
#    pickle.dump(data, f)


#データをドライブに入れる。
#f = drive.CreateFile({'title': 'TEST.TXT'})
#f.SetContentString('Hello')
#f.Upload()

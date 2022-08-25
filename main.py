from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import streamlit as st
#画像を簡単に処理するライブラリ
from PIL import Image, ImageFilter

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

name = st.text_input('name')
field = st.file_uploader('field')
im = Image.open(field)
st.text(type(im))
close = st.file_uploader('close')
st.text(type(close))


#データをドライブに入れる。
#f = drive.CreateFile({'title': 'TEST.TXT'})
#f.SetContentString('Hello')
#f.Upload()

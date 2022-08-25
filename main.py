from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import streamlit as st

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

name = st.text_input('name')
field = st.camera_input('field')
close = st.camera_input('close')

#データをドライブに入れる。
#f = drive.CreateFile({'title': 'TEST.TXT'})
#f.SetContentString('Hello')
#f.Upload()
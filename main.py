from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import streamlit as st

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

text1 = st.text_input()
#データをドライブに入れる。
#f = drive.CreateFile({'title': 'TEST.TXT'})
#f.SetContentString('Hello')
#f.Upload()
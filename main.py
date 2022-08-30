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

st.text(os.getcwd())

#ディレクトリの場所を確認。
#import glob
#files = glob.glob("/app/google.drive/*")
#for file in files:
#    st.text(file)   

#任意フォルダにデータを入れる。
button2 = st.button('シート作成')
if button2:
#フォルダの場所をIDに指定    
    folder_id = '10Ogv7m81vckhXxmRdleo5xouy6lO6O7V'
#スプレッドシート作成
#    f =drive.CreateFile({'title':'simple',
#                        'mimeType':'application/vnd.google-apps.spreadsheet',
#                        'parents':[{'id':folder_id}]})
    f.Upload()

name = st.text_input('name')
field = st.file_uploader('field',type = 'png')

#テキストをGoogleDriveに保存
#if field:
#    f = drive.CreateFile({'title':'test.txt'})
#    f.SetContentString('test')
#    f.Upload()
#    st.text('アップロード完了')

#データの変換
#    #im = Image.open(field)
#    #im = np.array(im)

#ファイルを一度ドライブの手前のファイルに保存した後にアップロード
if field:
    st.markdown(f'{field.name}をアップロードしました。')
    with open(field.name,'wb') as f:
        f.write(field.read())
    f = drive.CreateFile({'title':field.name,
                        'mimeType':'image/png',
                        'parents':[{'id':folder_id}]})
    f.SetContentFile(field.name)
    f.Upload()
    f.clear()

close = st.file_uploader('close',type = 'png')

if close:
    st.markdown(f'{close.name}をアップロードしました。')
    with open(close.name,'wb') as f:
        f.write(close.read())
    f2 = drive.CreateFile({'title':field.name,'mimeType':'image/png'})
    f2.SetContentFile(field.name)
    f2.Upload()

button = st.button('ファルダの作成')
if button:
    f_folder = drive.CreateFile({'title':'NEW_Folder','mimeType':'application/vnd.google-apps.folder'})
    f_folder.Upload()    

#フォルダーの場所
#https://drive.google.com/drive/folders/10Ogv7m81vckhXxmRdleo5xouy6lO6O7V

#ディレクトリの確認
#import glob
#files = glob.glob("/app/google.drive/*")
#for file in files:
#    st.text(file)   

if name and field and close:
    data = [name,im,im2] #ndarray でないとリストに入らないわけでない。
    st.image(data[1])
    #tt = Image.fromarray(data[2])
    st.image(data[2])
    #Image.open(tt)
    st.text(data[0])



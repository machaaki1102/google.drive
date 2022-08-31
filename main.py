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
#テスト
st.text(os.getcwd())
import io
from googleapiclient.http import MediaIoBaseDownload
button3 = st.button('ダウンロード')
file_list = drive.ListFile().GetList()

st.text(type(file_list))
# <class 'list'>

st.text(len(file_list))
# 9

st.text(type(file_list[0]))
# <class 'pydrive.files.GoogleDriveFile'>

for f in file_list:
    st.text(f['title'])
    st.text(f['id'])

if  button3:
    file_id = drive.ListFile({'q': 'title = "image.jpg"'}).GetList()[0]['id']
    f = drive.CreateFile({'id': file_id})
    f.GetContentFile('/app/google/image.jpg')

#  request = drive.files().get_media(fileId='1MqCvA3bM9HWueE39j4Y0MmRsrYXFXjNO')
#    fh = io.FileIO(file['image.jpeg'],mode='wb')
#    downloader = MediaIoBaseDownload(fh,request)
#    st.image(downloader)

st.markdown('データ入力フォーム')

#ディレクトリの場所を確認。
#import glob
#st.text(os.getcwd())
#files = glob.glob("/app/google.drive/*")
#for file in files:
#    st.text(file)   

name = st.text_input('name')
field = st.file_uploader('field')
if field:
    st.image(field)
close = st.file_uploader('close')
if close:
    st.image(close)
#field = st.file_uploader('field',type = 'png')2

button2 = st.button('データをアップコード')
folder_id = '10Ogv7m81vckhXxmRdleo5xouy6lO6O7V' 

if button2:
#ファイルを一度ドライブの手前のファイルに保存した後にアップロードし、IDでフォルダの場所を指定
#if field:
    st.markdown(f'{field.name}をアップロードしました。')
    with open(field.name,'wb') as f:
        f.write(field.read())
    #フォルダの場所をIDに指定する
    folder_id = '10Ogv7m81vckhXxmRdleo5xouy6lO6O7V'    
    f = drive.CreateFile({'title':field.name,
                        'mimeType':'image/png,image/jpeg',
                        'parents':[{'id':folder_id}]})
    f.SetContentFile(field.name)
    f.Upload()
    f.clear()

#if close:
    st.markdown(f'{close.name}をアップロードしました。')
    with open(close.name,'wb') as f:
        f.write(close.read())
    f = drive.CreateFile({'title':close.name,
                        'mimeType':'image/png,imag/jpeg',
                        'parents':[{'id':folder_id}]})
    f.SetContentFile(close.name)
    f.Upload()
    f.clear()


#フォルダ作成
#button = st.button('ファルダの作成')
#if button:
#    f_folder = drive.CreateFile({'title':'NEW_Folder',
#                                'mimeType':'application/vnd.google-apps.folder'})
#    f_folder.Upload()    

#テキストをGoogleDriveに保存
#if field:
#    f = drive.CreateFile({'title':'test.txt'})
#    f.SetContentString('test')
#    f.Upload()
#    st.text('アップロード完了')

#データの変換
#    #im = Image.open(field)
#    #im = np.array(im)


if name and field and close:
    data = [name,im,im2] #ndarray でないとリストに入らないわけでない。
    st.image(data[1])
    #tt = Image.fromarray(data[2])
    st.image(data[2])
    #Image.open(tt)
    st.text(data[0])



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

#body
st.markdown('データ入力フォーム')
col1, col2, col3 = st.columns(3)
with col1:
    title_t = st.text_input('タイトル')
with col2:    
    ki = st.text_input('期')
with col3:
    name_id = st.text_input('番号')

field = st.file_uploader('field')
if field:
    st.image(field)
close = st.file_uploader('close')
if close:
    st.image(close)

button2 = st.button('データをアップコード')
button3 = st.button('ダウンロード')

folder_id = '10Ogv7m81vckhXxmRdleo5xouy6lO6O7V' 
download_name_a = ki + name_id + 'field'
download_name_b = ki + name_id + 'close'
#  Googledriveからデータを取る。
if  button3:
    #クエリでlist内の名前で検索、IDを取得。そのIDを使って画像取得
    file_id = drive.ListFile({'q': 'title = "image2.jpg"'}).GetList()[0]['id']
    f = drive.CreateFile({'id': file_id})
    f.GetContentFile(f['title'])
    st.image(f['title'])
    f.clear()

#ファイルを一度ドライブの手前のファイルに保存した後にアップロードし、IDでフォルダの場所を指定
if button2:
#if field:
    st.markdown(f'{field.name}をアップロードしました。')
    with open(field.name,'wb') as f:
        f.write(field.read())
    #フォルダの場所をIDに指定する
    folder_id = '10Ogv7m81vckhXxmRdleo5xouy6lO6O7V'    
    f = drive.CreateFile({'title':download_name_a,#field.name
                        'mimeType':'image/png,image/jpeg',
                        'parents':[{'id':folder_id}]})
    f.SetContentFile(field.name)
    f.Upload()
    #test
    file_id_a = drive.ListFile().GetList()[0]['id']
    st.text(file_id_a)
    f.clear()

#if close:
    st.markdown(f'{close.name}をアップロードしました。')
    with open(close.name,'wb') as f:
        f.write(close.read())
    f = drive.CreateFile({'title':download_name_b,
                        'mimeType':'image/png,imag/jpeg',
                        'parents':[{'id':folder_id}]})
    f.SetContentFile(close.name)
    f.Upload()
    f.clear()

st.text(file_id_a)
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


#ディレクトを確認。
#st.text(os.getcwd())
#file_list = drive.ListFile().GetList()
#st.text(type(file_list))
# <class 'list'>
#st.text(len(file_list))
# 9
#st.text(type(file_list[0]))
# <class 'pydrive.files.GoogleDriveFile'>
#for f in file_list:
#    st.text(f)
#    st.text(f['id'])

#ディレクトリの場所を確認。
#import glob
#st.text(os.getcwd())
#files = glob.glob("/app/google.drive/*")
#for file in files:
#    st.text(file)   


#if name and field and close:
#    data = [name,im,im2] #ndarray でないとリストに入らないわけでない。
#    st.image(data[1])
#    #tt = Image.fromarray(data[2])
#    st.image(data[2])
#    #Image.open(tt)
#    st.text(data[0])



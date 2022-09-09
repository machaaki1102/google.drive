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
import pandas as pd
import csv
#
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

#body
st.markdown('データ入力フォーム')
col1, col2, col3,col4 = st.columns(4)
with col1:
    id_id = st.text_input('id')
with col2:
    title_t = st.text_input('タイトル')
with col3:    
    ki = st.text_input('期')
with col4:
    name_id = st.text_input('番号')

field = st.file_uploader('field')
#if field:
#    st.image(field)
close = st.file_uploader('close')
#if close:
#    st.image(close)

data_long = st.number_input('long')
data_spat = st.number_input('spat')

button_upload = st.button('入力データ保存')
button_download = st.button('保存データ呼び出し')

folder_id = '10Ogv7m81vckhXxmRdleo5xouy6lO6O7V' 
download_name_a = ki + name_id + 'field.jpeg'
download_name_b = ki + name_id + 'close.jpeg'

fx = 0
fb = 0

#openxlテスト
#import os
import openpyxl
#from PIL import Image 
#os.chdir('/content/drive/MyDrive')
#ファイルを作成し、データ（数字）を入力
excel = st.button('excel')
if excel:
    wb = openpyxl.Workbook()
#ws = wb.active
#ws['A1'] = 10
#wb.save('aa.xlsx')
#print(os.getcwd())
#画像を入力
#wc = openpyxl.load_workbook('aa.xlsx')
    
#画像選択 png形式はRGBA　jpeg形式はRGB
    file_id = drive.ListFile({'q': 'title = "dd.png"'}).GetList()[0]['id']
    f = drive.CreateFile({'id': file_id})#ファイルを読み込みして、見えないカレントディレクトリ内に見えないが保存されている。絶対パスで
    f.GetContentFile('dd.png')
    
    wc = wb.active
    img_dir = 'dd.png' #width:916,height:685 #width,height = img.size #print(width,height)
    img = Image.open(img_dir).convert('RGB')
#リサイズ
#img = Image.open(img_dir)
    img_re = img.resize((300,200))
    img_re.save(img_dir)

    img_to = openpyxl.drawing.image.Image(img_dir)
    wc.add_image(img_to,'B3')
    wb.save('aa.xlsx')

excel_up = st.button('excel_up')
if excel_up:
    #フォルダの場所をIDに指定する
    folder_id = '10Ogv7m81vckhXxmRdleo5xouy6lO6O7V'    
    f = drive.CreateFile({'title':'aa.xlsx',#field.name
                        'mimeType':'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                        'parents':[{'id':folder_id}]})
    f.SetContentFile('aa.xlsx')
    f.Upload()
    f.clear()
#ディレクトリの場所を確認。
import glob
st.text(os.getcwd())
files = glob.glob("/app/google.drive/*")
for file in files:
    st.text(file)   

#  Googledriveからデータを取る。
#if  button_download:
    #クエリでlist内の名前で検索、IDを取得。そのIDを使って画像取得
#    file_id = drive.ListFile({'q': 'title = "image2.jpg"'}).GetList()[0]['id']
#    f = drive.CreateFile({'id': file_id})
#    f.GetContentFile(f['title'])
#    st.image(f['title'])
#    f.clear()

#グーグルドライブにあるdf.csvを取得する。
if  button_download:
    #クエリでtitle＝ファイル名で検索して、IDを取得する。
    file_id = drive.ListFile({'q': 'title = "df.csv"'}).GetList()[0]['id']
    #取得したIDでファイル作る。
    #st.text(file_id)
    f = drive.CreateFile({'id': file_id})
    #ファイルを読み込みして、見えないカレントディレクトリ内に見えないが保存されている。絶対パスで
    f.GetContentFile('df.csv')
    
    #GOOGLEドライブ内のdf.csvがうまく取り込めないので、DataFrameに変換して取り込む
    with open('df.csv','r') as f:
        df = pd.DataFrame(f)
        #t.dataframe(df)
        list_A = df.iloc[0,0].split(',')
        list_B= df.iloc[1,0].split(',')
        data = [list_B]
        df = pd.DataFrame(data,columns=list_A)
        #df2 = pd.concat([df_i, df_a], axis=0)
        st.dataframe(df)

folder_id = '10Ogv7m81vckhXxmRdleo5xouy6lO6O7V'    

#ファイルを一度ドライブの手前のファイルに保存した後にアップロードし、IDでフォルダの場所を指定
if button_upload:
#if field:
    #st.markdown(f'{field.name}をアップロードしました。')
    with open(field.name,'wb') as f:
        f.write(field.read())
    #フォルダの場所をIDに指定する
    #folder_id = '10Ogv7m81vckhXxmRdleo5xouy6lO6O7V'    
    f = drive.CreateFile({'title':download_name_a,#field.name
                        'mimeType':'image/png,image/jpeg',
                        'parents':[{'id':folder_id}]})
    f.SetContentFile(field.name)
    f.Upload()

    file_id_a = drive.ListFile().GetList()
    fx = file_id_a['title' == download_name_a]['id']
    #st.text(fx)
    #st.write(type(fx))
    f.clear()
    #st.text(fx)

#if close:
    #st.markdown(f'{close.name}をアップロードしました。')
    with open(close.name,'wb') as f:
        f.write(close.read())
    f = drive.CreateFile({'title':download_name_b,
                        'mimeType':'image/png,imag/jpeg',
                        'parents':[{'id':folder_id}]})
    f.SetContentFile(close.name)
    f.Upload()
    file_id_b = drive.ListFile().GetList()
    fb = file_id_b['title' == download_name_b]['id']
    #st.text(fb)
    f.clear()
    
    #df1 = pd.DataFrame(data = data,columns=colmuns)
    colmuns = ['id','title','ki','number','long','spad','picture1','picture2']
    data = [id_id,title_t,ki,name_id,data_long,data_spat,fx,fb]
    
    #最初にデータを作る時
    with open('df_csv','w') as f:
         writer = csv.writer(f)
         writer.writerow(colmuns)
         writer.writerow(data)
    
    f = drive.CreateFile({'title':'df.csv',
                    'mimeType':'text/csv',
                    'parents':[{'id':folder_id}]})
    f.SetContentFile('df_csv')
    f.Upload()
    f.clear


    #既存のデータに追加する時

    #クエリでtitle＝ファイル名で検索して、IDを取得する。
    file_id = drive.ListFile({'q': 'title = "df.csv"'}).GetList()[0]['id']
    f = drive.CreateFile({'id': file_id})
    f.GetContentFile('df.csv')
    with open('df.csv','a') as f:
         writer = csv.writer(f)
         writer.writerow(data)
  

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
#    st.text(f['title'])
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



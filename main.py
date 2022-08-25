from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

f = drive.CreateFile({'title': 'TEST.TXT'})
f.SetContentString('Hello')
f.Upload()

#dd
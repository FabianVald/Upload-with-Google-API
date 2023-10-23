from googleapiclient.http import MediaFileUpload
from Google import Create_Service
import os
import time
from httplib2 import ServerNotFoundError


CLIENT_SECRET_FILE = 'credentials.json'       
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']
#mime_types = 'application/zip'
folder_id = '13rxta1ojwg6Orit_j4ms43jhideBTitW'           #ID de la Carpeta de Drive 
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION,SCOPES)




path = './forUpload'                                      #Ruta donde estan mis archivos


def subirArchivos(path):
    fileNames = os.listdir(path)
    if len(fileNames) < 1:
        return print('No hay archivos en la carpeta')
    for file_name in fileNames:        
        file_metadata = {
            'name':file_name,
            'parents':[folder_id]
        }
        media = MediaFileUpload(path+"/"+'{0}'.format(file_name),resumable=True)
        time_inicio = time.time()
        
        service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
            ).execute()   
        
        
        time_final = time.time()
        os.remove(path+"/"+'{0}'.format(file_name))
        print('Upload has been Succesfull in: ', round(time_final-time_inicio),' seconds','The file has been deleted in the PC')
        

if __name__ == "__main__":
    subirArchivos(path)
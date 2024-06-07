import cloud_delete

file_path = ''  # Ruta del archivo
folder_id = ''  # ID de la carpeta en Google Drive

uploaded_file_id = cloud_delete.upload_file(file_path, folder_id)
if uploaded_file_id:
    print(f'Archivo subido correctamente con ID: {uploaded_file_id}')
else:
    print('Error al subir el archivo a Google Drive.')
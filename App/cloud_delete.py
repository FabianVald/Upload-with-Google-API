import os.path
import mimetypes
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

# pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

# Si modificas estos alcances, elimina el archivo token.json.
SCOPES = ["https://www.googleapis.com/auth/drive.file"]

def authenticate_and_build_service():
    creds = None
    # El archivo token.json almacena los tokens de acceso y actualización del usuario,
    # y se crea automáticamente cuando se completa el flujo de autorización por primera vez.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # Si no hay credenciales disponibles (válidas), permite al usuario iniciar sesión.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Guarda las credenciales para la próxima ejecución
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return build("drive", "v3", credentials=creds)

# Función para obtener el MIME type
def get_mime_type(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type if mime_type else 'application/octet-stream'

# Función para subir un archivo
def upload_file(file_path, folder_id=None):
    service = authenticate_and_build_service()

    mime_type = get_mime_type(file_path)
    file_metadata = {'name': os.path.basename(file_path)}
    if folder_id:
        file_metadata['parents'] = [folder_id]

    media = MediaFileUpload(file_path, mimetype=mime_type)

    try:
        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()

        print(f'File ID: {file.get("id")}')
        
        if file.get("id"):
            # Cerrar el archivo para asegurarse de que no esté siendo utilizado
            media._fd.close()
            # Eliminar el archivo local después de la subida exitosa
            os.remove(file_path)
            print(f'File {file_path} has been uploaded and deleted locally.')
        
    except HttpError as err:
        print(f'An error occurred: {err}')
        file = None

    return file
# Upload-Module-with-Google-API

- [Installation](#Installation)
- [Use](#IUse)



## Installation

1. clone the repository: git clone https://github.com/FabianVald/Upload-with-Google-API.git

2. The quick start guides explain how to set up and run an app that calls a Google Workspace API, which is why you need to complete this form (https://developers.google.com/docs/api/quickstart/python?hl=es-419). In particular, you must enable the Si hace uso de este módulo genere los agradecimientos correspondientesAPI, set up the OAuth consent screen and Authorize credentials for a desktop application.

3. Install dependencies from requirements.txt: pip install -r requirements.txt
   
## Use

1. Place all python files in the same folder as credentials.json.
2. Inside the main.py or function module use (cloud_delete.py) file modify the "folder_id" to the desired one (corresponding to the Drive folder where the files are expected to be stored) and the path of the file to upload.
3. Create a folder inside your current working directory called "forUpload" and store the files you expect to upload in it.
5. Run the main.py or execute de function to upload the file located in the forUpload folder.
6. Warning! The file it's will deleted after upload process.

If you use this module, please thank Fabian Valderrama and Google.

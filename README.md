# Upload-Module-with-Google-API

- [Installation](#Installation)
- [Use](#IUse)



## Installation

0. clone the repository: git clone https://github.com/FabianVald/Upload-with-Google-API/tree/main

1. The quick start guides explain how to set up and run an app that calls a Google Workspace API, which is why you need to complete this form (https://developers.google.com/docs/api/quickstart/python?hl=es-419). In particular, you must enable the API, set up the OAuth consent screen and Authorize credentials for a desktop application.

2. Install dependencies from requirements.txt
   
## Use

1. Place all python files in the same folder as credentials.json.
2. Inside the main.py file modify the "folder_id" to the desired one (corresponding to the Drive folder where the files are expected to be stored).
3. Create a folder inside your current working directory called "forUpload" and store the files you expect to upload in it.
5. Run the main.py file to upload all files located in the forUpload folder.

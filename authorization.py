import os
import io
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

# gets credentials
def authenticate():

    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

# creates drive api client
def build_api():

    # credentials
    temp_creds = authenticate()

    # create drive api client
    service = build('drive', 'v3', credentials=temp_creds)
    return service

#downloads file
def download_csv(file_id, destination):

    # creates drive api client
    service = build_api()

    # gets file from Google drive
    request = service.files().get_media(fileId=file_id)

    # downloads file from Google dive
    try:
        fh = io.FileIO(destination, 'wb')
    except Exception as e:
        print(f'Failed to open file : {e}')
        
    downloader = MediaIoBaseDownload(fh, request)
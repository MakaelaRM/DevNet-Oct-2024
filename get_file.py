import os
import io
from tkinter import Image
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from PIL import Image

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']


def authenticate():

    creds = None

    #gets credentials
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


def build_api():

    # credentials
    temp_creds = authenticate()

    # create drive api client
    service = build('drive', 'v3', credentials=temp_creds)
    return service


def download_csv(file_id, destination):

    # creates drive api client
    service = build_api()

    try:
        # gets file from Google drive
        request = service.files().get_media(fileId=file_id)
        # open the local file in binary write mode
        with io.FileIO(destination, 'wb') as fh:
            # initialize MediaIoBaseDownload with the file handle and request
            downloader = MediaIoBaseDownload(fh, request)
            done = False

            # loops through each chunk and download the file until completed
            while not done:
                done = downloader.next_chunk()

    except Exception as e:
        print(f"Error during download: {e}")
        
# Download the most recent image in the folder
def download_last_image_in_folder(folder_id, destination):
    service = build_api()
    
    # List files in folder (ordered by created time in descending order)
    query = f"'{folder_id}' in parents and mimeType contains 'image/'"
    results = service.files().list(
        q=query,
        fields="files(id, name, createdTime)",
        orderBy="createdTime desc", 
        pageSize=1 
    ).execute()
    
    files = results.get('files', [])
    if not files:
        print("No images found in the folder.")
        return None

    # Get the ID and name of the latest file
    latest_file = files[0]
    file_id = latest_file['id']
    file_name = latest_file['name']
    
    # Download the image to destination
    request = service.files().get_media(fileId=file_id)
    with io.FileIO(destination, 'wb') as fh:
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            done = downloader.next_chunk()
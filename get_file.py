import authorization

def find_file(file_id):

    try:
        # create drive api client
        service = authorization.build_api()
        
        print(f"Trying to find file with ID: {file_id}")

        # Use the files().get() method to retrieve the file metadata
        csv_file = service.files().get(fileID=file_id).execute()

        # Print the file details
        print("Yayyy file found:")
        print("Name:", csv_file.get('name'))
        print("MIME Type:", csv_file.get('mimeType'))
        print("ID:", csv_file.get('id'))

    except:
        print('Failed to get file')

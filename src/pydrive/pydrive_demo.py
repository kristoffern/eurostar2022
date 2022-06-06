from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials

gauth = GoogleAuth()
scope = ["https://www.googleapis.com/auth/drive"]
gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secrets.json', scope)
drive = GoogleDrive(gauth)

print(drive)

file1 = drive.CreateFile({'title': 'testdata.tar.gz', 'mimeType': 'application/gzip'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
file1.SetContentFile('testdata.tar.gz') # Set content of the file from given string.
file1.Upload()

# Insert the permission.
permission = file1.InsertPermission({
                        'type': 'anyone',
                        'value': 'anyone',
                        'role': 'reader'})

print(file1['alternateLink'])  # Display the sharable link.
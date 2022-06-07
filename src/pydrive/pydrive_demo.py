"""
    Example code showing how you can authenticate with a json credential file
    from a service account in Google Cloud.

"""

from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials

gauth = GoogleAuth()
scope = ["https://www.googleapis.com/auth/drive"]
gauth.auth_method = 'service'
gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name('eurostar-2022-1cf61be6884d.json', scope)
drive = GoogleDrive(gauth)

file1 = drive.CreateFile({'title': 'reports.zip', 'mimeType': 'application/zip'})
file1.SetContentFile('reports.zip')
file1.Upload()

file1.InsertPermission({
    'type': 'anyone',
    'value': 'anyone',
    'role': 'reader'
    })

print(file1['alternateLink'])
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

class GoogleDriveApi:
    def __init__(self):
        gauth = GoogleAuth()
        self.drive = GoogleDrive(gauth)

    def upload(self,folder_id,upload_file_list):
        for upload_file in upload_file_list:
            gfile = self.drive.CreateFile({'parents': [{'id': folder_id}]})
            gfile.SetContentFile(upload_file)
            gfile.Upload()

    def listFile(self,folder_id):
        file_list = self.drive.ListFile(
            {'q': "'{}' in parents and trashed=false".format(folder_id)}).GetList()
        for file in file_list:
            print('title: %s, id: %s' % (file['title'], file['id']))
        return file_list

    def DownloadFile(self,folder_id):
        file_list = self.listFile(folder_id)
        for i, file in enumerate(sorted(file_list, key=lambda x: x['title']), start=1):
            print('Downloading {} file from GDrive ({}/{})'.format(file['title'], i, len(file_list)))
            file.GetContentFile(file['title'])

    def createTxt(self,folder_id,name,content):
        file1 = self.drive.CreateFile({'parents': [{'id': folder_id}], 'title': f'{name}.txt'})
        file1.SetContentString(content)
        file1.Upload()

api = GoogleDriveApi()
# api.upload('1wSOGKRY6ZqT4aBWmfc_CsLtS6iEHqQKy',['dcard_crawler.csv'])
# file_list = api.listFile('1jNvdWZEI0iS3sODsc4PvjD78je4guqXi')
# api.DownloadFile('1pk6_TIMVjxdIoKwWe34t-QyVIeaCcrGd')
# api.createTxt('1wSOGKRY6ZqT4aBWmfc_CsLtS6iEHqQKy','test','12345')

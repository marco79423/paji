import dropbox
from dropbox.exceptions import ApiError
from dropbox.files import WriteMode
from paji_sdk.base.exceptions import BaseError


class DropboxStorage:
    def __init__(self, token):
        self.token = token

    def upload(self, path, data):
        with dropbox.Dropbox(self.token) as dbx:
            try:
                print('上傳檔案到', path)
                dbx.files_upload(data, path, mode=WriteMode('overwrite'))
            except ApiError as err:
                raise BaseError(err.user_message_text)

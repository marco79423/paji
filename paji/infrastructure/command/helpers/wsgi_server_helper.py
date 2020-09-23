from paji.domain.command import helpers


class WSGIServerHelper(helpers.WSGIServerHelperBase):

    def serve(self, host: str, port: int, is_dev: bool):
        print(f'啟動 paji 伺服器 (http://{host}:{port}) 開發者模式：{is_dev}')

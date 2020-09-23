from paji.command.domain import helpers


class WSGIServerHelper(helpers.WSGIServerHelperBase):

    def __init__(self, console_helper: helpers.ConsoleHelperBase):
        self._console_helper = console_helper

    def serve(self, host: str, port: int, is_dev: bool):
        self._console_helper.print(f'啟動 paji 伺服器 (http://{host}:{port}) 開發者模式：{is_dev}')

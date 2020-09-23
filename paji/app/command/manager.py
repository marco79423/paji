class Manager:

    def hello(self, name):
        print(f'哈囉 {name}')

    def run_server(self, host, port, is_dev):
        print(f'啟動 paji 伺服器 (http://{host}:{port}) 開發者模式：{is_dev}')

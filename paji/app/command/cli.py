import click

from .manager import Manager


def create_cli(manager: Manager):
    @click.group()
    def cli():
        """兩大類專案中台"""
        pass

    @cli.command('hello', short_help='打個招呼')
    @click.argument('name')
    def hello(name):
        manager.hello(name=name)

    @cli.command('serve', short_help='啟動 paji 服務')
    @click.option('--host', default='0.0.0.0', help='啟動的 host')
    @click.option('-p', '--port', default=8000, help='啟動的 port')
    @click.option('-d', '--dev', is_flag=True, default=False, help='開發者模式')
    def serve(host, port, dev):
        manager.run_server(host=host, port=port, is_dev=dev)

    return cli

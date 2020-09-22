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

    return cli

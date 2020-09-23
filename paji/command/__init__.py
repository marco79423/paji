from paji.command.app import CommandContainer

container = CommandContainer()
cli = container.create_cli()

if __name__ == '__main__':
    cli()

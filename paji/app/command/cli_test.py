import shlex
from unittest import mock

from click.testing import CliRunner

from .cli import create_cli


def test_hello():
    manager = mock.MagicMock()

    runner = CliRunner()
    cli = create_cli(manager)
    result = runner.invoke(cli, shlex.split('hello 兩大類'))

    assert result.exit_code == 0
    manager.hello.assert_called_with(name='兩大類')


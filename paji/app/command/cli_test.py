import shlex
from unittest import mock

from click.testing import CliRunner

from paji.app.command.cli import create_cli


def test_hello():
    manager = mock.MagicMock()

    runner = CliRunner()
    cli = create_cli(manager)
    result = runner.invoke(cli, shlex.split('hello 兩大類'))

    assert result.exit_code == 0
    manager.hello.assert_called_with(name='兩大類')


def test_serve():
    manager = mock.MagicMock()

    runner = CliRunner()
    cli = create_cli(manager)
    result = runner.invoke(cli, shlex.split('serve'))

    assert result.exit_code == 0
    manager.run_server.assert_called_with(host='0.0.0.0', port=8000, is_dev=False)


def test_serve_with_host():
    manager = mock.MagicMock()

    runner = CliRunner()
    cli = create_cli(manager)
    result = runner.invoke(cli, shlex.split('serve --host 1.1.1.1'))

    assert result.exit_code == 0
    manager.run_server.assert_called_with(host='1.1.1.1', port=8000, is_dev=False)


def test_serve_with_port():
    manager = mock.MagicMock()

    runner = CliRunner()
    cli = create_cli(manager)
    result = runner.invoke(cli, shlex.split('serve --port 9527'))

    assert result.exit_code == 0
    manager.run_server.assert_called_with(host='0.0.0.0', port=9527, is_dev=False)


def test_serve_with_abbr_port():
    manager = mock.MagicMock()

    runner = CliRunner()
    cli = create_cli(manager)
    result = runner.invoke(cli, shlex.split('serve -p 9527'))

    assert result.exit_code == 0
    manager.run_server.assert_called_with(host='0.0.0.0', port=9527, is_dev=False)


def test_serve_with_dev_mode_flag():
    manager = mock.MagicMock()

    runner = CliRunner()
    cli = create_cli(manager)
    result = runner.invoke(cli, shlex.split('serve --dev'))

    assert result.exit_code == 0
    manager.run_server.assert_called_with(host='0.0.0.0', port=8000, is_dev=True)


def test_serve_with_abbr_dev_mode_flag():
    manager = mock.MagicMock()

    runner = CliRunner()
    cli = create_cli(manager)
    result = runner.invoke(cli, shlex.split('serve -d'))

    assert result.exit_code == 0
    manager.run_server.assert_called_with(host='0.0.0.0', port=8000, is_dev=True)


def test_serve_with_host_and_port():
    manager = mock.MagicMock()

    runner = CliRunner()
    cli = create_cli(manager)
    result = runner.invoke(cli, shlex.split('serve --host 1.1.1.1 --port 9527'))

    assert result.exit_code == 0
    manager.run_server.assert_called_with(host='1.1.1.1', port=9527, is_dev=False)


def test_serve_with_host_and_port_in_dev_mode():
    manager = mock.MagicMock()

    runner = CliRunner()
    cli = create_cli(manager)
    result = runner.invoke(cli, shlex.split('serve --host 1.1.1.1 --port 9527 --dev'))

    assert result.exit_code == 0
    manager.run_server.assert_called_with(host='1.1.1.1', port=9527, is_dev=True)

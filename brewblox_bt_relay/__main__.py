"""
Entrypoint for the bluetooth relay PoC
"""

import signal
import sys

import click

from brewblox_bt_relay import client, server

cli = click.CommandCollection(
    sources=[
        client.cli,
        server.cli,
    ])


def exit_handler(n, f):
    print('goodbye')
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGTERM, exit_handler)
    cli()

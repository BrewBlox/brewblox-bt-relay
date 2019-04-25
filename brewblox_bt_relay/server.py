"""
Server
"""

from subprocess import check_call

import click


@click.group()
def cli():
    """Command collector"""


@cli.command()
def server():
    print('starting server')
    check_call('rpyc_classic.py --host 0.0.0.0 --port 5010', shell=True)

"""
Client
"""

import click
import rpyc
from bluepy.btle import DefaultDelegate


@click.group()
def cli():
    """Command collector"""


class ScanDelegate(DefaultDelegate):

    def handleDiscovery(self, dev, isNewDev, isNewData):
        print(dev.addr, isNewDev, isNewData, flush=True)


@cli.command()
def client():
    try:
        print('starting client', flush=True)
        relay = rpyc.classic.connect('172.17.0.1', 5010)
        bluepy = relay.modules.bluepy

        delegate = ScanDelegate()
        scanner = bluepy.btle.Scanner().withDelegate(delegate)
    except Exception as ex:
        print(f'Startup fail: {ex}', flush=True)
        raise ex

    while True:
        try:
            print('scanning...')
            scanner.scan(timeout=6)
        except Exception as ex:
            print(f'Oh no! {ex}')
            raise ex

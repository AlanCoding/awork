
import click

from awork.api import client

from awork.cli.generics import global_params

# from awork.cli.generics import AworkCommand

__all__ = ['version']


class AworkCommand(click.core.Command):
    pass


def print_version(*args, **kwargs):
    """Display full version information."""
    click.echo('Awork %s' % 1.0)

    # Attempt to connect to the Ansible Tower server.
    # If we succeed, print a version; if not, generate a failure.
    r = client.get('/config/')
    config = r.json()
    license = config.get('license_info', {}).get('license_type', 'open')
    if license == 'open':
        server_type = 'AWX'
    else:
        server_type = 'Ansible Tower'
    click.echo('%s %s' % (server_type, config['version']))

    # Print out Ansible version of server
    click.echo('Ansible %s' % config['ansible_version'])


version = AworkCommand('version', callback=print_version, params=global_params)

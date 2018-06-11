
import click

from awork.cli.generics import CommandWithGlobals
from awork.models import server


__all__ = ['version', 'produce_schema']


def print_version():
    """Display full version information."""
    click.echo('Awork %s' % 1.0)

    # Attempt to connect to the Ansible Tower server.
    # If we succeed, print a version; if not, generate a failure.
    config = server.get_server_config()
    click.echo('%s %s' % (server.get_server_type(config), config['version']))

    # Print out Ansible version of server
    click.echo('Ansible %s' % config['ansible_version'])


version = CommandWithGlobals('version', callback=print_version)


produce_schema = CommandWithGlobals(
    'produce_schema', callback=server.produce_schema
)

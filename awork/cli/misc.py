import os
import json
import pprint

import click

from awork.api import client
from awork.cli.generics import global_params


__all__ = ['version', 'produce_schema']


class AworkCommand(click.core.Command):
    pass


def print_version():
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


def crawl_api(root_dir, addr):
    resources = client.get(addr).json()
    with open(os.path.join(root_dir, '..', '__init__.py'), 'w'):
        pass
    with open(os.path.join(root_dir, '__init__.py'), 'w'):
        pass

    for res_endpoint, addr in resources.items():
        click.echo('Obtaining OPTIONS for resource {}'.format(res_endpoint))
        res_options = client.options(addr).json()
        if 'types' not in res_options or len(res_options['types']) != 1:
            click.echo(' skipping resource because of types: {}'.format(
                res_options.get('types', None)
            ))
            continue
        res_name = res_options['types'][0]
        res_path = os.path.join(root_dir, '{}.py'.format(res_name))
        click.echo(' writing OPTIONS to {}'.format(res_path))
        with open(res_path, 'w') as f:
            f.write('endpoint = "{}"\n'.format(res_endpoint))
            pp = pprint.PrettyPrinter(indent=0, stream=f)
            for var_name, val in res_options.items():
                if var_name == 'description':
                    continue
                f.write('{} = '.format(var_name))
                pp.pprint(val)


def _produce_schema():
    if not os.path.isdir('awork'):
        raise Exception('schema command must be ran from root directory.')

    versions = client.get('/api/').json()['available_versions']

    for prefix, addr in versions.items():
        root_dir = os.path.join('awork', 'schema', 'current', prefix)
        if not os.path.isdir(root_dir):
            os.makedirs(root_dir)
        click.echo('Crawling API for version {}'.format(prefix))
        crawl_api(root_dir, addr)


produce_schema = AworkCommand('produce_schema', callback=_produce_schema,
                              params=global_params)


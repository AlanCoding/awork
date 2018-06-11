import os
import pprint

from awork.api import client

from click import echo


__all__ = ['get_server_type', 'get_server_config', 'produce_schema']


def get_server_type(config_data):
    license = config_data.get('license_info', {}).get('license_type', 'open')
    if license == 'open':
        return 'AWX'
    else:
        return 'Ansible Tower'


def get_server_config():
    r = client.get('/config/')
    return r.json()


def _crawl_api(root_dir, addr):
    resources = client.get(addr).json()
    with open(os.path.join(root_dir, '..', '__init__.py'), 'w'):
        pass
    with open(os.path.join(root_dir, '__init__.py'), 'w') as init_f:
        init_f.write('resource_list = [\n')

        for res_endpoint, addr in resources.items():
            echo(
                'Obtaining OPTIONS for resource {}'.format(res_endpoint))
            res_options = client.options(addr).json()
            if 'types' not in res_options or len(res_options['types']) != 1:
                echo(' skipping resource because of types: {}'.format(
                    res_options.get('types', None)
                ))
                continue
            res_name = res_options['types'][0]
            res_path = os.path.join(root_dir, '{}.py'.format(res_name))
            init_f.write('    "{}",\n'.format(res_name))
            echo(' writing OPTIONS to {}'.format(res_path))
            with open(res_path, 'w') as f:
                f.write('endpoint = "{}"\n'.format(res_endpoint))
                pp = pprint.PrettyPrinter(indent=0, stream=f)
                for var_name, val in res_options.items():
                    if var_name == 'description':
                        continue
                    f.write('{} = '.format(var_name))
                    pp.pprint(val)
        init_f.write(']\n')


def produce_schema():
    if not os.path.isdir('awork'):
        raise Exception('schema command must be ran from root directory.')

    versions = client.get('/api/').json()['available_versions']

    for prefix, addr in versions.items():
        root_dir = os.path.join('awork', 'schema', 'current', prefix)
        if not os.path.isdir(root_dir):
            os.makedirs(root_dir)
        echo('Crawling API for version {}'.format(prefix))
        _crawl_api(root_dir, addr)

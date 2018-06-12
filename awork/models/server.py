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


def pprint_options(path, options_data):
    with open(path, 'w') as f:
        pp = pprint.PrettyPrinter(indent=0, stream=f)
        for var_name, val in options_data.items():
            if var_name == 'description':
                continue
            f.write('{} = '.format(var_name))
            pp.pprint(val)


def _crawl_api_resource(root_dir, list_url, res_endpoint):
    echo('Obtaining OPTIONS for resource {}'.format(res_endpoint))
    list_options = client.options(list_url).json()
    list_options['endpoint'] = res_endpoint  # add backref
    # TODO: maybe implement unified job templates / jobs, maybe not
    if 'types' not in list_options or len(list_options['types']) != 1:
        echo(' skipping resource because of types: {}'.format(
            list_options.get('types', None)
        ))
        return
    res_name = list_options['types'][0]
    # make directory like awork/schema/current/v2/job_template/
    res_dir = os.path.join(root_dir, res_name)
    if not os.path.exists(res_dir):
        os.makedirs(res_dir)
    with open(os.path.join(res_dir, '__init__.py'), 'w'):
        pass
    list_path = os.path.join(res_dir, 'list.py')
    echo(' writing list schema to {}'.format(list_path))
    pprint_options(list_path, list_options)
    # try to find a detail endpoint, but some might not have any objects
    objs = client.get(list_url).json()
    if objs['count']:
        detail_url = objs['results'][0]['url']
        detail_path = os.path.join(res_dir, 'detail.py')
        detail_options = client.options(detail_url).json()
        detail_options['endpoint'] = res_endpoint
        echo('  writing detail schema to {}'.format(detail_path))
        pprint_options(detail_path, detail_options)
    return res_name


def _crawl_api_version(root_dir, addr):
    resources = client.get(addr).json()
    with open(os.path.join(root_dir, '__init__.py'), 'w') as init_f:
        init_f.write('resource_list = [\n')
        for res_endpoint, list_url in resources.items():
            res_name = _crawl_api_resource(root_dir, list_url, res_endpoint)
            if res_name:
                init_f.write('    "{}",\n'.format(res_name))
        init_f.write(']\n')


def produce_schema(release='current'):
    if not os.path.isdir('awork'):
        raise Exception('schema command must be ran from root directory.')
    if not os.path.isdir(os.path.join('awork', 'schema')):
        raise Exception('could not find base schema directory')
    os.makedirs(os.path.join('awork', 'schema', release))
    with open(os.path.join('awork', 'schema', release, '__init__.py'), 'w'):
        pass

    versions = client.get('/api/').json()['available_versions']

    for prefix, addr in versions.items():
        root_dir = os.path.join('awork', 'schema', release, prefix)
        if not os.path.isdir(root_dir):
            os.makedirs(root_dir)
        echo('Crawling API for version {}'.format(prefix))
        _crawl_api_version(root_dir, addr)

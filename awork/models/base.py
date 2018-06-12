from awork.utils.functional import cached_property
from awork.utils.grammar import action_names
from awork.api import client

import importlib


class Resource:

    def __init__(self, resource):
        self.resource = resource
        # TODO: move these into settings
        self.version = 'current'
        self.api_version = 'v2'

    def list_commands(self):
        cmd_names = []
        list_action_names = action_names.copy()
        list_action_names['GET'] = 'list'
        try:
            methods = self.list_schema.actions.keys()
            cmd_names += [list_action_names[method] for method in methods]
        except Exception:
            pass
        try:
            methods = self.detail_schema.actions.keys()
            cmd_names += [action_names[method] for method in methods]
        except Exception:
            pass
        return cmd_names

    def schema_for_command(self, name):
        if name == 'list':
            r = {}
            # take out options that are not filterable
            options = self.list_schema.actions['GET']
            for name, element in options.items():
                if element.get('filterable', False):
                    r[name] = element
            return r
        elif name == 'create':
            return self.list_schema.actions['POST']
        elif name == 'modify':
            return self.detail_schema.actions['PATCH']
        elif name == 'get':
            return self.detail_schema.actions['GET']
        raise Exception('could not find schema for commands {}'.format(name))

    @cached_property
    def detail_schema(self):
        try:
            return importlib.import_module(
                'awork.schema.{}.{}.{}.detail'.format(
                    self.version, self.api_version, self.resource
                )
            )
        except ImportError:
            raise Exception('{} may not allow user modification.'.format(
                self.resource))

    @cached_property
    def list_schema(self):
        try:
            return importlib.import_module('awork.schema.{}.{}.{}.list'.format(
                self.version, self.api_version, self.resource
            ))
        except ImportError:
            raise Exception('{} is not known to be an AWX resource.'.format(
                self.resource))

    @property
    def endpoint(self):
        return self.list_schema.endpoint

    def list(self, *args, **kwargs):
        return client.get(self.endpoint).json()

    def create(self, *args, **kwargs):
        print ' create '
        print ' root command:           awork (of course)'
        print ' resource category name: ' + str(self.resource)
        print ''
        print ' call args: ' + str(args)
        print ' call kwargs: ' + str(kwargs)

    def modify(self, *args, **kwargs):
        print ' modify'
        print ' root command:           awork (of course)'
        print ' resource category name: ' + str(self.resource)
        print ''
        print ' call args: ' + str(args)
        print ' call kwargs: ' + str(kwargs)

    def delete(self, *args, **kwargs):
        print ' modify'
        print ' root command:           awork (of course)'
        print ' resource category name: ' + str(self.resource)
        print ''
        print ' call args: ' + str(args)
        print ' call kwargs: ' + str(kwargs)

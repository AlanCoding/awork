from awork.utils.functional import cached_property

import importlib


class Resource:

    def __init__(self, resource):
        self.resource = resource
        # TODO: move these into settings
        self.version = 'current'
        self.api_version = 'v2'

    @cached_property
    def schema(self):
        try:
            return importlib.import_module('awork.schema.{}.{}.{}'.format(
                self.version, self.api_version, self.resource
            ))
        except ImportError:
            raise Exception('{} is not known to be an AWX resource.'.format(
                self.resource))

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

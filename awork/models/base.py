from awork.schema import current
from awork.conf import settings
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
            raise Exception('{} is not known to be an AWX resource.'.format(self.resource))



import click

from awork.cli.action import ActionSubcommand
from awork.utils.functional import cached_property
from awork.models.base import Resource


class ResSubcommand(click.MultiCommand):
    """
    Resource-level routing multi-command, example:
        awork job_template
    This command will list all of the actions possible with that resource
    """
    def __init__(self, name):
        self.resource_name = name
        super(ResSubcommand, self).__init__()

    @cached_property
    def resource(self):
        return Resource(self.resource_name)

    def list_commands(self, ctx):
        return self.resource.list_commands()

    def get_command(self, ctx, name):
        return ActionSubcommand(self.resource, name)


import click

from awork.cli.action import ActionSubcommand
from awork.utils.functional import cached_property
from awork.utils.grammar import action_names
from awork.models.base import Resource


class ResSubcommand(click.MultiCommand):
    """A subcommand that implements all command methods on the
    Resource.
    """
    def __init__(self, name):
        self.resource_name = name
        super(ResSubcommand, self).__init__()

    @cached_property
    def resource(self):
        return Resource(self.resource_name)

    def list_commands(self, ctx):
        cmds = []
        print ' listing commands '
        for html_verb in self.resource.schema.actions.keys():
            cmds.append(action_names[html_verb])
        return cmds

    def get_command(self, ctx, name):
        return ActionSubcommand(self.resource_name, name)

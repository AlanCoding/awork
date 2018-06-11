import sys
import importlib

import click

from awork.cli.resource import ResSubcommand
from awork.cli import misc
from awork.utils import secho


class RootCommand(click.MultiCommand):

    def list_commands(self, ctx):
        cmds = list(misc.__all__)
        cmds += importlib.import_module(
            'awork.schema.current.v2'
        ).resource_list
        return cmds

    def get_command(self, ctx, name):
        if name in misc.__all__:
            return getattr(misc, name)
        elif name != 'none':
            return ResSubcommand(name)

        secho('No such command: %s.' % name, fg='red', bold=True)
        sys.exit(2)

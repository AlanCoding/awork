import click

from awork.cli.resource import ResSubcommand

from awork.cli import misc


class RootCommand(click.MultiCommand):

    def list_commands(self, ctx):
        return misc.__all__

    def get_command(self, ctx, name):
        return ResSubcommand(name)

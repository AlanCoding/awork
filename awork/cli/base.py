import click

from awork.cli.resource import ResSubcommand


class RootCommand(click.MultiCommand):
    def get_command(self, ctx, name):
        return ResSubcommand(name)

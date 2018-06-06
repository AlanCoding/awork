
import click


class ResSubcommand(click.MultiCommand):
    """A subcommand that implements all command methods on the
    Resource.
    """
    def __init__(self, name):
        self.awork_name = name
        super(ResSubcommand, self).__init__()

    def get_command(self, ctx, name):

        def callback(*args, **kwargs):
            print ' root command:           awork (of course)'
            print ' resource category name: ' + str(self.awork_name)
            print ' action name:            ' + str(name)
            print ''
            print ' call args: ' + str(args)
            print ' call kwargs: ' + str(kwargs)

        params = [
            click.core.Argument(['pk'], 'pk', type=int),
            click.core.Option(['-b', '--baz'], 'baz', type=unicode)
        ]

        cmd = click.core.Command('foo', callback=callback, params=params)

        return cmd

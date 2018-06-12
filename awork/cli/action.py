
import click

# TODO: route this stuff through the formatting code
import json


class ActionSubcommand(click.core.Command):
    """
    The final command in the chain (not a multi-command) invoked by
        awork resource action --option val --option2 val2
    for example:
        awork job_template create --playbook foo.yml --inventory bar
    """

    def __init__(self, resource, action_name):
        self.resource = resource
        self.action_name = action_name
        super(ActionSubcommand, self).__init__(
            action_name,
            callback=self.perform_action
        )

    def get_params(self, ctx):
        rv = super(ActionSubcommand, self).get_params(ctx)  # --help option
        rv.append(
            click.core.Argument(
                param_decls=['pk'], required=False, type=int
            )
        )
        options = self.resource.schema_for_command(self.action_name)
        for name, element in options.items():
            help = element.get('help_text')
            rv.append(
                click.core.Option(
                    ['--{}'.format(name)], type=unicode, help=help
                )
            )
        return rv

    def perform_action(self, *args, **kwargs):
        method = getattr(self.resource, self.action_name)
        r = method(*args, **kwargs)
        click.echo(json.dumps(r, indent=4))
        return r

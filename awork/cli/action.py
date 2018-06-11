
import click

from awork.utils.functional import cached_property
from awork.utils.grammar import method_names
from awork.models.base import Resource


class ActionSubcommand(click.core.Command):

    def __init__(self, resource_name, action_name):
        self.resource_name = resource_name
        self.action_name = action_name
        super(ActionSubcommand, self).__init__(
            action_name,
            callback=self.perform_action
        )

    @cached_property
    def resource(self):
        return Resource(self.resource_name)

    def get_params(self, ctx):
        rv = super(ActionSubcommand, self).get_params(ctx)  # --help option
        rv.append(
            click.core.Argument(
                param_decls=['pk'], required=False, type=int
            )
        )
        options = self.resource.schema.actions[
            method_names()[self.action_name]
        ]
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
        return method(*args, **kwargs)

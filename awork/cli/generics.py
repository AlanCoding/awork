
import click

from awork.conf import _apply_runtime_setting


__all__ = ['CommandWithGlobals']


class SettingOption(click.core.Option):
    '''
    Option class for CLI options that set Awork settings values
    for example, the target host or username to use.
    '''

    def __init__(self, *args, **attrs):
        # No runtime settings are required, because could be in file settings
        attrs.setdefault('required', False)
        # Callback setting adds the given value to runtime settings parser
        attrs.setdefault('callback', _apply_runtime_setting)
        # The callback must be processed before other parameters
        # because the settings may affect resolution of other flags
        attrs.setdefault('is_eager', True)
        # Do not pass the value into the command, only defining settings hers
        attrs.setdefault('expose_value', False)

        super(SettingOption, self).__init__(*args, **attrs)


global_params = [
    SettingOption(
        ['-h', '--tower-host'],
        help='The location of the Ansible Tower host. '
             'HTTPS is assumed as the protocol unless "http://" is explicitly '
             'provided. This will take precedence over a host provided to '
             '`tower config`, if any.',
    ),
    SettingOption(
        ['-u', '--tower-username'],
        help='Username to use to authenticate to Ansible Tower. '
             'This will take precedence over a username provided to '
             '`tower config`, if any.',
    ),
    SettingOption(
        ['-p', '--tower-password'],
        help='Password to use to authenticate to Ansible Tower. '
             'This will take precedence over a password provided to '
             '`tower config`, if any.',
    ),

    # Create a global verbose/debug option.
    SettingOption(
        ['-f', '--format'],
        help='Output format. The "human" format is intended for humans '
             'reading output on the CLI; the "json" and "yaml" formats '
             'provide more data, and "id" echos the object id only.',
        type=click.Choice(['human', 'json', 'yaml', 'id']),
    ),
    SettingOption(
        ['-v', '--verbose'],
        default=None,
        help='Show information about requests being made.',
        is_flag=True,
    ),
    SettingOption(
        ['--description-on'],
        default=None,
        help='Show description in human-formatted output.',
        is_flag=True,
    ),

    # Create a global SSL warning option.
    SettingOption(
        ['--insecure'],
        default=None,
        help='Turn off insecure connection warnings. Set config verify_ssl '
             'to make this permanent.',
        is_flag=True,
    ),

    # Create a custom certificate specification option.
    SettingOption(
        ['--certificate'],
        default=None,
        help='Path to a custom certificate file that will be used throughout'
             ' the command. Overwritten by --insecure flag if set.',
    ),
    SettingOption(
        ['--use-token'],
        default=None,
        help='Turn on Tower\'s token-based authentication. Set config'
             ' use_token to make this permanent.',
        is_flag=True,
    ),
]


class CommandWithGlobals(click.core.Command):
    '''
    Class that comes with the global parameters automatically applied
    '''
    def get_params(self, ctx):
        rv = super(CommandWithGlobals, self).get_params(ctx)
        # TODO: idea is to create new internal "Field" class for all
        # settings, which can be used accross all use cases, including
        # this one
        rv += global_params
        return rv

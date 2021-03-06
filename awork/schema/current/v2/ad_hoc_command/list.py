endpoint = u'ad_hoc_commands'
name = u'Ad Hoc Command List'
related_search_fields = [u'schedule__search',
                         u'modified_by__search',
                         u'notifications__search',
                         u'inventory__search',
                         u'unified_job_template__search',
                         u'unified_job_node__search',
                         u'unifiedjob_ptr__search',
                         u'instance_group__search',
                         u'hosts__search',
                         u'credentials__search',
                         u'ad_hoc_command_events__search',
                         u'credential__search',
                         u'dependent_jobs__search',
                         u'launch_config__search',
                         u'job_origin__search',
                         u'created_by__search',
                         u'labels__search']
parses = [u'application/json']
search_fields = [u'description', u'name']
actions = {u'GET': {u'become_enabled': {u'filterable': True,
                                        u'label': u'Become enabled',
                                        u'type': u'boolean'},
                    u'controller_node': {u'filterable': True,
                                         u'help_text': u'The instance that managed the isolated execution environment.',
                                         u'label': u'Controller node',
                                         u'type': u'string'},
                    u'created': {u'filterable': True,
                                 u'help_text': u'Timestamp when this ad hoc command was created.',
                                 u'label': u'Created',
                                 u'type': u'datetime'},
                    u'credential': {u'filterable': True,
                                    u'label': u'Credential',
                                    u'type': u'field'},
                    u'diff_mode': {u'filterable': True,
                                   u'label': u'Diff mode',
                                   u'type': u'boolean'},
                    u'elapsed': {u'filterable': True,
                                 u'help_text': u'Elapsed time in seconds that the job ran.',
                                 u'label': u'Elapsed',
                                 u'type': u'decimal'},
                    u'execution_node': {u'filterable': True,
                                        u'help_text': u'The node the job executed on.',
                                        u'label': u'Execution node',
                                        u'type': u'string'},
                    u'extra_vars': {u'filterable': True,
                                    u'label': u'Extra vars',
                                    u'type': u'string'},
                    u'failed': {u'filterable': True,
                                u'label': u'Failed',
                                u'type': u'boolean'},
                    u'finished': {u'filterable': True,
                                  u'help_text': u'The date and time the job finished execution.',
                                  u'label': u'Finished',
                                  u'type': u'datetime'},
                    u'forks': {u'filterable': True,
                               u'label': u'Forks',
                               u'max_value': 2147483647,
                               u'min_value': 0,
                               u'type': u'integer'},
                    u'id': {u'filterable': True,
                            u'help_text': u'Database ID for this ad hoc command.',
                            u'label': u'ID',
                            u'type': u'integer'},
                    u'inventory': {u'filterable': True,
                                   u'label': u'Inventory',
                                   u'type': u'field'},
                    u'job_explanation': {u'filterable': True,
                                         u'help_text': u"A status field to indicate the state of the job if it wasn't able to run and capture stdout",
                                         u'label': u'Job explanation',
                                         u'type': u'string'},
                    u'job_type': {u'choices': [[u'run', u'Run'], [u'check', u'Check']],
                                  u'filterable': True,
                                  u'label': u'Job type',
                                  u'type': u'choice'},
                    u'launch_type': {u'choices': [[u'manual', u'Manual'],
                                                  [u'relaunch', u'Relaunch'],
                                                  [u'callback', u'Callback'],
                                                  [u'scheduled', u'Scheduled'],
                                                  [u'dependency', u'Dependency'],
                                                  [u'workflow', u'Workflow'],
                                                  [u'sync', u'Sync'],
                                                  [u'scm', u'SCM Update']],
                                     u'filterable': True,
                                     u'label': u'Launch type',
                                     u'type': u'choice'},
                    u'limit': {u'filterable': True,
                               u'label': u'Limit',
                               u'type': u'string'},
                    u'modified': {u'filterable': True,
                                  u'help_text': u'Timestamp when this ad hoc command was last modified.',
                                  u'label': u'Modified',
                                  u'type': u'datetime'},
                    u'module_args': {u'filterable': True,
                                     u'label': u'Module args',
                                     u'type': u'string'},
                    u'module_name': {u'choices': [[u'command', u'command'],
                                                  [u'shell', u'shell'],
                                                  [u'yum', u'yum'],
                                                  [u'apt', u'apt'],
                                                  [u'apt_key', u'apt_key'],
                                                  [u'apt_repository',
                                                      u'apt_repository'],
                                                  [u'apt_rpm', u'apt_rpm'],
                                                  [u'service', u'service'],
                                                  [u'group', u'group'],
                                                  [u'user', u'user'],
                                                  [u'mount', u'mount'],
                                                  [u'ping', u'ping'],
                                                  [u'selinux', u'selinux'],
                                                  [u'setup', u'setup'],
                                                  [u'win_ping', u'win_ping'],
                                                  [u'win_service', u'win_service'],
                                                  [u'win_updates', u'win_updates'],
                                                  [u'win_group', u'win_group'],
                                                  [u'win_user', u'win_user']],
                                     u'filterable': True,
                                     u'label': u'Module name',
                                     u'type': u'choice'},
                    u'name': {u'filterable': True,
                              u'help_text': u'Name of this ad hoc command.',
                              u'label': u'Name',
                              u'type': u'string'},
                    u'related': {u'help_text': u'Data structure with URLs of related resources.',
                                 u'label': u'Related',
                                 u'type': u'object'},
                    u'started': {u'filterable': True,
                                 u'help_text': u'The date and time the job was queued for starting.',
                                 u'label': u'Started',
                                 u'type': u'datetime'},
                    u'status': {u'choices': [[u'new', u'New'],
                                             [u'pending', u'Pending'],
                                             [u'waiting', u'Waiting'],
                                             [u'running', u'Running'],
                                             [u'successful', u'Successful'],
                                             [u'failed', u'Failed'],
                                             [u'error', u'Error'],
                                             [u'canceled', u'Canceled']],
                                u'filterable': True,
                                u'label': u'Status',
                                u'type': u'choice'},
                    u'summary_fields': {u'help_text': u'Data structure with name/description for related resources.',
                                        u'label': u'Summary fields',
                                        u'type': u'object'},
                    u'type': {u'choices': [[u'ad_hoc_command', u'Command']],
                              u'help_text': u'Data type for this ad hoc command.',
                              u'label': u'Type',
                              u'type': u'choice'},
                    u'url': {u'help_text': u'URL for this ad hoc command.',
                             u'label': u'Url',
                             u'type': u'string'},
                    u'verbosity': {u'choices': [[0, u'0 (Normal)'],
                                                [1, u'1 (Verbose)'],
                                                [2, u'2 (More Verbose)'],
                                                [3, u'3 (Debug)'],
                                                [4, u'4 (Connection Debug)'],
                                                [5, u'5 (WinRM Debug)']],
                                   u'filterable': True,
                                   u'label': u'Verbosity',
                                   u'type': u'choice'}},
           u'POST': {u'become_enabled': {u'default': False,
                                         u'filterable': True,
                                         u'label': u'Become enabled',
                                         u'required': False,
                                         u'type': u'boolean'},
                     u'credential': {u'filterable': True,
                                     u'label': u'Credential',
                                     u'required': False,
                                     u'type': u'field'},
                     u'diff_mode': {u'default': False,
                                    u'filterable': True,
                                    u'label': u'Diff mode',
                                    u'required': False,
                                    u'type': u'boolean'},
                     u'extra_vars': {u'default': u'',
                                     u'filterable': True,
                                     u'label': u'Extra vars',
                                     u'required': False,
                                     u'type': u'string'},
                     u'forks': {u'default': 0,
                                u'filterable': True,
                                u'label': u'Forks',
                                u'max_value': 2147483647,
                                u'min_value': 0,
                                u'required': False,
                                u'type': u'integer'},
                     u'inventory': {u'filterable': True,
                                    u'label': u'Inventory',
                                    u'required': False,
                                    u'type': u'field'},
                     u'job_type': {u'choices': [[u'run', u'Run'], [u'check', u'Check']],
                                   u'default': u'run',
                                   u'filterable': True,
                                   u'label': u'Job type',
                                   u'required': False,
                                   u'type': u'choice'},
                     u'limit': {u'default': u'',
                                u'filterable': True,
                                u'label': u'Limit',
                                u'max_length': 1024,
                                u'required': False,
                                u'type': u'string'},
                     u'module_args': {u'default': u'',
                                      u'filterable': True,
                                      u'label': u'Module args',
                                      u'required': False,
                                      u'type': u'string'},
                     u'module_name': {u'choices': [[u'command', u'command'],
                                                   [u'shell', u'shell'],
                                                   [u'yum', u'yum'],
                                                   [u'apt', u'apt'],
                                                   [u'apt_key', u'apt_key'],
                                                   [u'apt_repository',
                                                    u'apt_repository'],
                                                   [u'apt_rpm', u'apt_rpm'],
                                                   [u'service', u'service'],
                                                   [u'group', u'group'],
                                                   [u'user', u'user'],
                                                   [u'mount', u'mount'],
                                                   [u'ping', u'ping'],
                                                   [u'selinux', u'selinux'],
                                                   [u'setup', u'setup'],
                                                   [u'win_ping', u'win_ping'],
                                                   [u'win_service', u'win_service'],
                                                   [u'win_updates', u'win_updates'],
                                                   [u'win_group', u'win_group'],
                                                   [u'win_user', u'win_user']],
                                      u'default': u'command',
                                      u'filterable': True,
                                      u'label': u'Module name',
                                      u'required': False,
                                      u'type': u'choice'},
                     u'verbosity': {u'choices': [[0, u'0 (Normal)'],
                                                 [1, u'1 (Verbose)'],
                                                 [2, u'2 (More Verbose)'],
                                                 [3, u'3 (Debug)'],
                                                 [4, u'4 (Connection Debug)'],
                                                 [5, u'5 (WinRM Debug)']],
                                    u'default': 0,
                                    u'filterable': True,
                                    u'label': u'Verbosity',
                                    u'required': False,
                                    u'type': u'choice'}}}
renders = [u'application/json', u'text/html']
max_page_size = 200
types = [u'ad_hoc_command']

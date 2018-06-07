endpoint = "jobs"
name = u'Job List'
related_search_fields = [u'schedule__search',
                         u'modified_by__search',
                         u'job_events__search',
                         u'project__search',
                         u'inventory__search',
                         u'credentials__search',
                         u'unified_job_template__search',
                         u'job_host_summaries__search',
                         u'unifiedjob_ptr__search',
                         u'instance_group__search',
                         u'labels__search',
                         u'hosts__search',
                         u'notifications__search',
                         u'project_update__search',
                         u'unified_job_node__search',
                         u'dependent_jobs__search',
                         u'launch_config__search',
                         u'job_origin__search',
                         u'created_by__search',
                         u'job_template__search']
parses = [u'application/json']
search_fields = [u'description', u'name']
actions = {u'GET': {u'allow_simultaneous': {u'filterable': True,
                                            u'label': u'Allow simultaneous',
                                            u'type': u'boolean'},
                    u'artifacts': {u'filterable': True,
                                   u'label': u'Artifacts',
                                   u'type': u'field'},
                    u'ask_credential_on_launch': {u'label': u'Ask credential on launch',
                                                  u'type': u'field'},
                    u'ask_diff_mode_on_launch': {u'label': u'Ask diff mode on launch',
                                                 u'type': u'field'},
                    u'ask_inventory_on_launch': {u'label': u'Ask inventory on launch',
                                                 u'type': u'field'},
                    u'ask_job_type_on_launch': {u'label': u'Ask job type on launch',
                                                u'type': u'field'},
                    u'ask_limit_on_launch': {u'label': u'Ask limit on launch',
                                             u'type': u'field'},
                    u'ask_skip_tags_on_launch': {u'label': u'Ask skip tags on launch',
                                                 u'type': u'field'},
                    u'ask_tags_on_launch': {u'label': u'Ask tags on launch',
                                            u'type': u'field'},
                    u'ask_variables_on_launch': {u'label': u'Ask variables on launch',
                                                 u'type': u'field'},
                    u'ask_verbosity_on_launch': {u'label': u'Ask verbosity on launch',
                                                 u'type': u'field'},
                    u'controller_node': {u'filterable': True,
                                         u'help_text': u'The instance that managed the isolated execution environment.',
                                         u'label': u'Controller node',
                                         u'type': u'string'},
                    u'created': {u'filterable': True,
                                 u'help_text': u'Timestamp when this job was created.',
                                 u'label': u'Created',
                                 u'type': u'datetime'},
                    u'credential': {u'help_text': u'This resource has been deprecated and will be removed in a future release',
                                    u'label': u'Credential',
                                    u'min_value': 1,
                                    u'type': u'integer'},
                    u'description': {u'filterable': True,
                                     u'help_text': u'Optional description of this job.',
                                     u'label': u'Description',
                                     u'type': u'string'},
                    u'diff_mode': {u'filterable': True,
                                   u'help_text': u'If enabled, textual changes made to any templated files on the host are shown in the standard output',
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
                    u'force_handlers': {u'filterable': True,
                                        u'label': u'Force handlers',
                                        u'type': u'boolean'},
                    u'forks': {u'filterable': True,
                               u'label': u'Forks',
                               u'max_value': 2147483647,
                               u'min_value': 0,
                               u'type': u'integer'},
                    u'id': {u'filterable': True,
                            u'help_text': u'Database ID for this job.',
                            u'label': u'ID',
                            u'type': u'integer'},
                    u'instance_group': {u'filterable': True,
                                        u'help_text': u'The Rampart/Instance group the job was run under',
                                        u'label': u'Instance group',
                                        u'type': u'field'},
                    u'inventory': {u'filterable': True,
                                   u'label': u'Inventory',
                                   u'type': u'field'},
                    u'job_explanation': {u'filterable': True,
                                         u'help_text': u"A status field to indicate the state of the job if it wasn't able to run and capture stdout",
                                         u'label': u'Job explanation',
                                         u'type': u'string'},
                    u'job_tags': {u'filterable': True,
                                  u'label': u'Job tags',
                                  u'type': u'string'},
                    u'job_template': {u'filterable': True,
                                      u'label': u'Job template',
                                      u'type': u'field'},
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
                                  u'help_text': u'Timestamp when this job was last modified.',
                                  u'label': u'Modified',
                                  u'type': u'datetime'},
                    u'name': {u'filterable': True,
                              u'help_text': u'Name of this job.',
                              u'label': u'Name',
                              u'type': u'string'},
                    u'passwords_needed_to_start': {u'label': u'Passwords needed to start',
                                                   u'type': u'field'},
                    u'playbook': {u'filterable': True,
                                  u'label': u'Playbook',
                                  u'type': u'string'},
                    u'project': {u'filterable': True,
                                 u'label': u'Project',
                                 u'type': u'field'},
                    u'related': {u'help_text': u'Data structure with URLs of related resources.',
                                 u'label': u'Related',
                                 u'type': u'object'},
                    u'scm_revision': {u'filterable': True,
                                      u'help_text': u'The SCM Revision from the Project used for this job, if available',
                                      u'label': u'SCM Revision',
                                      u'type': u'string'},
                    u'skip_tags': {u'filterable': True,
                                   u'label': u'Skip tags',
                                   u'type': u'string'},
                    u'start_at_task': {u'filterable': True,
                                       u'label': u'Start at task',
                                       u'type': u'string'},
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
                    u'timeout': {u'filterable': True,
                                 u'help_text': u'The amount of time (in seconds) to run before the task is canceled.',
                                 u'label': u'Timeout',
                                 u'max_value': 2147483647,
                                 u'min_value': -2147483648,
                                 u'type': u'integer'},
                    u'type': {u'choices': [[u'job', u'Playbook Run']],
                              u'help_text': u'Data type for this job.',
                              u'label': u'Type',
                              u'type': u'choice'},
                    u'unified_job_template': {u'filterable': True,
                                              u'label': u'unified job template',
                                              u'type': u'field'},
                    u'url': {u'help_text': u'URL for this job.',
                             u'label': u'Url',
                             u'type': u'string'},
                    u'use_fact_cache': {u'filterable': True,
                                        u'help_text': u'If enabled, Tower will act as an Ansible Fact Cache Plugin; persisting facts at the end of a playbook run to the database and caching facts for use by Ansible.',
                                        u'label': u'Use fact cache',
                                        u'type': u'boolean'},
                    u'vault_credential': {u'help_text': u'This resource has been deprecated and will be removed in a future release',
                                          u'label': u'Vault credential',
                                          u'min_value': 1,
                                          u'type': u'integer'},
                    u'verbosity': {u'choices': [[0, u'0 (Normal)'],
                                                [1, u'1 (Verbose)'],
                                                [2, u'2 (More Verbose)'],
                                                [3, u'3 (Debug)'],
                                                [4, u'4 (Connection Debug)'],
                                                [5, u'5 (WinRM Debug)']],
                                   u'filterable': True,
                                   u'label': u'Verbosity',
                                   u'type': u'choice'}}}
renders = [u'application/json', u'text/html']
max_page_size = 200
types = [u'job']

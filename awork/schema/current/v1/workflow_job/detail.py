endpoint = u'workflow_jobs'
name = u'Workflow Job Detail'
parses = [u'application/json']
actions = {u'GET': {u'allow_simultaneous': {u'filterable': True,
                                            u'label': u'Allow simultaneous',
                                            u'type': u'boolean'},
                    u'created': {u'filterable': True,
                                 u'help_text': u'Timestamp when this workflow job was created.',
                                 u'label': u'Created',
                                 u'type': u'datetime'},
                    u'description': {u'filterable': True,
                                     u'help_text': u'Optional description of this workflow job.',
                                     u'label': u'Description',
                                     u'type': u'string'},
                    u'elapsed': {u'filterable': True,
                                 u'help_text': u'Elapsed time in seconds that the job ran.',
                                 u'label': u'Elapsed',
                                 u'type': u'decimal'},
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
                    u'id': {u'filterable': True,
                            u'help_text': u'Database ID for this workflow job.',
                            u'label': u'ID',
                            u'type': u'integer'},
                    u'job_args': {u'filterable': True,
                                  u'label': u'Job args',
                                  u'type': u'string'},
                    u'job_cwd': {u'filterable': True,
                                 u'label': u'Job cwd',
                                 u'type': u'string'},
                    u'job_env': {u'filterable': True,
                                 u'label': u'job_env',
                                 u'type': u'field'},
                    u'job_explanation': {u'filterable': True,
                                         u'help_text': u"A status field to indicate the state of the job if it wasn't able to run and capture stdout",
                                         u'label': u'Job explanation',
                                         u'type': u'string'},
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
                    u'modified': {u'filterable': True,
                                  u'help_text': u'Timestamp when this workflow job was last modified.',
                                  u'label': u'Modified',
                                  u'type': u'datetime'},
                    u'name': {u'filterable': True,
                              u'help_text': u'Name of this workflow job.',
                              u'label': u'Name',
                              u'type': u'string'},
                    u'related': {u'help_text': u'Data structure with URLs of related resources.',
                                 u'label': u'Related',
                                 u'type': u'object'},
                    u'result_traceback': {u'filterable': True,
                                          u'label': u'Result traceback',
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
                    u'type': {u'choices': [[u'workflow_job', u'Workflow Job']],
                              u'help_text': u'Data type for this workflow job.',
                              u'label': u'Type',
                              u'type': u'choice'},
                    u'unified_job_template': {u'filterable': True,
                                              u'label': u'unified job template',
                                              u'type': u'field'},
                    u'url': {u'help_text': u'URL for this workflow job.',
                             u'label': u'Url',
                             u'type': u'string'},
                    u'workflow_job_template': {u'filterable': True,
                                               u'label': u'Workflow job template',
                                               u'type': u'field'}}}
renders = [u'application/json', u'text/html']
types = [u'workflow_job']

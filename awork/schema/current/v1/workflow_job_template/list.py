endpoint = u'workflow_job_templates'
name = u'Workflow Job Template List'
related_search_fields = [u'instance_groups__search',
                         u'modified_by__search',
                         u'workflowjobnodes__search',
                         u'schedules__search',
                         u'last_job__search',
                         u'credentials__search',
                         u'workflow_job_template_nodes__search',
                         u'notification_templates_any__search',
                         u'labels__search',
                         u'notification_templates_error__search',
                         u'unifiedjob_unified_jobs__search',
                         u'notification_templates_success__search',
                         u'next_schedule__search',
                         u'current_job__search',
                         u'workflowjobtemplatenodes__search',
                         u'created_by__search',
                         u'workflow_jobs__search',
                         u'unifiedjobtemplate_ptr__search',
                         u'organization__search']
parses = [u'application/json']
search_fields = [u'description', u'name']
actions = {u'GET': {u'allow_simultaneous': {u'filterable': True,
                                            u'label': u'Allow simultaneous',
                                            u'type': u'boolean'},
                    u'ask_variables_on_launch': {u'filterable': True,
                                                 u'label': u'Ask variables on launch',
                                                 u'type': u'boolean'},
                    u'created': {u'filterable': True,
                                 u'help_text': u'Timestamp when this workflow job template was created.',
                                 u'label': u'Created',
                                 u'type': u'datetime'},
                    u'description': {u'filterable': True,
                                     u'help_text': u'Optional description of this workflow job template.',
                                     u'label': u'Description',
                                     u'type': u'string'},
                    u'extra_vars': {u'filterable': True,
                                    u'label': u'Extra vars',
                                    u'type': u'string'},
                    u'id': {u'filterable': True,
                            u'help_text': u'Database ID for this workflow job template.',
                            u'label': u'ID',
                            u'type': u'integer'},
                    u'last_job_failed': {u'filterable': True,
                                         u'label': u'Last job failed',
                                         u'type': u'boolean'},
                    u'last_job_run': {u'filterable': True,
                                      u'label': u'Last job run',
                                      u'type': u'datetime'},
                    u'modified': {u'filterable': True,
                                  u'help_text': u'Timestamp when this workflow job template was last modified.',
                                  u'label': u'Modified',
                                  u'type': u'datetime'},
                    u'name': {u'filterable': True,
                              u'help_text': u'Name of this workflow job template.',
                              u'label': u'Name',
                              u'type': u'string'},
                    u'next_job_run': {u'filterable': True,
                                      u'label': u'Next job run',
                                      u'type': u'datetime'},
                    u'organization': {u'filterable': True,
                                      u'label': u'Organization',
                                      u'type': u'field'},
                    u'related': {u'help_text': u'Data structure with URLs of related resources.',
                                 u'label': u'Related',
                                 u'type': u'object'},
                    u'status': {u'choices': [[u'new', u'New'],
                                             [u'pending', u'Pending'],
                                             [u'waiting', u'Waiting'],
                                             [u'running', u'Running'],
                                             [u'successful', u'Successful'],
                                             [u'failed', u'Failed'],
                                             [u'error', u'Error'],
                                             [u'canceled', u'Canceled'],
                                             [u'never updated', u'Never Updated'],
                                             [u'ok', u'OK'],
                                             [u'missing', u'Missing'],
                                             [u'none', u'No External Source'],
                                             [u'updating', u'Updating']],
                                u'filterable': True,
                                u'label': u'Status',
                                u'type': u'choice'},
                    u'summary_fields': {u'help_text': u'Data structure with name/description for related resources.',
                                        u'label': u'Summary fields',
                                        u'type': u'object'},
                    u'survey_enabled': {u'filterable': True,
                                        u'label': u'Survey enabled',
                                        u'type': u'boolean'},
                    u'type': {u'choices': [[u'workflow_job_template',
                                            u'Workflow Template']],
                              u'help_text': u'Data type for this workflow job template.',
                              u'label': u'Type',
                              u'type': u'choice'},
                    u'url': {u'help_text': u'URL for this workflow job template.',
                             u'label': u'Url',
                             u'type': u'string'}},
           u'POST': {u'allow_simultaneous': {u'default': False,
                                             u'filterable': True,
                                             u'label': u'Allow simultaneous',
                                             u'required': False,
                                             u'type': u'boolean'},
                     u'ask_variables_on_launch': {u'default': False,
                                                  u'filterable': True,
                                                  u'label': u'Ask variables on launch',
                                                  u'required': False,
                                                  u'type': u'boolean'},
                     u'description': {u'default': u'',
                                      u'filterable': True,
                                      u'help_text': u'Optional description of this workflow job template.',
                                      u'label': u'Description',
                                      u'required': False,
                                      u'type': u'string'},
                     u'extra_vars': {u'default': u'',
                                     u'filterable': True,
                                     u'label': u'Extra vars',
                                     u'required': False,
                                     u'type': u'string'},
                     u'name': {u'filterable': True,
                               u'help_text': u'Name of this workflow job template.',
                               u'label': u'Name',
                               u'max_length': 512,
                               u'required': True,
                               u'type': u'string'},
                     u'organization': {u'filterable': True,
                                       u'label': u'Organization',
                                       u'required': False,
                                       u'type': u'field'},
                     u'survey_enabled': {u'default': False,
                                         u'filterable': True,
                                         u'label': u'Survey enabled',
                                         u'required': False,
                                         u'type': u'boolean'}}}
renders = [u'application/json', u'text/html']
max_page_size = 200
types = [u'workflow_job_template']

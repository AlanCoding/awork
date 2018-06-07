endpoint = "job_events"
name = u'Job Event List'
related_search_fields = [u'host__search',
                         u'parent__search',
                         u'hosts__search',
                         u'children__search',
                         u'job__search']
parses = [u'application/json']
search_fields = [u'stdout']
actions = {u'GET': {u'changed': {u'filterable': True,
                                 u'label': u'Changed',
                                 u'type': u'boolean'},
                    u'counter': {u'filterable': True,
                                 u'label': u'Counter',
                                 u'min_value': 0,
                                 u'type': u'integer'},
                    u'created': {u'filterable': True,
                                 u'help_text': u'Timestamp when this job event was created.',
                                 u'label': u'Created',
                                 u'type': u'datetime'},
                    u'end_line': {u'filterable': True,
                                  u'label': u'End line',
                                  u'min_value': 0,
                                  u'type': u'integer'},
                    u'event': {u'choices': [[u'runner_on_failed', u'Host Failed'],
                                            [u'runner_on_ok', u'Host OK'],
                                            [u'runner_on_error', u'Host Failure'],
                                            [u'runner_on_skipped',
                                                u'Host Skipped'],
                                            [u'runner_on_unreachable',
                                             u'Host Unreachable'],
                                            [u'runner_on_no_hosts',
                                             u'No Hosts Remaining'],
                                            [u'runner_on_async_poll',
                                                u'Host Polling'],
                                            [u'runner_on_async_ok',
                                                u'Host Async OK'],
                                            [u'runner_on_async_failed',
                                             u'Host Async Failure'],
                                            [u'runner_item_on_ok', u'Item OK'],
                                            [u'runner_item_on_failed',
                                                u'Item Failed'],
                                            [u'runner_item_on_skipped',
                                                u'Item Skipped'],
                                            [u'runner_retry', u'Host Retry'],
                                            [u'runner_on_file_diff',
                                                u'File Difference'],
                                            [u'playbook_on_start',
                                                u'Playbook Started'],
                                            [u'playbook_on_notify',
                                                u'Running Handlers'],
                                            [u'playbook_on_include',
                                                u'Including File'],
                                            [u'playbook_on_no_hosts_matched',
                                             u'No Hosts Matched'],
                                            [u'playbook_on_no_hosts_remaining',
                                             u'No Hosts Remaining'],
                                            [u'playbook_on_task_start',
                                                u'Task Started'],
                                            [u'playbook_on_vars_prompt',
                                             u'Variables Prompted'],
                                            [u'playbook_on_setup',
                                                u'Gathering Facts'],
                                            [u'playbook_on_import_for_host',
                                             u'internal: on Import for Host'],
                                            [u'playbook_on_not_import_for_host',
                                             u'internal: on Not Import for Host'],
                                            [u'playbook_on_play_start',
                                                u'Play Started'],
                                            [u'playbook_on_stats',
                                                u'Playbook Complete'],
                                            [u'debug', u'Debug'],
                                            [u'verbose', u'Verbose'],
                                            [u'deprecated', u'Deprecated'],
                                            [u'warning', u'Warning'],
                                            [u'system_warning', u'System Warning'],
                                            [u'error', u'Error']],
                               u'filterable': True,
                               u'label': u'Event',
                               u'type': u'choice'},
                    u'event_data': {u'filterable': True,
                                    u'label': u'Event data',
                                    u'type': u'field'},
                    u'event_display': {u'label': u'Event display', u'type': u'string'},
                    u'event_level': {u'label': u'Event level', u'type': u'integer'},
                    u'failed': {u'filterable': True,
                                u'label': u'Failed',
                                u'type': u'boolean'},
                    u'host': {u'filterable': True, u'label': u'Host', u'type': u'field'},
                    u'host_name': {u'filterable': True,
                                   u'label': u'Host name',
                                   u'type': u'string'},
                    u'id': {u'filterable': True,
                            u'help_text': u'Database ID for this job event.',
                            u'label': u'ID',
                            u'type': u'integer'},
                    u'job': {u'filterable': True, u'label': u'Job', u'type': u'field'},
                    u'modified': {u'filterable': True,
                                  u'help_text': u'Timestamp when this job event was last modified.',
                                  u'label': u'Modified',
                                  u'type': u'datetime'},
                    u'parent': {u'filterable': True,
                                u'label': u'Parent',
                                u'type': u'field'},
                    u'parent_uuid': {u'filterable': True,
                                     u'label': u'Parent uuid',
                                     u'type': u'string'},
                    u'play': {u'filterable': True, u'label': u'Play', u'type': u'string'},
                    u'playbook': {u'filterable': True,
                                  u'label': u'Playbook',
                                  u'type': u'string'},
                    u'related': {u'help_text': u'Data structure with URLs of related resources.',
                                 u'label': u'Related',
                                 u'type': u'object'},
                    u'role': {u'filterable': True, u'label': u'Role', u'type': u'string'},
                    u'start_line': {u'filterable': True,
                                    u'label': u'Start line',
                                    u'min_value': 0,
                                    u'type': u'integer'},
                    u'stdout': {u'filterable': True,
                                u'label': u'Stdout',
                                u'type': u'string'},
                    u'summary_fields': {u'help_text': u'Data structure with name/description for related resources.',
                                        u'label': u'Summary fields',
                                        u'type': u'object'},
                    u'task': {u'filterable': True, u'label': u'Task', u'type': u'string'},
                    u'type': {u'choices': [[u'job_event', u'Job Event']],
                              u'help_text': u'Data type for this job event.',
                              u'label': u'Type',
                              u'type': u'choice'},
                    u'url': {u'help_text': u'URL for this job event.',
                             u'label': u'Url',
                             u'type': u'string'},
                    u'uuid': {u'filterable': True, u'label': u'Uuid', u'type': u'string'},
                    u'verbosity': {u'filterable': True,
                                   u'label': u'Verbosity',
                                   u'min_value': 0,
                                   u'type': u'integer'}}}
renders = [u'application/json', u'text/html']
max_page_size = 200
types = [u'job_event']

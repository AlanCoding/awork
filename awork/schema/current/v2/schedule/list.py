endpoint = u'schedules'
name = u'Schedules'
related_search_fields = [u'unified_job_template__search',
                         u'modified_by__search',
                         u'credentials__search',
                         u'created_by__search',
                         u'inventory__search']
parses = [u'application/json']
search_fields = [u'description', u'name']
actions = {u'GET': {u'created': {u'filterable': True,
                                 u'help_text': u'Timestamp when this schedule was created.',
                                 u'label': u'Created',
                                 u'type': u'datetime'},
                    u'description': {u'filterable': True,
                                     u'help_text': u'Optional description of this schedule.',
                                     u'label': u'Description',
                                     u'type': u'string'},
                    u'diff_mode': {u'label': u'Diff mode', u'type': u'boolean'},
                    u'dtend': {u'filterable': True,
                               u'help_text': u'The last occurrence of the schedule occurs before this time, aftewards the schedule expires.',
                               u'label': u'Dtend',
                               u'type': u'datetime'},
                    u'dtstart': {u'filterable': True,
                                 u'help_text': u'The first occurrence of the schedule occurs on or after this time.',
                                 u'label': u'Dtstart',
                                 u'type': u'datetime'},
                    u'enabled': {u'filterable': True,
                                 u'help_text': u'Enables processing of this schedule.',
                                 u'label': u'Enabled',
                                 u'type': u'boolean'},
                    u'extra_data': {u'filterable': True,
                                    u'label': u'Extra data',
                                    u'type': u'field'},
                    u'id': {u'filterable': True,
                            u'help_text': u'Database ID for this schedule.',
                            u'label': u'ID',
                            u'type': u'integer'},
                    u'inventory': {u'filterable': True,
                                   u'label': u'Inventory',
                                   u'type': u'field'},
                    u'job_tags': {u'label': u'Job tags', u'type': u'string'},
                    u'job_type': {u'choices': [[u'run', u'Run'], [u'check', u'Check']],
                                  u'label': u'Job type',
                                  u'type': u'choice'},
                    u'limit': {u'label': u'Limit', u'type': u'string'},
                    u'modified': {u'filterable': True,
                                  u'help_text': u'Timestamp when this schedule was last modified.',
                                  u'label': u'Modified',
                                  u'type': u'datetime'},
                    u'name': {u'filterable': True,
                              u'help_text': u'Name of this schedule.',
                              u'label': u'Name',
                              u'type': u'string'},
                    u'next_run': {u'filterable': True,
                                  u'help_text': u'The next time that the scheduled action will run.',
                                  u'label': u'Next run',
                                  u'type': u'datetime'},
                    u'related': {u'help_text': u'Data structure with URLs of related resources.',
                                 u'label': u'Related',
                                 u'type': u'object'},
                    u'rrule': {u'filterable': True,
                               u'help_text': u'A value representing the schedules iCal recurrence rule.',
                               u'label': u'Rrule',
                               u'type': u'string'},
                    u'skip_tags': {u'label': u'Skip tags', u'type': u'string'},
                    u'summary_fields': {u'help_text': u'Data structure with name/description for related resources.',
                                        u'label': u'Summary fields',
                                        u'type': u'object'},
                    u'timezone': {u'label': u'Timezone', u'type': u'field'},
                    u'type': {u'choices': [[u'schedule', u'Schedule']],
                              u'help_text': u'Data type for this schedule.',
                              u'label': u'Type',
                              u'type': u'choice'},
                    u'unified_job_template': {u'filterable': True,
                                              u'label': u'Unified job template',
                                              u'type': u'field'},
                    u'until': {u'label': u'Until', u'type': u'field'},
                    u'url': {u'help_text': u'URL for this schedule.',
                             u'label': u'Url',
                             u'type': u'string'},
                    u'verbosity': {u'choices': [[0, u'0 (Normal)'],
                                                [1, u'1 (Verbose)'],
                                                [2, u'2 (More Verbose)'],
                                                [3, u'3 (Debug)'],
                                                [4, u'4 (Connection Debug)'],
                                                [5, u'5 (WinRM Debug)']],
                                   u'label': u'Verbosity',
                                   u'type': u'choice'}}}
renders = [u'application/json', u'text/html']
max_page_size = 200
types = [u'schedule']

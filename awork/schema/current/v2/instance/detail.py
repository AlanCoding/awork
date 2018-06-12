endpoint = u'instances'
name = u'Instance Detail'
parses = [u'application/json']
actions = {u'GET': {u'capacity': {u'filterable': True,
                                  u'label': u'Capacity',
                                  u'min_value': 0,
                                  u'type': u'integer'},
                    u'capacity_adjustment': {u'filterable': True,
                                             u'label': u'Capacity adjustment',
                                             u'type': u'decimal'},
                    u'consumed_capacity': {u'label': u'Consumed capacity',
                                           u'type': u'field'},
                    u'cpu': {u'filterable': True, u'label': u'Cpu', u'type': u'integer'},
                    u'cpu_capacity': {u'filterable': True,
                                      u'label': u'Cpu capacity',
                                      u'type': u'integer'},
                    u'created': {u'filterable': True,
                                 u'help_text': u'Timestamp when this instance was created.',
                                 u'label': u'Created',
                                 u'type': u'datetime'},
                    u'enabled': {u'filterable': True,
                                 u'label': u'Enabled',
                                 u'type': u'boolean'},
                    u'hostname': {u'filterable': True,
                                  u'label': u'Hostname',
                                  u'type': u'string'},
                    u'id': {u'filterable': True,
                            u'help_text': u'Database ID for this instance.',
                            u'label': u'ID',
                            u'type': u'integer'},
                    u'jobs_running': {u'help_text': u'Count of jobs in the running or waiting state that are targeted for this instance',
                                      u'label': u'Jobs running',
                                      u'type': u'integer'},
                    u'jobs_total': {u'help_text': u'Count of all jobs that target this instance',
                                    u'label': u'Jobs total',
                                    u'type': u'integer'},
                    u'mem_capacity': {u'filterable': True,
                                      u'label': u'Mem capacity',
                                      u'type': u'integer'},
                    u'memory': {u'filterable': True,
                                u'label': u'Memory',
                                u'type': u'integer'},
                    u'modified': {u'filterable': True,
                                  u'help_text': u'Timestamp when this instance was last modified.',
                                  u'label': u'Modified',
                                  u'type': u'datetime'},
                    u'percent_capacity_remaining': {u'label': u'Percent capacity remaining',
                                                    u'type': u'field'},
                    u'related': {u'help_text': u'Data structure with URLs of related resources.',
                                 u'label': u'Related',
                                 u'type': u'object'},
                    u'type': {u'choices': [[u'instance', u'Instance']],
                              u'help_text': u'Data type for this instance.',
                              u'label': u'Type',
                              u'type': u'choice'},
                    u'url': {u'help_text': u'URL for this instance.',
                             u'label': u'Url',
                             u'type': u'string'},
                    u'uuid': {u'filterable': True, u'label': u'Uuid', u'type': u'string'},
                    u'version': {u'filterable': True,
                                 u'label': u'Version',
                                 u'type': u'string'}}}
renders = [u'application/json', u'text/html']
types = [u'instance']

endpoint = u'instance_groups'
name = u'Instance Groups'
related_search_fields = [u'controller__search',
                         u'controlled_groups__search', u'instances__search']
parses = [u'application/json']
search_fields = [u'name']
actions = {u'GET': {u'capacity': {u'label': u'Capacity', u'type': u'field'},
                    u'committed_capacity': {u'label': u'Committed capacity',
                                            u'type': u'field'},
                    u'consumed_capacity': {u'label': u'Consumed capacity',
                                           u'type': u'field'},
                    u'controller': {u'filterable': True,
                                    u'help_text': u'Instance Group to remotely control this group.',
                                    u'label': u'Controller',
                                    u'type': u'field'},
                    u'created': {u'filterable': True,
                                 u'help_text': u'Timestamp when this instance group was created.',
                                 u'label': u'Created',
                                 u'type': u'datetime'},
                    u'id': {u'filterable': True,
                            u'help_text': u'Database ID for this instance group.',
                            u'label': u'ID',
                            u'type': u'integer'},
                    u'instances': {u'label': u'Instances', u'type': u'field'},
                    u'jobs_running': {u'help_text': u'Count of jobs in the running or waiting state that are targeted for this instance group',
                                      u'label': u'Jobs running',
                                      u'type': u'integer'},
                    u'jobs_total': {u'help_text': u'Count of all jobs that target this instance group',
                                    u'label': u'Jobs total',
                                    u'type': u'integer'},
                    u'modified': {u'filterable': True,
                                  u'help_text': u'Timestamp when this instance group was last modified.',
                                  u'label': u'Modified',
                                  u'type': u'datetime'},
                    u'name': {u'filterable': True,
                              u'help_text': u'Name of this instance group.',
                              u'label': u'Name',
                              u'type': u'string'},
                    u'percent_capacity_remaining': {u'label': u'Percent capacity remaining',
                                                    u'type': u'field'},
                    u'policy_instance_list': {u'child': {u'type': u'string'},
                                              u'filterable': True,
                                              u'help_text': u'List of exact-match Instances that will be assigned to this group',
                                              u'label': u'Policy Instance List',
                                              u'type': u'list'},
                    u'policy_instance_minimum': {u'filterable': True,
                                                 u'help_text': u'Static minimum number of Instances that will be automatically assign to this group when new instances come online.',
                                                 u'label': u'Policy Instance Minimum',
                                                 u'min_value': 0,
                                                 u'type': u'integer'},
                    u'policy_instance_percentage': {u'filterable': True,
                                                    u'help_text': u'Minimum percentage of all instances that will be automatically assigned to this group when new instances come online.',
                                                    u'label': u'Policy Instance Percentage',
                                                    u'max_value': 100,
                                                    u'min_value': 0,
                                                    u'type': u'integer'},
                    u'related': {u'help_text': u'Data structure with URLs of related resources.',
                                 u'label': u'Related',
                                 u'type': u'object'},
                    u'type': {u'choices': [[u'instance_group', u'Instance Group']],
                              u'help_text': u'Data type for this instance group.',
                              u'label': u'Type',
                              u'type': u'choice'},
                    u'url': {u'help_text': u'URL for this instance group.',
                             u'label': u'Url',
                             u'type': u'string'}},
           u'POST': {u'name': {u'filterable': True,
                               u'help_text': u'Name of this instance group.',
                               u'label': u'Name',
                               u'max_length': 250,
                               u'required': True,
                               u'type': u'string'},
                     u'policy_instance_list': {u'child': {u'read_only': False,
                                                          u'required': True,
                                                          u'type': u'string'},
                                               u'filterable': True,
                                               u'help_text': u'List of exact-match Instances that will be assigned to this group',
                                               u'label': u'Policy Instance List',
                                               u'required': False,
                                               u'type': u'list'},
                     u'policy_instance_minimum': {u'default': 0,
                                                  u'filterable': True,
                                                  u'help_text': u'Static minimum number of Instances that will be automatically assign to this group when new instances come online.',
                                                  u'label': u'Policy Instance Minimum',
                                                  u'min_value': 0,
                                                  u'required': False,
                                                  u'type': u'integer'},
                     u'policy_instance_percentage': {u'default': 0,
                                                     u'filterable': True,
                                                     u'help_text': u'Minimum percentage of all instances that will be automatically assigned to this group when new instances come online.',
                                                     u'label': u'Policy Instance Percentage',
                                                     u'max_value': 100,
                                                     u'min_value': 0,
                                                     u'required': False,
                                                     u'type': u'integer'}}}
renders = [u'application/json', u'text/html']
max_page_size = 200
types = [u'instance_group']

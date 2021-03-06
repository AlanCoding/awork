endpoint = u'credentials'
name = u'Credential Detail'
parses = [u'application/json']
actions = {u'GET': {u'created': {u'filterable': True,
                                 u'help_text': u'Timestamp when this credential was created.',
                                 u'label': u'Created',
                                 u'type': u'datetime'},
                    u'credential_type': {u'filterable': True,
                                         u'help_text': u'Specify the type of credential you want to create. Refer to the Ansible Tower documentation for details on each type.',
                                         u'label': u'Credential type',
                                         u'type': u'field'},
                    u'description': {u'filterable': True,
                                     u'help_text': u'Optional description of this credential.',
                                     u'label': u'Description',
                                     u'type': u'string'},
                    u'id': {u'filterable': True,
                            u'help_text': u'Database ID for this credential.',
                            u'label': u'ID',
                            u'type': u'integer'},
                    u'inputs': {u'filterable': True,
                                u'help_text': u'Enter inputs using either JSON or YAML syntax. Use the radio button to toggle between the two. Refer to the Ansible Tower documentation for example syntax.',
                                u'label': u'Inputs',
                                u'type': u'field'},
                    u'modified': {u'filterable': True,
                                  u'help_text': u'Timestamp when this credential was last modified.',
                                  u'label': u'Modified',
                                  u'type': u'datetime'},
                    u'name': {u'filterable': True,
                              u'help_text': u'Name of this credential.',
                              u'label': u'Name',
                              u'type': u'string'},
                    u'organization': {u'filterable': True,
                                      u'label': u'Organization',
                                      u'type': u'field'},
                    u'related': {u'help_text': u'Data structure with URLs of related resources.',
                                 u'label': u'Related',
                                 u'type': u'object'},
                    u'summary_fields': {u'help_text': u'Data structure with name/description for related resources.',
                                        u'label': u'Summary fields',
                                        u'type': u'object'},
                    u'type': {u'choices': [[u'credential', u'Credential']],
                              u'help_text': u'Data type for this credential.',
                              u'label': u'Type',
                              u'type': u'choice'},
                    u'url': {u'help_text': u'URL for this credential.',
                             u'label': u'Url',
                             u'type': u'string'}},
           u'PUT': {u'credential_type': {u'filterable': True,
                                         u'help_text': u'Specify the type of credential you want to create. Refer to the Ansible Tower documentation for details on each type.',
                                         u'label': u'Credential type',
                                         u'required': True,
                                         u'type': u'field'},
                    u'description': {u'default': u'',
                                     u'filterable': True,
                                     u'help_text': u'Optional description of this credential.',
                                     u'label': u'Description',
                                     u'required': False,
                                     u'type': u'string'},
                    u'inputs': {u'default': {},
                                u'filterable': True,
                                u'help_text': u'Enter inputs using either JSON or YAML syntax. Use the radio button to toggle between the two. Refer to the Ansible Tower documentation for example syntax.',
                                u'label': u'Inputs',
                                u'required': False,
                                u'type': u'field'},
                    u'name': {u'filterable': True,
                              u'help_text': u'Name of this credential.',
                              u'label': u'Name',
                              u'max_length': 512,
                              u'required': True,
                              u'type': u'string'},
                    u'organization': {u'filterable': True,
                                      u'label': u'Organization',
                                      u'required': False,
                                      u'type': u'field'}}}
renders = [u'application/json', u'text/html']
types = [u'credential']

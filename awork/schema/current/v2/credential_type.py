endpoint = "credential_types"
name = u'Credential Type List'
related_search_fields = [u'modified_by__search',
                         u'credentials__search', u'created_by__search']
parses = [u'application/json']
search_fields = [u'description', u'name']
actions = {u'GET': {u'created': {u'filterable': True,
                                 u'help_text': u'Timestamp when this credential type was created.',
                                 u'label': u'Created',
                                 u'type': u'datetime'},
                    u'description': {u'filterable': True,
                                     u'help_text': u'Optional description of this credential type.',
                                     u'label': u'Description',
                                     u'type': u'string'},
                    u'id': {u'filterable': True,
                            u'help_text': u'Database ID for this credential type.',
                            u'label': u'ID',
                            u'type': u'integer'},
                    u'injectors': {u'filterable': True,
                                   u'help_text': u'Enter injectors using either JSON or YAML syntax. Use the radio button to toggle between the two. Refer to the Ansible Tower documentation for example syntax.',
                                   u'label': u'Injectors',
                                   u'type': u'field'},
                    u'inputs': {u'filterable': True,
                                u'help_text': u'Enter inputs using either JSON or YAML syntax. Use the radio button to toggle between the two. Refer to the Ansible Tower documentation for example syntax.',
                                u'label': u'Inputs',
                                u'type': u'field'},
                    u'kind': {u'choices': [[u'ssh', u'Machine'],
                                           [u'vault', u'Vault'],
                                           [u'net', u'Network'],
                                           [u'scm', u'Source Control'],
                                           [u'cloud', u'Cloud'],
                                           [u'insights', u'Insights']],
                              u'filterable': True,
                              u'label': u'Kind',
                              u'type': u'choice'},
                    u'managed_by_tower': {u'filterable': True,
                                          u'label': u'Managed by tower',
                                          u'type': u'field'},
                    u'modified': {u'filterable': True,
                                  u'help_text': u'Timestamp when this credential type was last modified.',
                                  u'label': u'Modified',
                                  u'type': u'datetime'},
                    u'name': {u'filterable': True,
                              u'help_text': u'Name of this credential type.',
                              u'label': u'Name',
                              u'type': u'string'},
                    u'related': {u'help_text': u'Data structure with URLs of related resources.',
                                 u'label': u'Related',
                                 u'type': u'object'},
                    u'summary_fields': {u'help_text': u'Data structure with name/description for related resources.',
                                        u'label': u'Summary fields',
                                        u'type': u'object'},
                    u'type': {u'choices': [[u'credential_type', u'Credential Type']],
                              u'help_text': u'Data type for this credential type.',
                              u'label': u'Type',
                              u'type': u'choice'},
                    u'url': {u'help_text': u'URL for this credential type.',
                             u'label': u'Url',
                             u'type': u'string'}},
           u'POST': {u'description': {u'default': u'',
                                      u'filterable': True,
                                      u'help_text': u'Optional description of this credential type.',
                                      u'label': u'Description',
                                      u'required': False,
                                      u'type': u'string'},
                     u'injectors': {u'default': {},
                                    u'filterable': True,
                                    u'help_text': u'Enter injectors using either JSON or YAML syntax. Use the radio button to toggle between the two. Refer to the Ansible Tower documentation for example syntax.',
                                    u'label': u'Injectors',
                                    u'required': False,
                                    u'type': u'field'},
                     u'inputs': {u'default': {},
                                 u'filterable': True,
                                 u'help_text': u'Enter inputs using either JSON or YAML syntax. Use the radio button to toggle between the two. Refer to the Ansible Tower documentation for example syntax.',
                                 u'label': u'Inputs',
                                 u'required': False,
                                 u'type': u'field'},
                     u'kind': {u'choices': [[u'net', u'Network'], [u'cloud', u'Cloud']],
                               u'filterable': True,
                               u'label': u'Kind',
                               u'required': True,
                               u'type': u'choice'},
                     u'name': {u'filterable': True,
                               u'help_text': u'Name of this credential type.',
                               u'label': u'Name',
                               u'max_length': 512,
                               u'required': True,
                               u'type': u'string'}}}
renders = [u'application/json', u'text/html']
max_page_size = 200
types = [u'credential_type']

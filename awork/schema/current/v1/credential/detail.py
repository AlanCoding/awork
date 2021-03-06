endpoint = u'credentials'
name = u'Credential Detail'
parses = [u'application/json']
actions = {u'GET': {u'authorize': {u'help_text': u'Whether to use the authorize mechanism.',
                                   u'label': u'Authorize',
                                   u'type': u'boolean'},
                    u'authorize_password': {u'help_text': u'Password used by the authorize mechanism.',
                                            u'label': u'Authorize password',
                                            u'type': u'string'},
                    u'become_method': {u'choices': [[u'', u'None'],
                                                    [u'sudo', u'Sudo'],
                                                    [u'su', u'Su'],
                                                    [u'pbrun', u'Pbrun'],
                                                    [u'pfexec', u'Pfexec'],
                                                    [u'dzdo', u'DZDO'],
                                                    [u'pmrun', u'Pmrun'],
                                                    [u'runas', u'Runas'],
                                                    [u'enable', u'Enable'],
                                                    [u'doas', u'Doas']],
                                       u'help_text': u'Privilege escalation method.',
                                       u'label': u'Become method',
                                       u'type': u'choice'},
                    u'become_password': {u'help_text': u'Password for privilege escalation method.',
                                         u'label': u'Become password',
                                         u'type': u'string'},
                    u'become_username': {u'help_text': u'Privilege escalation username.',
                                         u'label': u'Become username',
                                         u'type': u'string'},
                    u'client': {u'help_text': u'Client Id or Application Id for the credential',
                                u'label': u'Client',
                                u'type': u'string'},
                    u'cloud': {u'label': u'Cloud', u'type': u'boolean'},
                    u'created': {u'filterable': True,
                                 u'help_text': u'Timestamp when this credential was created.',
                                 u'label': u'Created',
                                 u'type': u'datetime'},
                    u'description': {u'filterable': True,
                                     u'help_text': u'Optional description of this credential.',
                                     u'label': u'Description',
                                     u'type': u'string'},
                    u'domain': {u'help_text': u'The identifier for the domain.',
                                u'label': u'Domain',
                                u'type': u'string'},
                    u'host': {u'help_text': u'The hostname or IP address to use.',
                              u'label': u'Host',
                              u'type': u'string'},
                    u'id': {u'filterable': True,
                            u'help_text': u'Database ID for this credential.',
                            u'label': u'ID',
                            u'type': u'integer'},
                    u'kind': {u'choices': [[u'ssh', u'Machine'],
                                           [u'net', u'Network'],
                                           [u'scm', u'Source Control'],
                                           [u'aws', u'Amazon Web Services'],
                                           [u'vmware', u'VMware vCenter'],
                                           [u'satellite6', u'Red Hat Satellite 6'],
                                           [u'cloudforms', u'Red Hat CloudForms'],
                                           [u'gce', u'Google Compute Engine'],
                                           [u'azure_rm',
                                            u'Microsoft Azure Resource Manager'],
                                           [u'openstack', u'OpenStack'],
                                           [u'rhv', u'Red Hat Virtualization'],
                                           [u'insights', u'Insights'],
                                           [u'tower', u'Ansible Tower']],
                              u'label': u'Kind',
                              u'type': u'choice'},
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
                    u'password': {u'help_text': u'Password for this credential (or "ASK" to prompt the user for machine credentials).',
                                  u'label': u'Password',
                                  u'type': u'string'},
                    u'project': {u'help_text': u'The identifier for the project.',
                                 u'label': u'Project',
                                 u'type': u'string'},
                    u'related': {u'help_text': u'Data structure with URLs of related resources.',
                                 u'label': u'Related',
                                 u'type': u'object'},
                    u'secret': {u'help_text': u'Secret Token for this credential',
                                u'label': u'Secret',
                                u'type': u'string'},
                    u'security_token': {u'help_text': u'Security Token for this credential',
                                        u'label': u'Security Token',
                                        u'type': u'string'},
                    u'ssh_key_data': {u'help_text': u'RSA or DSA private key to be used instead of password.',
                                      u'label': u'SSH private key',
                                      u'type': u'string'},
                    u'ssh_key_unlock': {u'help_text': u'Passphrase to unlock SSH private key if encrypted (or "ASK" to prompt the user for machine credentials).',
                                        u'label': u'SSH key unlock',
                                        u'type': u'string'},
                    u'subscription': {u'help_text': u'Subscription identifier for this credential',
                                      u'label': u'Subscription',
                                      u'type': u'string'},
                    u'summary_fields': {u'help_text': u'Data structure with name/description for related resources.',
                                        u'label': u'Summary fields',
                                        u'type': u'object'},
                    u'tenant': {u'help_text': u'Tenant identifier for this credential',
                                u'label': u'Tenant',
                                u'type': u'string'},
                    u'type': {u'choices': [[u'credential', u'Credential']],
                              u'help_text': u'Data type for this credential.',
                              u'label': u'Type',
                              u'type': u'choice'},
                    u'url': {u'help_text': u'URL for this credential.',
                             u'label': u'Url',
                             u'type': u'string'},
                    u'username': {u'help_text': u'Username for this credential.',
                                  u'label': u'Username',
                                  u'type': u'string'},
                    u'vault_password': {u'help_text': u'Vault password (or "ASK" to prompt the user).',
                                        u'label': u'Vault password',
                                        u'type': u'string'}},
           u'PUT': {u'authorize': {u'default': False,
                                   u'help_text': u'Whether to use the authorize mechanism.',
                                   u'label': u'Authorize',
                                   u'required': False,
                                   u'type': u'boolean'},
                    u'authorize_password': {u'default': u'',
                                            u'help_text': u'Password used by the authorize mechanism.',
                                            u'label': u'Authorize password',
                                            u'max_length': 1024,
                                            u'required': False,
                                            u'type': u'string'},
                    u'become_method': {u'choices': [[u'', u'None'],
                                                    [u'sudo', u'Sudo'],
                                                    [u'su', u'Su'],
                                                    [u'pbrun', u'Pbrun'],
                                                    [u'pfexec', u'Pfexec'],
                                                    [u'dzdo', u'DZDO'],
                                                    [u'pmrun', u'Pmrun'],
                                                    [u'runas', u'Runas'],
                                                    [u'enable', u'Enable'],
                                                    [u'doas', u'Doas']],
                                       u'default': u'',
                                       u'help_text': u'Privilege escalation method.',
                                       u'label': u'Become method',
                                       u'required': False,
                                       u'type': u'choice'},
                    u'become_password': {u'default': u'',
                                         u'help_text': u'Password for privilege escalation method.',
                                         u'label': u'Become password',
                                         u'max_length': 1024,
                                         u'required': False,
                                         u'type': u'string'},
                    u'become_username': {u'default': u'',
                                         u'help_text': u'Privilege escalation username.',
                                         u'label': u'Become username',
                                         u'max_length': 1024,
                                         u'required': False,
                                         u'type': u'string'},
                    u'client': {u'default': u'',
                                u'help_text': u'Client Id or Application Id for the credential',
                                u'label': u'Client',
                                u'max_length': 128,
                                u'required': False,
                                u'type': u'string'},
                    u'description': {u'default': u'',
                                     u'filterable': True,
                                     u'help_text': u'Optional description of this credential.',
                                     u'label': u'Description',
                                     u'required': False,
                                     u'type': u'string'},
                    u'domain': {u'default': u'',
                                u'help_text': u'The identifier for the domain.',
                                u'label': u'Domain',
                                u'max_length': 100,
                                u'required': False,
                                u'type': u'string'},
                    u'host': {u'default': u'',
                              u'help_text': u'The hostname or IP address to use.',
                              u'label': u'Host',
                              u'max_length': 1024,
                              u'required': False,
                              u'type': u'string'},
                    u'kind': {u'choices': [[u'ssh', u'Machine'],
                                           [u'net', u'Network'],
                                           [u'scm', u'Source Control'],
                                           [u'aws', u'Amazon Web Services'],
                                           [u'vmware', u'VMware vCenter'],
                                           [u'satellite6', u'Red Hat Satellite 6'],
                                           [u'cloudforms', u'Red Hat CloudForms'],
                                           [u'gce', u'Google Compute Engine'],
                                           [u'azure_rm',
                                            u'Microsoft Azure Resource Manager'],
                                           [u'openstack', u'OpenStack'],
                                           [u'rhv', u'Red Hat Virtualization'],
                                           [u'insights', u'Insights'],
                                           [u'tower', u'Ansible Tower']],
                              u'default': u'ssh',
                              u'label': u'Kind',
                              u'required': False,
                              u'type': u'choice'},
                    u'name': {u'filterable': True,
                              u'help_text': u'Name of this credential.',
                              u'label': u'Name',
                              u'max_length': 512,
                              u'required': True,
                              u'type': u'string'},
                    u'organization': {u'filterable': True,
                                      u'label': u'Organization',
                                      u'required': False,
                                      u'type': u'field'},
                    u'password': {u'default': u'',
                                  u'help_text': u'Password for this credential (or "ASK" to prompt the user for machine credentials).',
                                  u'label': u'Password',
                                  u'max_length': 1024,
                                  u'required': False,
                                  u'type': u'string'},
                    u'project': {u'default': u'',
                                 u'help_text': u'The identifier for the project.',
                                 u'label': u'Project',
                                 u'max_length': 100,
                                 u'required': False,
                                 u'type': u'string'},
                    u'secret': {u'default': u'',
                                u'help_text': u'Secret Token for this credential',
                                u'label': u'Secret',
                                u'max_length': 1024,
                                u'required': False,
                                u'type': u'string'},
                    u'security_token': {u'default': u'',
                                        u'help_text': u'Security Token for this credential',
                                        u'label': u'Security Token',
                                        u'max_length': 1024,
                                        u'required': False,
                                        u'type': u'string'},
                    u'ssh_key_data': {u'default': u'',
                                      u'help_text': u'RSA or DSA private key to be used instead of password.',
                                      u'label': u'SSH private key',
                                      u'required': False,
                                      u'type': u'string'},
                    u'ssh_key_unlock': {u'default': u'',
                                        u'help_text': u'Passphrase to unlock SSH private key if encrypted (or "ASK" to prompt the user for machine credentials).',
                                        u'label': u'SSH key unlock',
                                        u'max_length': 1024,
                                        u'required': False,
                                        u'type': u'string'},
                    u'subscription': {u'default': u'',
                                      u'help_text': u'Subscription identifier for this credential',
                                      u'label': u'Subscription',
                                      u'max_length': 1024,
                                      u'required': False,
                                      u'type': u'string'},
                    u'tenant': {u'default': u'',
                                u'help_text': u'Tenant identifier for this credential',
                                u'label': u'Tenant',
                                u'max_length': 1024,
                                u'required': False,
                                u'type': u'string'},
                    u'username': {u'default': u'',
                                  u'help_text': u'Username for this credential.',
                                  u'label': u'Username',
                                  u'max_length': 1024,
                                  u'required': False,
                                  u'type': u'string'},
                    u'vault_password': {u'default': u'',
                                        u'help_text': u'Vault password (or "ASK" to prompt the user).',
                                        u'label': u'Vault password',
                                        u'max_length': 1024,
                                        u'required': False,
                                        u'type': u'string'}}}
renders = [u'application/json', u'text/html']
types = [u'credential']

endpoint = u'inventory_scripts'
name = u'Inventory Script Detail'
parses = [u'application/json']
actions = {u'GET': {u'created': {u'filterable': True,
                                 u'help_text': u'Timestamp when this custom inventory script was created.',
                                 u'label': u'Created',
                                 u'type': u'datetime'},
                    u'description': {u'filterable': True,
                                     u'help_text': u'Optional description of this custom inventory script.',
                                     u'label': u'Description',
                                     u'type': u'string'},
                    u'id': {u'filterable': True,
                            u'help_text': u'Database ID for this custom inventory script.',
                            u'label': u'ID',
                            u'type': u'integer'},
                    u'modified': {u'filterable': True,
                                  u'help_text': u'Timestamp when this custom inventory script was last modified.',
                                  u'label': u'Modified',
                                  u'type': u'datetime'},
                    u'name': {u'filterable': True,
                              u'help_text': u'Name of this custom inventory script.',
                              u'label': u'Name',
                              u'type': u'string'},
                    u'organization': {u'filterable': True,
                                      u'help_text': u'Organization owning this inventory script',
                                      u'label': u'Organization',
                                      u'type': u'field'},
                    u'related': {u'help_text': u'Data structure with URLs of related resources.',
                                 u'label': u'Related',
                                 u'type': u'object'},
                    u'script': {u'filterable': True,
                                u'label': u'Script',
                                u'type': u'string'},
                    u'summary_fields': {u'help_text': u'Data structure with name/description for related resources.',
                                        u'label': u'Summary fields',
                                        u'type': u'object'},
                    u'type': {u'choices': [[u'custom_inventory_script',
                                            u'Custom Inventory Script']],
                              u'help_text': u'Data type for this custom inventory script.',
                              u'label': u'Type',
                              u'type': u'choice'},
                    u'url': {u'help_text': u'URL for this custom inventory script.',
                             u'label': u'Url',
                             u'type': u'string'}},
           u'PUT': {u'description': {u'default': u'',
                                     u'filterable': True,
                                     u'help_text': u'Optional description of this custom inventory script.',
                                     u'label': u'Description',
                                     u'required': False,
                                     u'type': u'string'},
                    u'name': {u'filterable': True,
                              u'help_text': u'Name of this custom inventory script.',
                              u'label': u'Name',
                              u'max_length': 512,
                              u'required': True,
                              u'type': u'string'},
                    u'organization': {u'filterable': True,
                                      u'help_text': u'Organization owning this inventory script',
                                      u'label': u'Organization',
                                      u'required': True,
                                      u'type': u'field'},
                    u'script': {u'filterable': True,
                                u'label': u'Script',
                                u'required': True,
                                u'type': u'string'}}}
renders = [u'application/json', u'text/html']
types = [u'custom_inventory_script']

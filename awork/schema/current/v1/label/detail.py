endpoint = u'labels'
name = u'Label Detail'
parses = [u'application/json']
actions = {u'GET': {u'created': {u'filterable': True,
                                 u'help_text': u'Timestamp when this label was created.',
                                 u'label': u'Created',
                                 u'type': u'datetime'},
                    u'id': {u'filterable': True,
                            u'help_text': u'Database ID for this label.',
                            u'label': u'ID',
                            u'type': u'integer'},
                    u'modified': {u'filterable': True,
                                  u'help_text': u'Timestamp when this label was last modified.',
                                  u'label': u'Modified',
                                  u'type': u'datetime'},
                    u'name': {u'filterable': True,
                              u'help_text': u'Name of this label.',
                              u'label': u'Name',
                              u'type': u'string'},
                    u'organization': {u'filterable': True,
                                      u'help_text': u'Organization this label belongs to.',
                                      u'label': u'Organization',
                                      u'type': u'field'},
                    u'related': {u'help_text': u'Data structure with URLs of related resources.',
                                 u'label': u'Related',
                                 u'type': u'object'},
                    u'summary_fields': {u'help_text': u'Data structure with name/description for related resources.',
                                        u'label': u'Summary fields',
                                        u'type': u'object'},
                    u'type': {u'choices': [[u'label', u'Label']],
                              u'help_text': u'Data type for this label.',
                              u'label': u'Type',
                              u'type': u'choice'},
                    u'url': {u'help_text': u'URL for this label.',
                             u'label': u'Url',
                             u'type': u'string'}},
           u'PUT': {u'name': {u'filterable': True,
                              u'help_text': u'Name of this label.',
                              u'label': u'Name',
                              u'max_length': 512,
                              u'required': True,
                              u'type': u'string'},
                    u'organization': {u'filterable': True,
                                      u'help_text': u'Organization this label belongs to.',
                                      u'label': u'Organization',
                                      u'required': True,
                                      u'type': u'field'}}}
renders = [u'application/json', u'text/html']
types = [u'label']

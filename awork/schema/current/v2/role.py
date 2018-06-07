endpoint = "roles"
name = u'Role List'
related_search_fields = [u'descendents__search',
                         u'parents__search',
                         u'children__search',
                         u'content_type__search',
                         u'ancestors__search']
parses = [u'application/json']
search_fields = [u'role_field', u'content_type__model']
actions = {u'GET': {u'description': {u'help_text': u'Optional description of this role.',
                                     u'label': u'Description',
                                     u'type': u'field'},
                    u'id': {u'filterable': True,
                            u'help_text': u'Database ID for this role.',
                            u'label': u'ID',
                            u'type': u'integer'},
                    u'name': {u'help_text': u'Name of this role.',
                              u'label': u'Name',
                              u'type': u'field'},
                    u'related': {u'help_text': u'Data structure with URLs of related resources.',
                                 u'label': u'Related',
                                 u'type': u'object'},
                    u'summary_fields': {u'help_text': u'Data structure with name/description for related resources.',
                                        u'label': u'Summary fields',
                                        u'type': u'object'},
                    u'type': {u'choices': [[u'role', u'Role']],
                              u'help_text': u'Data type for this role.',
                              u'label': u'Type',
                              u'type': u'choice'},
                    u'url': {u'help_text': u'URL for this role.',
                             u'label': u'Url',
                             u'type': u'string'}}}
renders = [u'application/json', u'text/html']
max_page_size = 200
types = [u'role']

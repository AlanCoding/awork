

action_names = {
    'GET': 'get',
    'POST': 'create',
    'PUT': 'modify',
    'PATCH': 'modify',
    'DELETE': 'delete'
}


def method_names():
    r = {}
    for k, v in action_names.items():
        r[v] = k
    return r

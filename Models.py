models = {
    'User': {
        'user_id': {'type': 'text', 'options': 'PRIMARY KEY NOT NULL UNIQUE'},
        'first_name': {'type': 'text', 'options':'NOT NULL'},
        'last_name': {'type': 'text', 'options': 'NOT NULL'},
        'phone': {'type': 'text', 'options': 'UNIQUE'}
        },

    'Restaurant': {
        'name': {'type': 'text', 'options': ''},
        'address': {'type': 'text', 'options': 'UNIQUE'},
        'category': {'type': 'text', 'options': ''},
    }
}

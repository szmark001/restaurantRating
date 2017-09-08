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
    },

    'Address': {
        'address': {'type': 'text', 'options': ''},
        'state': {'type': 'text', 'options': ''},
        'city': {'type': 'text', 'options': ''},
        'zip': {'type': 'text', 'options': ''}
    },

    'Rating': {
        'cost': {'type': 'text', 'options': 'NOT NULL'},
        'food': {'type': 'text', 'options': 'NOT NULL'},
        'cleanliness': {'type': 'text', 'options': 'NOT NULL'},
        'service': {'type': 'text', 'options': 'NOT NULL'}
    }
}

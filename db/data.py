raw_events = [
    
    { 'show': True, 'month': 10, 'day': 25, 'nameday': True,  'name': 'Someone'  },
    { 'show': True, 'month': 6,  'day': 12, 'nameday': True,  'name': 'Somebody' },

    
    { 'show': True, 'month': 5,  'day': 13, 'year': 1980, 'birthday': True, 'name': 'Someone'  },
    { 'show': True, 'month': 1,  'day': 25, 'year': 1950, 'birthday': True, 'name': 'Somebody' },

    
    { 'show': True, 'month': 5,  'day': 13, 'payment': True, 'name': 'Payment 2' },
    { 'show': True, 'month': 4,  'day': 8,  'payment': True, 'name': 'Payment 1' },
]

db_keys = ( 'show', 'birthday', 'nameday', 'payment', 'year', 'month', 'day', 'name' )

def events():
    events = [ fill_missing_keys(raw_event) for raw_event in raw_events ]
    return events

def fill_missing_keys(raw_event):
    event = {}

    for key in db_keys:
        try:
            event[key] = raw_event[key]
        except KeyError:
            event[key] = None

    return event

OK_FORMAT = True

test = {   'name': 'q2_1',
    'points': 1,
    'suites': [   {   'cases': [   {'code': ">>> latest_poverty.labels == ('geo', 'time', 'poverty_percent')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> latest_poverty.num_rows == 145\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> latest_poverty.column('poverty_percent')[0] == 43.37\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
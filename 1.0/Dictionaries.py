database = {
    'Julia': {'name': 'Julia',
             'surname': 'Anholcer',
             'birthdate': '1982-04-28',
             'occupation': 'whatever',
             'interests': ['boardgames','cooking'],
             'bank_balance': 12536.00
             },
    'Agata': {'name': 'Agata',
             'surname': 'Sobiechowska',
             'birthdate': '1990-01-01',
             'occupation': 'whatever',
             'interests': ['sailing'],
             'bank_balance': 22000.00
             }
}

database['Julia']['interests'].append('books')
database['Agata']['interests'] += ['books']

database['Krysia'] = {'name': 'Krystyna',
                      'surname': 'Piątkowska',
                      'birthdate': '1981-05-05',
                      'occupation': 'whatever',
                      'interests': ['sailing'],
                      'bank_balance': 9999.00
                      }

database['Julia']['bank_balance'] *= 2
database['Agata']['interests'] += ['diving','hiking']
database['Agata']['surname'] = 'Kowalska'

for element in database:
    database[element]['secondname'] = 'Anna'
    database[element]['age'] = 30
    database[element]['education'] = []
    del database[element]['birthdate']

database['Julia']['age'] += 5

from pprint import pprint as pp
pp(database)
#pp(database['Julia'])
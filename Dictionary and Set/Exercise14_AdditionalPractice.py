ID_PASSWORD = {'Minsung': 'abc123',
               'Ronald': 'def456',
               'Kike': 'ghi798'}

def login():
    username = input('ID: ')
    if username not in ID_PASSWORD:
        print('Can not find such user name')
    else:
        password = input('PW: ')
        if password != ID_PASSWORD[username]:
            print('wrong password')
        else:
            print('login complete')

login()
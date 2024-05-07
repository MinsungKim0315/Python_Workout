'''
split the content and save needed info in a dictionary
'''
def passwd_to_dict(filename):
    users = {}
    with open(filename) as passwd:
        for line in passwd:
            if not line.startswith(('#', '\n')):
                user_info = line.split(':')
                users[user_info[0]] = int(user_info[2])
    return users

print(passwd_to_dict('test.txt'))

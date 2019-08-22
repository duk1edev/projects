import json


# users = [
#    {
#
#        'email': 'adam111@gmail.com',
#        'username': 'Adam'
#    },
#    {
#       'username': 'John',
#        'email': 'John123@hotmail.com'
#    },
#    {
#        'username': 'Alex',
#        'email': 'alex@yandex.ru'
#    }
# ]

class User(object):
    def __init__(self, Uname, Email):
        self.username = Uname
        self.email = Email

    @staticmethod
    def to_json(self):
        return {'username': self.username, 'email': self.email}


users = list([User('vitally', 'duk1e.ptc.ua@yandesdasdasd'), User('fasts', 'dfsdf@gds@.fds')])

with open('data/example8.json', 'w') as json_file:
    json.dump(users, json_file, indent=2, default=User.to_json)

import json


class User(object):
    def __init__(self, Uname, Email):
        self.username = Uname
        self.email = Email

    def to_json(self):
        return {'username': self.username, 'email': self.email}

    @classmethod
    def from_json(cls, js_object):
        return cls(js_object['username'], js_object['email'])

    def __repr__(self):
        return 'User({!r}, {!r}).'.format(self.username, self.email)

with open('data/example8.json') as data:
    users = json.load(data,object_hook=User.from_json)

print(users)

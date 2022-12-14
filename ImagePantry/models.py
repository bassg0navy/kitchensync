from flask_login import UserMixin
from ImagePantry import (login_manager, login_user, logout_user, current_user, login_required)
from ImagePantry import db
import uuid, json
from bson import ObjectId, json_util

# MongoDB Collections
users = db['users']
photos = db['photos']
videos = db['videos']

class User():
    def __init__(self, password, name, _id):
        self.password = password
        self.name     = name
        self._id      = _id
        # self._id = id
        # self.id = uuid.uuid4().hex if not id else id

    @classmethod
    def make_from_dict(cls, d):
        # Initialize User object from a dictionary
        return cls(d['password'], d['name'], d['_id'])

    def dict(self):
        # Return dictionary representation of the object
        return {
            "id": self._id,
            "name": self.name,
            "password": self.password,
        }

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self._id)
        # return str(self.name)

@login_manager.user_loader
def load_user(get_id):
    # Return user object or none
    user = users.find_one({'_id': get_id})
    # user = users.find_one({'name': get_id})
    if user:
        return User.make_from_dict(user)
    return None
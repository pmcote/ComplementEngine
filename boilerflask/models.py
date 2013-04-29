from boilerflask import app, db # use a cache and a crypto library for users!
import datetime
import re


class User(db.Document):
    user_id = db.StringField(required=True)
    user_token = db.StringField(required=True)
    user_name = db.StringField(required=True)
# Apache 2 License

#imports
from google.appengine.ext import db

class Shout(db.Model):
  message = db.TextProperty(required=True)
  when = db.DateTimeProperty(auto_now_add=True)
  who = db.StringProperty()

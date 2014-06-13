from google.appengine.ext import ndb

class MessageRecord(ndb.Model):
    uid = ndb.IntegerProperty()
    field1 = ndb.StringProperty(indexed=False)
    field2 = ndb.StringProperty(indexed=False)
    author = ndb.StringProperty(indexed=False)
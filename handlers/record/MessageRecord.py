from google.appengine.ext import ndb

class MessageRecord(ndb.Model):
    uid = ndb.StringProperty(indexed=True)
    field1 = ndb.StringProperty(indexed=False)
    field2 = ndb.StringProperty(indexed=False)
    author = ndb.StringProperty(indexed=False)
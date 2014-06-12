import webapp2
import cgi
import json
import time

from google.appengine.ext import ndb

class MessageRecord(ndb.Model):
    uid = ndb.IntegerProperty()
    field1 = ndb.StringProperty(indexed=False)
    field2 = ndb.StringProperty(indexed=False)
    author = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

class CreateHandler(webapp2.RequestHandler):
    def get(self):
        self.response.status = '404'
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Not Found')

    def post(self):
        self.response.headers['Content-Type'] = 'application/json'
        dataStr = cgi.escape(self.request.body)
        data = json.loads(dataStr)
        data['uid'] = int(time.time() * 1000000)

        messageRecord = MessageRecord(uid=data['uid'], field1=data['field1'], field2=data['field2'], author=data['author'])
        messageRecord.put()

        self.response.write("{\"uid\": %d}" % data['uid'])

application = webapp2.WSGIApplication([
    ('/create', CreateHandler),
])

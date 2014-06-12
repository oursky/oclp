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
    # date = ndb.DateTimeProperty(auto_now_add=True)

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

class QueryHandler(webapp2.RequestHandler):
    def get(self):
        queryID = self.request.get('id')

        if not queryID:
            self.response.status = '404'
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Not Found')
            return

        query = MessageRecord.query(MessageRecord.uid == int(queryID))
        queryRecords = query.fetch(1)

        # Protection
        if len(queryRecords) == 0:
            self.response.status = '404'
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Not Found')
            return

        self.response.status = '200'
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write('{"query": %s, ' % queryID)
        self.response.write('"field1": "%s", ' % queryRecord.field1 )
        self.response.write('"field2": "%s", ' % queryRecord.field2 )
        self.response.write('"author": "%s", ' % queryRecord.author )
        self.response.write('"success": true }')

application = webapp2.WSGIApplication([
    ('/create', CreateHandler),
    ('/message', QueryHandler),
])

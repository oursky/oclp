import cgi, json, time
import webapp2

from record.MessageRecord import MessageRecord

class Handler(webapp2.RequestHandler):
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

        queryRecord = queryRecords[0]

        self.response.status = '200'
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write('{"query": %s, ' % queryID)
        self.response.write('"field1": "%s", ' % queryRecord.field1 )
        self.response.write('"field2": "%s", ' % queryRecord.field2 )
        self.response.write('"author": "%s", ' % queryRecord.author )
        
        self.response.write('"success": true }')

    def post(self):
        self.response.headers['Content-Type'] = 'application/json'
        dataStr = cgi.escape(self.request.body)
        data = json.loads(dataStr)
        data['uid'] = int(time.time() * 1000000)

        messageRecord = MessageRecord(uid=data['uid'], field1=data['field1'], field2=data['field2'], author=data['author'])
        messageRecord.put()

        self.response.write("{\"uid\": %d}" % data['uid'])

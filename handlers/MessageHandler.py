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

        queryRecord = {}
        queryRecord['field1'] = queryRecords[0].field1
        queryRecord['field2'] = queryRecords[0].field2
        queryRecord['author'] = queryRecords[0].author

        self.response.status = '200'
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(queryRecord))

    def post(self):
        self.response.headers['Content-Type'] = 'application/json'
        dataStr = cgi.escape(self.request.body)
        data = json.loads(dataStr)
        data['uid'] = int(time.time() * 1000000)

        messageRecord = MessageRecord(uid=data['uid'], field1=data['field1'], field2=data['field2'], author=data['author'])
        messageRecord.put()

        self.response.write(json.dumps({'uid': data['uid']}))


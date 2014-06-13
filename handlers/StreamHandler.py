import webapp2
import json

from record.MessageRecord import MessageRecord

class Handler(webapp2.RequestHandler):
    def get(self):
        pageNumStr = self.request.get('page')

        if not pageNumStr:
            self.response.status = '404'
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Not Found')
            return

        try:
            pageNum = int(pageNumStr)
        except ValueError:
            self.response.status = '404'
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Not Found')

        query = MessageRecord.query().order(-MessageRecord.uid)
        queryRecords = query.fetch_page(10, offset=((pageNum - 1) * 10))[0]

        recordArray = []

        for perQueryRecord in queryRecords:
            perRecord = {}
            perRecord['field1'] = perQueryRecord.field1
            perRecord['field2'] = perQueryRecord.field2
            perRecord['author'] = perQueryRecord.author
            perRecord['uid'] = perQueryRecord.uid
            recordArray.append(perRecord)

        result = {}
        result['count'] = len(recordArray)
        result['result'] = recordArray

        self.response.status = '200'
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(result))

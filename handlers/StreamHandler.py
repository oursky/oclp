import webapp2

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

        resultStr = "["

        for i in range(len(queryRecords)):
            perRecord = queryRecords[i]

            resultStr += "{"
            resultStr += "\"field1\": \"%s\", " % perRecord.field1
            resultStr += "\"field2\": \"%s\", " % perRecord.field2
            resultStr += "\"author\": \"%s\", " % perRecord.author
            resultStr += "\"uid\": %s }" % perRecord.uid

            if i != len(queryRecords) - 1:
                resultStr += ","

        resultStr += "]"

        self.response.status = '200'
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write('{"count": %d, ' % len(queryRecords))
        self.response.write('"result": %s, ' % resultStr)
        
        self.response.write('"success": true }')

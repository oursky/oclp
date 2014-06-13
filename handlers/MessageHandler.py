# -*- coding: utf-8 -*-
import cgi, json, time
import webapp2

from config import JINJA_ENVIRONMENT
from record.MessageRecord import MessageRecord

class Handler(webapp2.RequestHandler):
    def get(self):
        queryID = self.request.get('id')

        if not queryID:
            self.response.status = '404'
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Not Found')
            return

        query = MessageRecord.query(MessageRecord.uid == queryID)
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
        data['uid'] = str(int(time.time()))

        messageRecord = MessageRecord(uid=data['uid'],
            field1=data['field1'],
            field2=data['field2'],
            author=data['author'])
        messageRecord.put()

        self.response.write(json.dumps({'uid': data['uid']}))


class Share(webapp2.RequestHandler):
    def get(self, message_id):
        query = MessageRecord.query(MessageRecord.uid == message_id)
        queryRecords = query.fetch(1)

        # Protection
        if len(queryRecords) == 0:
            self.response.status = '302'
            self.response.headers['Location'] = '/'
            return

        template_values = {
            'og_url': 'http://oclp622.com/message/{mid}'.format(mid=message_id),
            'og_image': 'http://oclp622.com/social-network.png',
            'og_description': u'全城{up_for}！向{no_to}說不！ － {author}'.format(
                up_for=queryRecords[0].field1,
                no_to=queryRecords[0].field2,
                author=queryRecords[0].author
            )
        }
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render(template_values))

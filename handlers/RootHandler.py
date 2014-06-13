import webapp2

class Handler(webapp2.RequestHandler):
    def get(self):
        self.response.status = '302'
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.headers['Location'] = '/index.html'
        self.response.write('Redirecting...')

import os
import webapp2

from main import JINJA_ENVIRONMENT

class Handler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'og:url': 'http://oclp622.com',
            'og:image': 'http://oclp622.com/social-network.png'
        }
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render(template_values))

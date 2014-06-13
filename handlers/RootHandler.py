import os
import webapp2

from config import JINJA_ENVIRONMENT

class Handler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'og_url': 'http://oclp622.com',
            'og_image': 'http://oclp622.com/assets/social_network.png'
        }
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render(template_values))

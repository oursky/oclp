import os
import sys

def fix_path():
    # credit:  Nick Johnson of Google
    sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

import webapp2
import jinja2

from handlers import RootHandler, MessageHandler, StreamHandler

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

application = webapp2.WSGIApplication([
    ('/', RootHandler.Handler),
    ('/create', MessageHandler.Handler),
    ('/message', MessageHandler.Handler),
    ('/stream', StreamHandler.Handler),
])

if __name__ == "__main__":
    fix_path()

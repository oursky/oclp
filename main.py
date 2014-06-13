import os
import sys

def fix_path():
    # credit:  Nick Johnson of Google
    sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

import webapp2

from handlers import RootHandler, MessageHandler, StreamHandler

application = webapp2.WSGIApplication([
    ('/', RootHandler.Handler),
    webapp2.Route('/create', handler=MessageHandler.Handler, name='post', methods=['POST']),
    ('/create', RootHandler.Handler),
    ('/message', MessageHandler.Handler),
    (r'/message/(.*)', MessageHandler.Share),
    ('/stream', StreamHandler.Handler)
])

if __name__ == "__main__":
    fix_path()

import webapp2
from handlers import RootHandler, MessageHandler, StreamHandler

application = webapp2.WSGIApplication([
    ('/', RootHandler.Handler),
    ('/create', MessageHandler.Handler),
    ('/message', MessageHandler.Handler),
    ('/stream', StreamHandler.Handler),
])

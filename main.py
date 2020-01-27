import logging

import tornado.ioloop
import tornado.web

from handler.json_ping_handler import JsonPingHandler
from handler.ping_handler import PingHandler
from tornado import log

PING_URL = r"/ping"
JSON_PING_URL = r"/json-ping"
PORT = 8888
LOG_LEVEL = logging.INFO


def make_app():
    return tornado.web.Application([
        (PING_URL, PingHandler),
        (JSON_PING_URL, JsonPingHandler)
    ])


def _set_log_level():
    log.app_log.setLevel(LOG_LEVEL) # Logging of errors from application code (i.e. uncaught exceptions from callbacks)
    log.gen_log.setLevel(LOG_LEVEL) # General-purpose logging, including any errors or warnings from Tornado itself.
    log.access_log.setLevel(LOG_LEVEL) # Per-request logging for Tornado’s HTTP servers (and potentially other servers in the future)

if __name__ == "__main__":
    app = make_app()
    _set_log_level()
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()

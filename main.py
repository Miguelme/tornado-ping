import tornado.ioloop
import tornado.web

from handler.json_ping_handler import JsonPingHandler
from handler.ping_handler import PingHandler

PING_URL = r"/ping"
JSON_PING_URL = r"/json-ping"
PORT = 8888

def make_app():
    return tornado.web.Application([
        (PING_URL, PingHandler),
        (JSON_PING_URL, JsonPingHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()

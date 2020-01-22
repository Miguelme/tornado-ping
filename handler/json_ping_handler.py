from datetime import datetime

import tornado


class JsonPingHandler(tornado.web.RequestHandler):
    def get(self):
        self.write({"response": "pong", "timestamp": str(datetime.now())})

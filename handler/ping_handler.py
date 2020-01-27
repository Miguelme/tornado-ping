from datetime import datetime

import tornado.web
from tornado import log


class PingHandler(tornado.web.RequestHandler):
    def get(self):
        log.app_log.info("Receiving ping at {}".format(datetime.now()))
        self.write("pong")

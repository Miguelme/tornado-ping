import tornado
from tornado import log


class IncrementHandler(tornado.web.RequestHandler):

    def get(self, number):
        log.app_log.info("Receiving request with number " + str(number))
        result = int(number) + 1
        return self.write(str(result))

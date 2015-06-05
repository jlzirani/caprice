import sys


class Logger(object):
    def info(self, message):
        sys.stdout.write(message.lstrip())
        sys.stdout.write("\n")


log = Logger()

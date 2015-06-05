import sys


class Logger(object):
    # "\033[*;**(;**)m"
    # "\033[*;**(;**)m"
    DEFAULT = "\033[0m"
    OK = "\033[0;32m"
    QUESTION = "\033[0;36m"
    ACTION = "\033[1;36m"


    def action(self, message):
        sys.stdout.write(self.ACTION)
        sys.stdout.write(message.lstrip())
        sys.stdout.write(self.DEFAULT)
        sys.stdout.write("\n")

    def question(self, message):
        sys.stdout.write(self.QUESTION)
        sys.stdout.write(message.lstrip())
        sys.stdout.write(self.DEFAULT)
        sys.stdout.write("\n")

    def ok(self, message):
        sys.stdout.write(self.OK)
        sys.stdout.write(message.lstrip())
        sys.stdout.write(self.DEFAULT)
        sys.stdout.write("\n")

    def info(self, message):
        sys.stdout.write(message.lstrip())
        sys.stdout.write("\n")


log = Logger()

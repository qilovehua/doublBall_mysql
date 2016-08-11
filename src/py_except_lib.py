class MyError_Latest(Exception):
    def __init__(self, strerr):
        self.strerr = strerr
    def __str__(self):
        return repr(self.strerr)
class Error(BaseException):
    message = 'Generic Error'

    def getMessage(self):
        return self.message

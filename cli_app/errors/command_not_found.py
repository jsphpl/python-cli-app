from .error import Error

class CommandNotFound(ValueError, Error):
    def __init__(self, name, available_names):
        self.message = 'Command "%s" not found. Registered commands are: %s' % (
            name,
            ', '.join(available_names)
        )

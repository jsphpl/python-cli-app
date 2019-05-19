import sys

class Env:
    platform = None
    is_linux = False
    is_darwin = False

    def __init__(self):
        self._check_platform()

    def _check_platform(self):
        self.platform = sys.platform
        if self.platform == 'linux':
            self.is_linux = True
        elif self.platform == 'darwin':
            self.is_darwin = True

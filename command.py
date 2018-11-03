class Command:
    name = None

    def __init__(self, app):
        self.app = app

    @staticmethod
    def register_arguments(parser):
        pass

    def run(self):
        pass

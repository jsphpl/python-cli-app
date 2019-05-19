import argparse

from .errors import Error, CommandNotFound
from .helpers import trim_docstring
from .env import Env


class App:
    args = None
    commands = {}
    env = None

    def __init__(self):
        self.env = Env()
        self.register_commands()

        parser = argparse.ArgumentParser(
            description=trim_docstring(self.__doc__),
            formatter_class=argparse.RawTextHelpFormatter
        )
        self.register_arguments(parser)
        self.parse_command_arguments(parser)
        self.args = parser.parse_args()

    def run(self):
        try:
            self.run_command(self.args.command)
        except Error as e:
            print(e.getMessage())


    def add_command(self, name, cls):
        self.commands[name] = {
            'name': name,
            'cls': cls,
            'description': cls.__doc__
        }

    def parse_command_arguments(self, parser):
        subparsers = parser.add_subparsers(dest='command')
        for name, config in self.commands.items():
            subparser = subparsers.add_parser(name, help=config['description'])
            config['cls'].register_arguments(subparser)

    def run_command(self, name):
        if name not in self.commands:
            raise CommandNotFound(name, self.commands.keys())

        config = self.commands[name]
        instance = config['cls'](self)
        return instance.run()

    def register_commands(self):
        pass

    def register_arguments(self, parser):
        pass

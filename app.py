import argparse
from pprint import pprint
from .helpers import trim_docstring


class App:
    args = None
    commands = {}

    def __init__(self):
        self.register_commands()

        parser = argparse.ArgumentParser(
            description=trim_docstring(self.__doc__),
            formatter_class=argparse.RawTextHelpFormatter
        )
        self.register_arguments(parser)
        self.parse_command_arguments(parser)
        self.args = parser.parse_args()

    def run(self):
        self.run_command(self.args.command)

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
            raise ValueError(
                'Command "%s" not found. Registered commands are: %s' %
                (name, ', '.join(self.commands.keys()))
            )

        config = self.commands[name]
        instance = config['cls'](self)
        return instance.run()

    def register_commands(self):
        pass

    def register_arguments(self, parser):
        pass

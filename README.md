# Python CLI App
> Framework for creating CLI apps using Python

The purpose of this library is to speed up bulding CLI applications by providing abstract classes representing an app and its commands. It uses `argparse` to define and parse command line arguments.

## Concepts
### App
An "App" is the main entry point of an application. It groups together one or more commands

### Command
A "Command" is a single operation that the application can perform. It is identified by a positional argument on the command line. Let's take `git` as an example. `git` would be the **app** that provides different **commands**, such as `add`, `commit`, `merge`, `checkout`, etc.

## Example
**git.py**
```python
#!/usr/bin/env python3

from cli_app import App
from commands.checkout import Checkout
from commands.merge import Merge


class Git(App):
    """Git - fast, scalable, distributed revision control system"""

    def register_commands(self):
        self.add_command('checkout', Checkout)  # make the Checkout command available through `git.py checkout …`
        self.add_command('merge', Merge)  # make the Merge command available through `git.py merge …`


if __name__ == '__main__':
    app = Git()
    app.run()

```

**commands/checkout.py**
```python
from cli_app import Command


class Checkout(Command):
    """Switch branches or restore working tree files"""

    @staticmethod
    def register_arguments(parser):
        parser.add_argument('ref', type=str, help='The ref (branch name, tag, commit sha) to checkout')

    def run(self):
        # Do whatever needs to be done to checkout given ref
        print('Checking out %s' % self.app.args.ref)
```

**commands/merge.py**
```python
from cli_app import Command


class Merge(Command):
    """Join two or more development histories together"""

    @staticmethod
    def register_arguments(parser):
        parser.add_argument('branch', type=str, help='The branch to merge into the currently checked-out branch')

    def run(self):
        # Do whatever needs to be done to merge given branch
        print('Merging %s into current branch' % self.app.args.branch)
```

import re

from jvasseur.packaging.feed import Command
from jvasseur.packaging.app.github import ArchiveGitHubApp
from config import base_url

OS_NAMES = {
    'darwin': 'Darwin',
    'freebsd': 'FreeBSD',
    'linux': 'Linux',
    'windows': 'Windows',
}

CPU_NAMES = {
    '386': 'i386',
    'amd64': 'x86_64',
    'arm': 'armv6l',
    'arm64': 'aarch64',
}

class Task(ArchiveGitHubApp):
    uri = base_url + 'task.xml'
    repo = 'go-task/task'

    def version(self, tag_name):
        if tag_name == 'nightly':
            return None

        return tag_name.removeprefix('v')

    def assets(self, assets):
        for asset in assets:
            match = re.fullmatch(r'task_(?P<os>[a-z]+)_(?P<cpu>[a-z0-9]+)(\.tar\.gz|\.zip)', asset['name'])

            if match is not None:
                os = OS_NAMES.get(match.group('os'))
                cpu = CPU_NAMES.get(match.group('cpu'))

                if os is not None and cpu is not None:
                    yield f'{os}-{cpu}', asset

    def commands(self, data):
        yield Command(
            name='run',
            path='task.exe' if data['arch'].startswith('Windows-') else 'task',
        );

if __name__ == '__main__':
    Task().main()

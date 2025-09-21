import re

from jvasseur.packaging.app.github import FileGitHubApp
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
    'ppc64': 'ppc64',
}

class Direnv(FileGitHubApp):
    uri = base_url + 'direnv.xml'
    repo = 'direnv/direnv'

    def assets(self, assets):
        for asset in assets:
            match = re.fullmatch(r'direnv\.(?P<os>[a-z]+)-(?P<cpu>[a-z0-9]+)(?:\.exe)?', asset['name'])

            if match is not None:
                os = OS_NAMES.get(match.group('os'))
                cpu = CPU_NAMES.get(match.group('cpu'))

                if os is not None and cpu is not None:
                    yield f'{os}-{cpu}', asset

    def file_name(self, data):
        if data['arch'].startswith('Windows-'):
            return 'direnv.exe'
        else:
            return 'direnv'

if __name__ == '__main__':
    Direnv().main()

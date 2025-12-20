import re

from jvasseur.packaging.app.github import FileGitHubApp
from jvasseur.packaging.feed import Command, File, Runner
from config import base_url

class Composer(FileGitHubApp):
    uri = base_url + 'composer.xml'
    repo = 'composer/composer'

    def version(self, tag_name):
        return re.sub(r'-RC(?P<number>[0-9]+)', r'-rc\g<number>', tag_name)

    def assets(self, assets):
        for asset in assets:
            if asset['name'] == 'composer.phar':
                yield None, asset

    def file_name(self, data):
        return 'composer.phar'

    def file_executable(self, data):
        return False

    def commands(self, data):
        yield Command(
            Runner(
                interface='https://packages.jvasseur.me/php.xml',
            ),
            name='run',
            path=self.file_name(data),
        )

if __name__ == '__main__':
    Composer().main()

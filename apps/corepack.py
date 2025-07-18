from jvasseur.packaging.app.npm import NpmApp, create_node_command
from config import base_url

class Corepack(NpmApp):
    uri = base_url + 'corepack.xml'
    name = 'corepack'

    def commands(self, data):
        constraint = data.get('engines', {}).get('node')

        # npm and npx are not defined in version data (probably to prevent conflicts) so we have to add them manualy
        commands = super().commands(data)
        commands.append(create_node_command('npm', './dist/npm.js', constraint))
        commands.append(create_node_command('npx', './dist/npx.js', constraint))

        return commands

if __name__ == '__main__':
    Corepack().main()

from jvasseur.packaging.app.npm import NpmApp
from config import base_url

class Corepack(NpmApp):
    uri = base_url + 'corepack.xml'
    name = 'corepack'

if __name__ == '__main__':
    Corepack().main()

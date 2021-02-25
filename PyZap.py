import requests
import zipfile
from packaging import version
import json
import os

owner = 'CodyAbode'
repo = 'PyZap'

def update():
    url = 'https://api.github.com/repos/' + owner + '/' + repo + '/releases/latest'
    with zipfile.ZipFile('PyZap.pyz') as archive:
        with archive.open('version.txt') as file:
            current_version = file.read().decode()
    request = requests.get(url)
    release = json.loads(request.text)
    if version.parse(release['tag_name']) > version.parse(current_version):
        print('Update needed:', release['tag_name'], '>', current_version)
        for asset in release['assets']:
            if asset['name'] == 'PyZap.pyz':
                getfile = requests.get(asset['browser_download_url'])
                os.remove('PyZap.pyz')
                open('PyZap.pyz', 'wb').write(getfile.content)
                print('Updated')
                break
            print('Could not find PyZap.pyz')
    else:
        print('Already on the latest version')

def main():
    update()
    print('Hello world!')

if __name__ == '__main__':
    main()
import os
import urllib.request
import gzip

# Downloading within programs automatically (does not preform any visible action)
def download(url):
    cwd = os.getcwd()
    filename = os.path.split(url)[-1]
    download = urllib.request.urlopen(url)
    with open(filename, 'b+w') as f:
        f.write(download.read())
        
# Standard download system
def requestDownload(url):
    cwd = os.getcwd()
    filename = os.path.split(url)[-1]
    print('Downloading ' + url + ' to ' + cwd)
    print('y/n?')
    yn = input()
    if yn == 'y':
        download = urllib.request.urlopen(url)
        with open(filename, 'b+w') as f:
            f.write(download.read())
        print('Press enter to terminate')
        input()
    else:
        print('Download cancelled.')
        print('Press enter to terminate')
        input()

# Downloading within programs automatically (delievers one line to console for logging)
def printDownload(url):
    cwd = os.getcwd()
    filename = os.path.split(url)[-1]
    print('Downloading ' + url + ' to ' + cwd)
    download = urllib.request.urlopen(url)
    with open(filename, 'b+w') as f:
        f.write(download.read())

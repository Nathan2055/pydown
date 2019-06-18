# All standard functions for pydown

import os
import urllib.request
import gzip

# Standard download system
def download(url):
    # ToDo - Implement printing the size
    # print('Total size of download - ' + size)
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

'''      
# Standard download system (alternate version, will be phased out eventually)
def stddlalt(url):
    # ToDo - Implement printing the size
    # print('Total size of download - ' + size)
    cwd = os.getcwd()
    filename = os.path.split(url)[-1]
    print('[pydown] - Downloading ' + url + ' to ' + cwd)
    print('[pydown] - y/n?')
    yn = input()
    if yn == 'y':
        download = urllib.request.urlopen(url)
        with open(filename, 'b+w') as f:
            f.write(download.read())
        print('[pydown] - Press enter to terminate')
        input()
    else:
        print('[pydown] - Download cancelled.')
        print('[pydown] - Press enter to terminate')
        input()
'''

# Downloading within programs automatically (delievers one line to console for logging)
def printDownload(url):
    cwd = os.getcwd()
    filename = os.path.split(url)[-1]
    print('Downloading ' + url + ' to ' + cwd)
    download = urllib.request.urlopen(url)
    with open(filename, 'b+w') as f:
        f.write(download.read())

# Downloading within programs automatically (does not preform any visible action)
def printDownload(url):
    cwd = os.getcwd()
    filename = os.path.split(url)[-1]
    download = urllib.request.urlopen(url)
    with open(filename, 'b+w') as f:
        f.write(download.read())

# Debug file for if the new setup blows everything up
# This consists of the old single file format from before.
# -----
# pydown - Here's the source code. May be spread out into individual files in the future.

import os
import urllib.request
import gzip

# Standard download system.
def stddl(url):
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
        
# Standard download system (alternate version, will be phased out eventually).
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

# Downloading within programs automatically (for scripts and stuff).
def intdl(url):
    cwd = os.getcwd()
    filename = os.path.split(url)[-1]
    print('Downloading ' + url + ' to ' + cwd)
    download = urllib.request.urlopen(url)
    with open(filename, 'b+w') as f:
        f.write(download.read())
    

# The current version of the text interface. In the future this will be depreciated and available in another source file.
def originalCLI():
    # Greetings!
    print('Welcome to pydown!')
    print('This program is copyright 2013 Nathan2055, use is subject to the terms in the LICENSE.txt file included with the distribution.')
    print('-----')

    # Collect the data
    # #1 Download directory
    print('Welcome! Please enter the full path of your working directory:')
    dest = input()
    if dest != '':
        os.chdir(dest)
    cwd = os.getcwd()
    print('Your working directory is ' + cwd)
    # #2 Download url
    print('Please enter the URL of the file you wish to download:')
    url = input()
    # #3 Compression
    print('Would you like to compress the end result using gzip? (y/n)')
    willCompress = input()
    
    # Now download the file
    print('Downloading file...', end='')
    download = urllib.request.urlopen(url)
    filename = os.path.split(url)[-1]
    print('done!')
    
    # Compress and save...
    if willCompress == 'y':
        print('Compressing and saving file...', end='')
        with gzip.open(filename + '.gz', 'wb') as f:
            f.write(download.read())
        print('done!')
        print('Press enter to terminate')
        input()
    
    # ...or just save
    else:
        print('Saving to file...', end='')
        with open(filename, 'b+w') as f:
            f.write(download.read())
        print('done!')
        print('Press enter to terminate')
        input()

originalCLI()

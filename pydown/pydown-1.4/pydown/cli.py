# Old style (before functions) CLI for pydown

import os
import urllib.request
import gzip

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

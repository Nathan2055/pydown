# pydown - A simple command line downloader written in Python
# Written by Nathan2055, licensed under the 3-clause BSD

import os
import urllib.request
import gzip

# Greetings!
print('Welcome to pydown!')
print('This program is copyright 2013 Nathan2055, use is subject to the terms in the LICENSE.txt file included with the distribution.')
print('-----')

# Set up the download location
print('Welcome! Please enter the full path of your working directory:')
dest = input()
os.chdir(dest)
cwd = os.getcwd()
print('Your working directory is ' + cwd)

# Now download the file
print('Please enter the URL of the file you wish to download:')
url = input()
print('Downloading file...')
download = urllib.request.urlopen(url)
filename = os.path.split(url)[-1]
print('Done!')

# Decisions, decisions...
print('Please type "yes" and press enter if you wish to gzip the finished file, or just hit enter to continue:')
willCompress = input()

# This path is followed if you choose to compress the product
if willCompress == 'yes':
    print('Compressing file...')
    with gzip.open(filename + '.gz', 'wb') as f:
        f.write(download.read())
    print('Done!')
    print('Press enter to terminate')
    input()

# This path produces the uncompressed product
else:
    print('Saving to file...')
    with open(filename, 'b+w') as f:
        f.write(download.read())
    print('Done!')
    print('Press enter to terminate')
    input()

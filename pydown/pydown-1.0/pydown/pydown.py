# pyget - An advanced wget clone written in Python
import os
import urllib.request
import gzip
print('Welcome to pydown!')
print('This program is copyright 2013 Nathan2055, use is subject to the terms in the LICENSE.txt file included with the distribution.')
print('-----')
print('Welcome! Please enter the full path of your working directory:')
dest = input()
os.chdir(dest)
cwd = os.getcwd()
print('Your working directory is ' + cwd)
print('Please enter the URL of the file you wish to download:')
url = input()
print('Downloading file...')
download = urllib.request.urlopen(url)
print('Done!')
print('Getting file name...')
print('Done!')
filename = os.path.split(url)[-1]
print('Please type "yes" and press enter if you wish to gzip the finished file, or just hit enter to continue:')
willCompress = input()
if willCompress == 'yes':
    print('Compressing file...')
    with gzip.open(filename + '.gz', 'wb') as f:
        f.write(download.read())
    print('Done!')
    print('Press enter to terminate')
    input()
else:
    print('Saving to file...')
    with open(filename, 'b+w') as f:
        f.write(download.read())
    print('Done!')
    print('Press enter to terminate')
    input()

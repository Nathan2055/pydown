import hashlib
import sys
from functools import partial
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("algorithim", help="the hashing algorithim to use")
parser.add_argument("file", help="the file to check")
args = parser.parse_args()

def md5sum(filename):
    with open(filename, mode='rb') as f:
        d = hashlib.md5()
        for buf in iter(partial(f.read, 128), b''):
            d.update(buf)
    return d.hexdigest()

def sha1sum(filename):
    with open(filename, mode='rb') as f:
        d = hashlib.sha1()
        for buf in iter(partial(f.read, 128), b''):
            d.update(buf)
    return d.hexdigest()

def sha256sum(filename):
    with open(filename, mode='rb') as f:
        d = hashlib.sha256()
        for buf in iter(partial(f.read, 128), b''):
            d.update(buf)
    return d.hexdigest()

if args.algorithim == 'md5':
    print(md5sum(args.file))
elif args.algorithim == 'sha1':
    print(sha1sum(args.file))
elif args.algorithim == 'sha256':
    print(sha256sum(args.file))

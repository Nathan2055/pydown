===========
pydown
===========

pydown is a Python based downloader with compression support. It currently includes an easy to use command line interface, but we have plans for command line switches and functions to add downloading to your own code. Install it by downloading the tarball, unzipping it, and then running "python setup.py install" on the directory. It can then be run with "python -m pydown".


Changelog
=========

v1.1
-------------
* The main script has been completly rewritten, it now collects all of the info it needs and THEN works on the download
* The package has been revamped, it will now execute properly when called
* Two unused code files, natfun.py and oldCode.py, have been added to the package

v1.0.1
-------------
* Updated documentation to remove old mentions of the working name "pyget" and gnerally clean it up
* Added gzip package, planned to become the only distributed package

v1.0.0
-------------
* Initial release

License
=========

Copyright (c) 2013 Nathan2055
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the software nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE DEVELOPERS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
from setuptools import setup

setup(
    name='pydown',
    version='1.3',
    author='Nathan2055',
    author_email='nathan2055@private.fake',
    packages=['pydown',],
    url='http://pypi.python.org/pypi/pydown/',
    license='BSD license',
    description='A program that provides easy downloading to Python 3',
    long_description=open('README.txt').read(),
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
    ],
    install_requires=[
    'setuptools',
    ],
)

from setuptools import setup

setup(
    name='pydown',
    version='0.1',
    author='Nathan2055',
    author_email='nathan2055@private.fake',
    packages=['pydown',],
    url='http://pypi.python.org/pypi/pydown/',
    license=open('LICENSE.txt').read()
    description='Downloading, simplified',
    long_description=open('README.rst').read(),
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
    ],
    install_requires=[
    'setuptools',
    ],
)

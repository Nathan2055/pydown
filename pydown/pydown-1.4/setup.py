from setuptools import setup

setup(
    name='pydown',
    version='1.4',
    author='Nathan2055',
    author_email='nathan2055@private.fake',
    packages=['pydown',],
    url='http://pypi.python.org/pypi/pydown/',
    license='BSD license',
    description='The ultimate downloading library for Python',
    long_description=open('README.rst').read(),
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

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pydown",
    version="2.0",
    author="Nathan Larsen",
    author_email="nlarsen@nathan2055.com",
    description="Python library allowing you to download files with a one-liner",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nathan2055/pydown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

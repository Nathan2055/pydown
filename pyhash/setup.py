import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyhash",
    version="0.1",
    author="Nathan Larsen",
    author_email="nlarsen@nathan2055.com",
    description="A simple tool to make calculating file hashes easy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nathan2055/pyhash",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

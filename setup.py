import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pylts",
    version="0.0.1",
    author="Alan Bandeira",
    author_email="alan.p.bandeira@gmail.com",
    description="A library for modeling systems using Labelled Trasition System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alanpbandeira/pylts.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
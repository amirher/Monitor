import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Monitor",
    version = "0.1.0",
    author = "Bobby Dilley",
    author_email = "bobbydilley@live.com",
    description = ("A network monitoring solution."),
    license = "BSD",
    keywords = "linux monitor database",
    url = "http://github.com/bobbydilley/Monitor",
    packages=['Monitor', 'tests'],
    long_description=read('README'),
    scripts=['bin/monitor'],
)

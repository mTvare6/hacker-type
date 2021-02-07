import setuptools
import os
setuptools.setup(
        name='hackertype',
    version='0.1.0',
    scripts=['bin/hacker-type'],
    author='mTvare',
    description='CLI based version of https://hackertyper.net/.',
    install_requires=[
        'setuptools'
    ],
    python_requires='>=3.6'
)
#os.rename("./hacker-type/__init__.py", "/usr/local/bin/hacker-type")

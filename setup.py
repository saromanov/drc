import os
from setuptools import setup

def read(name):
    return open(os.path.join(os.path.dirname(__file__), name)).read()

setup(
    name='python-drc',
    version='7.4.1',
    description="Package for Docker v2 Registry",
    long_description=read('README.rst'),
    keywords='docker registry',
    author='Sergey Romanov',
    author_email='xxsmotur@gmail.com',
    url='https://github.com/saromanov/drc',
    license='MIT',
    packages=['drc'],
    entry_points={'console_scripts': ['drc=drc.main:main']},
)
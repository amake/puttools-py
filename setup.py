from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='torrenttools',
    version='1.0',
    description='Tools for getting torrents via Put.io',
    long_description=long_description,
    url='http://example.com',
    author='Aaron Madlon-Kay',
    author_email='aaron@madlon-kay.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Internet',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='bittorrent torrent putio put.io',
    py_modules=['putioget', 'feedputter'],
    install_requires=['putio @ git+https://github.com/amake/putio-py.git'],
    entry_points={
        'console_scripts': [
            'feedputter=feedputter:main',
            'putioget=putioget:main',
        ],
    }
)

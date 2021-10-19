from os.path import join, dirname
from setuptools import setup, find_packages


setup(
    name="RSS-Reader",
    version="0.2",
    author="Vitaliy Chiruk",
    author_email="backstep13@tut.by",
    license="GNU GPL",
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    entry_points={
        'console_scripts':
            ['rss-reader = rss_reader.rss_reader:main']}
)

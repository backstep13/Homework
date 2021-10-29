from os.path import join, dirname
from setuptools import setup, find_packages


setup(
    name="RSS-Reader",
    version="0.4",
    author="Vitaliy Chiruk",
    license="GNU GPL",
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'rss_reader/data/README.md')).read(),
    install_requires=['fpdf>=1.7.2'],
    include_package_data=True,
    package_data={'rss_reader': ['data/README.md', 'data/storage.json', 'DejaVuSansCondensed.ttf']},
    entry_points={'console_scripts': ['rss-reader = rss_reader.rss_reader:main']}
)

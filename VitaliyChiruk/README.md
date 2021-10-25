        RSS-Reader

What is it?
-----------

Pure Python command-line RSS reader. Enter the url-address of the rss-feed
and read the news.

        rss-reader https://news.yahoo.com/rss/ --limit 1

        Feed: YahooNews

        Title: FirstNews
        Date: 2021-10-14 18:55:03 UTC+1
        Description: FirstNews is ...
        ============================================================

Documentation
-------------

The documentation available as of the date of this release is
included in 1) help, if you enter 'rss-reader -h' or 'rss-reader --help' 
in command line; 2) README.md.

        RSS-Reader [-h] [--version] [--json] [--verbose] [--limit LIMIT] source

        Pure Python command-line RSS reader.

        positional arguments:
        source         RSS URL

        optional arguments:
        -h, --help     show this help message and exit
        --version      Print version info
        --json         Print result as JSON in stdout
        --verbose      Outputs verbose status messages
        --limit LIMIT  Limit news topics if this parameter provided
        --date DATE    Y-m-d format, for example: 2020-04-22

JSON has structure:

        {
        "Title": "string",
        "Date": "string",
        "Link": "string"
        "Description": "any"
        }

Date mode allows read news from local storage on a specified date, 
possibly without specifying a source

Installation
------------

Unpack the RSS-Reader distribution archive that you downloaded to
where you wish to install the program. We will refer to this destination
location as your {installation home} below.

        $ cd ~/installation home
        $ tar -xvf RSS-Reader-0.3.tar.gz

Open a console and cd into "{installation home}" and type:

        $ cd ./RSS-Reader-0.3/

Install the program

        $ sudo python3 setup.py install

Licensing
---------

GNU General Public License.

Contacts
--------

Vitaliy Chiruk
backstep13@tut.by

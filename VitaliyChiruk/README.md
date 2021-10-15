        RSS-Reader

What is it?
-----------

Pure Python command-line RSS reader. Enter the url-address of the rss-feed
and read the news.

        rss-reader https://news.yahoo.com/rss/ --limit 5

        Feed: YahooNews

        Title: FirstNews
        Date: 2021-10-14 18:55:03 UTC+1
        Description: FirstNews is ...
        ============================================================

Documentation
-------------

The documentation available as of the date of this release is
included in help, if you enter 'rss-reader -h' or 'rss-reader --help' 
in command line.

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

JSON has structure:

        {
        "Title": "Представляем Ansible Automation Platform 2",
        "Date": ", 15 Oct 2021 17:35:34 GMT",
        "Link": "https://habr.com/ru/post/583758/
        "Description": "На прошедшей в конце сентября конференции мы анонсировали новую,
        вторую версию платформы автоматизации Ansible, над которой трудились два года. 
        Сегодня мы дадим краткий обзор концептуальных новшеств и полезных ресурсов по 
        Ansible Automation Platform 2, а также начнем чуть подробнее знакомиться с ее 
        новыми функциями
        }

Installation
------------

Please see the file called.  Platform specific notes can be
found in README.platforms.

Licensing
---------

GNU General Public License.

Contacts
--------

Vitaliy Chiruk
backstep13@tut.by

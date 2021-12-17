import feedparser
import sqlite3
import os


scriptDir = os.path.dirname(os.path.realpath(__file__))


def parser(url, limit):
    """
    INPUT: url, limit
    OUTPUT: list_data
    """
    list_data = []
    if limit is None:
        limit = 100
    elif limit <= 0:
        print("You enter wrong limit number")
        return list_data

    feed = feedparser.parse(url)
    if not feed["entries"]:
        print("Error URL or not RSS, please enter right URL")
        return False

    for i in feed["entries"]:
        if limit == 0:
            return list_data
        limit -= 1
        title = i["title"]
        date = i["published"]
        link = i["link"]
        try:
            description = i["description"]
        except KeyError:
            description = ""
        data = {"title": title, "date": date, "link": link, "description": description}
        list_data.append(data)
    return list_data


def cache(data):
    """
    INPUT: list_data
    OUTPUT: data to SQLite
    """
    db_conn = sqlite3.connect(scriptDir + "/rss_base.sqlite")
    db = db_conn.cursor()
    db.execute('''CREATE TABLE IF NOT EXISTS feed
               (title TEXT, 
               date TEXT, 
               link TEXT PRIMARY KEY,
               description TEXT DEFAULT NULL);''')
    for i in data:
        new_data = (i["title"], i["date"], i["link"], i["description"])
        db.execute("INSERT OR IGNORE INTO feed VALUES (?, ?, ?, ?);", new_data)
        db_conn.commit()


def read_news(date, limit=None):
    """
    INPUT: limit, date, source
    OUTPUT: list_data
    """
    db_conn = sqlite3.connect(scriptDir + "/rss_base.sqlite")
    db = db_conn.cursor()
    list_data = []
    query = "SELECT * FROM feed WHERE date=\"" + date + "\" ORDER BY date;"
    db.execute(query)
    if limit:
        result = db.fetchmany(limit)
    else:
        result = db.fetchall()

    for i in result:
        data = dict()
        data['title'] = i[0]
        data['date'] = i[1]
        data['link'] = i[2]
        data['description'] = i[3]
        list_data.append(data)
    if list_data:
        return list_data  # TODO del data in DB
    else:
        print(f"Don't have data on {date} \n")

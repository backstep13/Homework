#!/usr/bin/env python3

import argparse
import urllib.request
from urllib.error import HTTPError, URLError
from xml.dom import minidom
import xml.parsers.expat
import json
import re
import os


storage_path = os.getcwd()
filename = os.path.join(os.path.split(storage_path)[0], 'storage.json')


def create_parse():
    """Function create console arguments
    INPUT: -
    OUTPUT: ArgumentParser object (names of arguments)"""
    parser = argparse.ArgumentParser(prog="RSS-Reader", description="Pure Python command-line RSS reader.")
    parser.add_argument("source", type=str, nargs='?', help="RSS URL")
    parser.add_argument("--version", action="version", version="%(prog)s Version 0.3", help="Print version info")
    parser.add_argument("--json", action="store_true", help="Print result as JSON in stdout")
    parser.add_argument("--verbose", action="store_true", help="Outputs verbose status messages")
    parser.add_argument("--limit", type=int, help="Limit news topics if this parameter provided")
    parser.add_argument("--date", type=str, help="Y-m-d format, for example: 2020-04-22")
    return parser


def get_data(url, date, limit, json_type=False, verbose=False):
    """Function get data from URL address,
    if data is in XML format - read data else write ERROR.
    If date mode, have not url - call another function.
    INPUT: url address, date, limit, verbose mode from console arguments
    OUTPUT: XML data or call another function"""
    if url is None and date:
        read_news(limit, json_type, date, verbose)
        return False
    elif url is None and date is None:
        print("You didn't enter URL")
        return False
    elif url and date:
        read_news(limit, json_type, date, verbose, url)
        return False
    else:
        try:
            if verbose:
                print("---> try to connect url")
            with urllib.request.urlopen(url) as res:  # request to url
                if verbose:
                    print("---> connection successful\n---> try to read data from url")
                dom = minidom.parseString(res.read().decode('utf-8'))  # reading xml
                if verbose:
                    print("---> reading is successful")
                return dom
        except (HTTPError, URLError):
            print("ERROR: Wrong url, check the url address")
        except (TypeError, xml.parsers.expat.ExpatError, ValueError):  # if not xml
            print("ERROR: Invalid data")


def print_data(title, date, link, description, json_type=False):
    """Function print result to json or string format
    INPUT: XML-tags which request the program
    OUTPUT: string or json data from feed"""
    try:
        if json_type:
            data = (json.dumps({"Title": title, "Date": date, "Link": link, "Description": description},
                    indent=4, ensure_ascii=False))  # false ensure ascii for russian alphabet
            print(data)
            return data
        else:
            data = "Title: "+str(title)+"\nDate: "+str(date)+"\nLink: "+str(link)+"\n\n" + description
            print(data)
            print("==========================================================================================\n")
            return data
    except (TypeError, ValueError):
        print("ERROR: Error data")


def output_data(source, dom, limit, json_type=False, verbose=False):
    """Function parse XML, read data from XML-tags and save and print data
    INPUT: data source, xml-data; limit items & verbose mode & json format from console arguments
    OUTPUT: None, print data from items in stdout"""
    try:
        if verbose:
            print("---> try to read xml items")
        print(f"Feed: {dom.getElementsByTagName('title')[0].firstChild.nodeValue}\n")
        count = 0  # limit counter
        for i in dom.getElementsByTagName('item'):  # loop for search info by XML-tag <item>
            if verbose:
                print("---> check limit")
            if limit is None:  # if limit not provided limit=1000 (big number)
                limit = 1000
            elif limit > 0:  # count items for limit stop
                if count >= limit:
                    if verbose:
                        print("---> limit is over")
                    break
                count += 1
            else:
                print("ERROR: wrong limit number")  # if limit -1, 0 etc.
                break
            if verbose:
                print(f"---> read item №{count}")

            title = i.getElementsByTagName('title')[0].firstChild.nodeValue
            date = check_variable('pubDate', i)  # check optional parameters for information
            date = time_format(date, verbose)  # format data 2021-10-30
            description = check_variable("description", i)
            description = re.sub(r'\<[^>]*\>', '', str(description))
            link = i.getElementsByTagName('link')[0].firstChild.nodeValue

            print_data(title, date, link, description, json_type)  # check json mode or string, and print data
            data_to_cache = {"Feed": source, "Title": title, "Date": date, "Link": link, "Description": description}
            cache(data_to_cache, verbose)

    except (AttributeError, NameError):
        print("Problem with items in XML")


def check_variable(var, i):
    """Function check existence of a variable
    INPUT: XML-tag which need checking
    OUTPUT: string (400 symbols) from XML or space in stdout"""
    try:
        return i.getElementsByTagName(var)[0].firstChild.nodeValue[:400]  # if item too long
    except IndexError:
        print("")


def check_unique(json_dict, check_data, verbose=False):
    """Function compare new data and json file.
    If new data is unique, return new data
    INPUT: data from json file, data for checking
    OUTPUT: unique data"""
    unique = True
    if verbose:
        print("---> compare data from RSS and storage.json")
    for i in json_dict["data"]:
        if i["Link"] == check_data["Link"]:  # compare links
            unique = False
            if verbose:
                print("---> data is not unique")
    if unique:
        if verbose:
            print("---> data is UNIQUE")
        return check_data


def check_file(verbose=False):
    """Function create data in storage.json if data in it
    is not correct of file is empty
    INPUT: -
    OUTPUT: required data in storage.json"""
    prolog = {"data": []}
    if verbose:
        print('---> create required data on storage.json')
    with open(filename, 'w') as file:
        json.dump(prolog, file)


def cache(new_data, verbose=False):
    """Function add new data in json file if new data unique
    INPUT: new data from RSS feed
    OUTPUT: write unique data in file"""
    try:
        with open(filename) as file:
            if verbose:
                print("---> try to load json from file")
            dict_data = json.load(file)
            add = check_unique(dict_data, new_data, verbose)
            if add:
                dict_data["data"].append(add)

        with open(filename, 'w') as file:
            if verbose:
                print("---> try to dump data in storage.json")
            json.dump(dict_data, file, indent=4)

    except FileNotFoundError:
        print('File storage.json is not found')
    except (json.decoder.JSONDecodeError, KeyError):
        check_file()


def read_news(limit, json_type, date, verbose=False, source=None):
    """Function write data from json in stdout and then call delete function
    INPUT: required date
    OUTPUT: string data"""
    del_list = []
    with open(filename) as file:
        if verbose:
            print("---> try to load json from file")
        json_data = json.load(file)
        if not json_data["data"]:
            print("Error: have not data in storage")
        not_data = 0
        count = 0
        for i in json_data["data"]:
            if i["Date"] == date:
                if limit is None:  # if limit not provided limit=1000 (big number)
                    limit = 1000
                elif limit > 0:  # count items for limit stop
                    if count >= limit:
                        break
                    count += 1
                if verbose:
                    print("---> find data on required date")
                if source is None:
                    print_data(i["Title"], i["Date"], i["Link"], i["Description"], json_type)
                    del_list.append(i)
                    not_data += 1
                else:
                    if i["Feed"] == str(source):
                        print_data(i["Title"], i["Date"], i["Link"], i["Description"], json_type)
                        del_list.append(i)
                        not_data += 1

    if not_data == 0:
        print("Error: have not data for this date")

    for i in del_list:
        json_data["data"].remove(i)

    with open(filename, 'w') as file:
        json.dump(json_data, file, indent=4)


def time_format(time, verbose=False):
    """Function get date of required format from any string (popular date formats)
    INPUT: string of date
    OUTPUT: date in format YYYY-MM-DD"""
    months = {
        'jan': '01', 'feb': '02', 'mar': '03', 'apr': '04', 'may': '05', 'jun': '06',
        'jul': '07', 'aug': '08', 'sep': '09', 'oct': '10', 'nov': '11', 'dec': '12',
    }
    lst = time.lower().split()
    if len(lst) == 1:
        if verbose:
            print("---> len(data) is 1")
        format_data = str(lst[0]).split('t')
        if verbose:
            print(f"---> format data = {format_data}")
        return format_data[0]
    else:
        for i in lst:
            try:
                _ = int(i)  # checking 'is number or letter/symbol'
            except ValueError:
                if i in months:  # replace month name and month number
                    if verbose:
                        print("---> string is month")
                    num_month = months[i]
                    index = lst.index(i)
                    lst.remove(i)
                    lst.insert(index, num_month)
                else:
                    lst.remove(i)
        new_lst = lst[:3]  # del extra
        if len(new_lst[0]) != 4:  # change 10 12 2020 to 2020 12 10
            new_lst.reverse()
        if len(new_lst[2]) == 1:
            new_lst.insert(2, str('0'+new_lst[2].pop))
        if verbose:
            print("---> preparing format data")
        format_data = '-'.join(new_lst)
        return format_data


def main():
    """Function read console arguments, get data from URL feed
    and execute commands
    INPUT: -
    OUTPUT: None, call another functions or messages"""
    args = create_parse().parse_args()

    if args.verbose:
        print("---> start program")

    url_ok = get_data(args.source, args.date, args.limit, args.json, args.verbose)

    if url_ok:
        output_data(args.source, url_ok, args.limit, args.json, args.verbose)

    if args.verbose:
        print("---> finish program")


if __name__ == "__main__":
    if not os.path.exists(filename):
        check_file()
    main()

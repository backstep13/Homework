import argparse
import urllib.request
from urllib.error import HTTPError
from xml.dom import minidom
import xml.parsers.expat
import json


def create_parse():
    """Function create console arguments
    INPUT: -
    OUTPUT: ArgumentParser object (names of arguments)"""
    parser = argparse.ArgumentParser(prog="RSS-Reader", description="Pure Python command-line RSS reader.")
    parser.add_argument("source", type=str, help="RSS URL")
    parser.add_argument("--version", action="version", version="%(prog)s Version 0.1", help="Print version info")
    parser.add_argument("--json", action="store_true", help="Print result as JSON in stdout")
    parser.add_argument("--verbose", action="store_true", help="Outputs verbose status messages")
    parser.add_argument("--limit", type=int, help="Limit news topics if this parameter provided")
    return parser


def get_data(url, verbose=False):
    """Function get data from URL address,
    if data is in XML format - read data else write ERROR
    INPUT: url address, verbose mode from console arguments
    OUTPUT: XML data"""
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
    except HTTPError:
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
            data = "Title: "+str(title)+"\nDate: "+str(date)+"\nLink: "+str(link)+"\n"+str(description)
            print(data)
            print("==========================================================================================\n")
            return data
    except (TypeError, ValueError):
        print("ERROR: Error data")


def output_data(dom, limit, verbose=False, json_type=False):
    """Function parse XML, read data from XML-tags and print data
    INPUT: xml-data; limit items & verbose mode & json format from console arguments
    OUTPUT: None, print data from items in stdout"""
    try:
        if verbose:
            print("---> try to read xml items")
        print(f"Feed: {dom.getElementsByTagName('title')[0].firstChild.nodeValue}\n")  # print source
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
            description = check_variable("description", i)
            link = i.getElementsByTagName('link')[0].firstChild.nodeValue

            print_data(title, date, link, description, json_type)  # check json mode or string, and print data

    except (AttributeError, NameError):
        print("Problem with items in XML")


def check_variable(var, i):
    """Function check existence of a variable
    INPUT: XML-tag which need checking
    OUTPUT: string (400 symbols) from XML or space in stdout"""
    try:
        return i.getElementsByTagName(var)[0].firstChild.nodeValue[3:400]  # if description too long
    except IndexError:
        print(" ")


def main():
    """Function read console arguments, get data from URL feed
    and execute commands
    INPUT: -
    OUTPUT: None, call another functions or messages"""

    args = create_parse().parse_args()

    if args.verbose:
        print("---> start program")

    url_ok = get_data(args.source, args.verbose)
    if url_ok:
        output_data(url_ok, args.limit, args.verbose, args.json)

    if args.verbose:
        print("---> finish program")


if __name__ == "__main__":
    main()

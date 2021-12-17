import json


def print_json(list_data):
    """
    INPUT: list_data
    OUTPUT: stdout
    """
    try:
        for i in list_data:
            print(json.dumps(i, indent=4, ensure_ascii=False))  # false ensure ascii for russian alphabet
            print("=" * 90 + "\n")
    except (TypeError, ValueError):
        print("ERROR: Error data")


def print_data(list_data):
    """
    INPUT: list_data
    OUTPUT: stdout
    """
    print("\n")
    for i in list_data:
        print("Title: " + i["title"])
        print("Date " + i["date"])
        print("Link: " + i["link"])
        print(i["description"])
        print("=" * 90 + "\n")

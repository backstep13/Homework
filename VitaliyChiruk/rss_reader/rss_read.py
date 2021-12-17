#!/usr/bin/env python3


def create_parse():
    """Function create console arguments
    INPUT: -
    OUTPUT: ArgumentParser object (names of arguments)"""
    pars = argparse.ArgumentParser(prog="RSS-Reader", description="Pure Python command-line RSS reader")
    pars.add_argument("source", type=str, nargs="?", help="RSS URL")
    pars.add_argument("--version", action="version", version="%(prog)s Version 1.0", help="Print version info")
    pars.add_argument("--json", action="store_true", help="Print result as JSON in stdout")
    pars.add_argument("--limit", type=int, help="Limit news topics if this parameter provided")
    pars.add_argument("--date", type=str, help="Y-m-d format, for example: 2020-04-22")
    pars.add_argument("--to-pdf", type=str, help="Convert news to PDF and save to path")
    pars.add_argument("--to-html", type=str, help="Convert news to HTML and save to path")
    return pars


if __name__ == "__main__":

    import argparse
    import parser_rss_line
    import printer
    import converter

    args = create_parse().parse_args()
    if args.source is None and args.date is None:
        print("You didn't enter URL or date")
        list_data = []
    elif args.date:
        list_data = parser_rss_line.read_news(args.date, args.limit)
    else:
        list_data = parser_rss_line.parser(args.source, args.limit)
        parser_rss_line.cache(list_data)

    if args.json:
        printer.print_json(list_data)
    else:
        printer.print_data(list_data)

    if args.to_pdf:
        converter.convert_to_pdf(list_data, args.to_pdf)
    elif args.to_html:
        converter.convert_to_html(list_data, args.to_html)

'''
1. Не удаляет из БД данные
2. По дате не работает, потому что в БД складывается разные форматы'''

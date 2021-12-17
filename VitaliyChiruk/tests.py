from rss_reader import rss_read, parser_rss_line, printer, converter
import unittest
import sys
import os.path


class RSSReaderTests(unittest.TestCase):

    def test_create_parse(self):
        """function checks the values of the variables"""
        parsed = rss_read.create_parse().parse_args(["https://habr.com/rss/", "--json", "--limit", "3"])
        args_list = [parsed.source, parsed.json, parsed.limit]
        self.assertEqual(args_list, ["https://habr.com/rss/", True, 3])


class ParserRSSTests(unittest.TestCase):

    def test_db(self):
        data = [{"title": "a", "date": "2001-12-15", "link": "https://", "description": ""}]
        parser_rss_line.cache(data)
        parser_rss_line.read_news("2001-12-15")
        self.assertEqual(parser_rss_line.read_news("2001-12-15"), data)

    def test_parser(self):
        url = "https://news.yahoo.com/rss/"
        self.assertTrue(parser_rss_line.parser(url, 1))
        self.assertEqual(parser_rss_line.parser(url, 0), [])
        self.assertEqual(len(parser_rss_line.parser(url, 2)), 2)

        wrong_url = "https://habr.com/rs"
        temp = sys.stdout
        sys.stdout = open("test.txt", "w")
        parser_rss_line.parser(wrong_url, 1)
        sys.stdout.close()
        sys.stdout = temp
        with open("test.txt", "r") as f:
            text = f.readline()
        self.assertEqual(text, "Error URL or not RSS, please enter right URL\n")

        self.assertFalse(parser_rss_line.parser(wrong_url, 1))
        self.assertIsInstance(parser_rss_line.parser(url, 2), list)

        lst = parser_rss_line.parser(url, 2)
        self.assertIsInstance(lst[0], dict)


class PrinterTests(unittest.TestCase):

    def test_print_data(self):
        data = [{"title": "a", "date": "2001-12-15", "link": "https://", "description": ""}]
        temp = sys.stdout
        sys.stdout = open("test.txt", "w")
        printer.print_data(data)
        sys.stdout.close()
        sys.stdout = temp
        with open("test.txt", "r") as f:
            f.readline()
            f.readline()
            text = f.readline()
        self.assertIsInstance(text, str)
        self.assertEqual(text, "Title: a\n")


class ConverterTests(unittest.TestCase):

    def test_convert_pdf(self):
        """function check created PDF-file"""
        app_path = os.path.dirname(__file__)
        data = [{"Title": "1", "Date": "2", "Link": "3", "Description": "4"}]
        converter.convert_to_pdf(data, app_path)
        file = os.path.join(app_path, "RSS_Reader.pdf")
        self.assertTrue(os.path.exists(file))
        os.remove(file)  # delete file

    def test_convert_html(self):
        """function check created html-file"""
        app_path = os.path.dirname(__file__)
        data = [{"Title": "1", "Date": "2", "Link": "3", "Description": "4"}]
        converter.convert_to_html(data, app_path)
        file = os.path.join(app_path, "RSS_Reader.html")
        self.assertTrue(os.path.exists(file))
        os.remove(file)  # delete file


if __name__ == "__main__":
    unittest.main()

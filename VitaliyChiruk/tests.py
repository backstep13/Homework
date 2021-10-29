from rss_reader import rss_reader
import unittest
import xml.dom.minidom
import json
import sys
import os.path


class RSSTests(unittest.TestCase):

    def test_create_parse(self):
        """function checks the values of the variables"""
        parsed = rss_reader.create_parse().parse_args(["https://habr.com/rss/", "--json", "--limit", "3"])
        args_list = [parsed.source, parsed.json, parsed.verbose, parsed.limit]
        self.assertEqual(args_list, ["https://habr.com/rss/", True, False, 3])

    def test_get_data(self):
        """function checks format data from URL"""
        url = "https://news.yahoo.com/rss/"
        self.assertTrue(rss_reader.get_data(url, None, None))
        self.assertIsInstance(rss_reader.get_data(url, None, None), xml.dom.minidom.Document)

    def test_HTTPError(self):
        """Function checks exception if entered wrong URL"""
        wrong_url = "https://habr.com/rs"
        temp = sys.stdout
        sys.stdout = open("test.txt", "w")
        rss_reader.get_data(wrong_url, None, None)
        sys.stdout.close()
        sys.stdout = temp
        with open("test.txt", "r") as f:
            text = f.readline()
        self.assertEqual(text, "ERROR: Wrong url, check the url address\n")

    def test_invalid_data(self):
        """Function checks exception if URL return not xml data,
        creates file test.txt for reading stdout"""
        not_rss = "https://habr.com/"
        temp = sys.stdout
        sys.stdout = open("test.txt", "w")
        rss_reader.get_data(not_rss, None, None)
        sys.stdout.close()
        sys.stdout = temp
        with open("test.txt", "r") as f:
            text = f.readline()
        self.assertEqual(text, "ERROR: Invalid data\n")

    def test_print_json(self):
        """Function checks format data if json argument provided"""
        data = rss_reader.print_data("1", "2", "3", "4", json_type=True)
        self.assertTrue(json.loads(data))

    def test_print_data(self):
        """Function checks the receipt of data"""
        data = rss_reader.print_data("1", "2", "3", "4")
        self.assertIsInstance(data, str)

    def test_output_data_wrong_limit(self):
        """Function checks exception if entered wrong limit numbers,
        creates file test.txt for reading stdout"""
        dom = rss_reader.get_data("https://habr.com/rss/", None, None)
        temp = sys.stdout
        sys.stdout = open("test.txt", "w")
        rss_reader.output_data("https://habr.com/rss/", dom, -1)
        sys.stdout.close()
        sys.stdout = temp
        with open("test.txt", "r") as f:
            f.readline()  # skip print "Feed:"
            f.readline()
            text = f.readline()
        self.assertEqual(text, "ERROR: wrong limit number\n")

    def test_output_data_with_limit(self):
        """Function checks limit number,
        creates file test.txt for reading stdout"""
        dom = rss_reader.get_data("https://habr.com/rss/", None, None)
        temp = sys.stdout
        sys.stdout = open("test.txt", "w")
        rss_reader.output_data("https://habr.com/rss/", dom, 3)
        sys.stdout.close()
        sys.stdout = temp
        with open("test.txt", "r") as f:
            lst = f.read().split()
        self.assertEqual(lst.count("Title:"), 3)

    def test_verbose(self):
        """Function checks verbose mode,
        creates file test.txt for reading stdout"""
        temp = sys.stdout
        sys.stdout = open("test.txt", "w")
        rss_reader.get_data("https://habr.com/rss/", None, None, verbose=True)
        sys.stdout.close()
        sys.stdout = temp
        with open("test.txt", "r") as f:
            text = f.readline()
        self.assertIn("--->", text)

    def test_time_format(self):
        """Function checks format date for compare with command line argument"""
        time = "Sun, 24 Oct 2021 16:30:41 GMT"
        string = rss_reader.time_format(time)
        self.assertEqual(string, "2021-10-24")

    def test_check_unique(self):
        """Function checks unique and not unique data with storage"""
        json_dict = {"data": [
            {
                "Feed": "https://habr.com/rss/",
                "Title": "My_title",
                "Date": "2021-10-24",
                "Link": "https://habr.com/ru/post/585208",
                "Description": "My_description"
            }]}
        check_data1 = {
            "Feed": "https://habr.com/rss/",
            "Title": "My_title",
            "Date": "2021-10-24",
            "Link": "https://habr.com/ru/post/585208",
            "Description": "My_description"
        }
        check_data2 = {
            "Feed": "https://habr.com/rss/",
            "Title": "My_title",
            "Date": "2021-10-24",
            "Link": "https://habr.com/ru/post/585209",
            "Description": "My_description"
        }
        self.assertEqual(rss_reader.check_unique(json_dict, check_data1), None)
        self.assertEqual(rss_reader.check_unique(json_dict, check_data2), check_data2)

    def test_convert_pdf(self):
        """function check created PDF-file"""
        app_path = os.path.dirname(__file__)
        data = [{"Title": "1", "Date": "2", "Link": "3", "Description": "4"}]
        rss_reader.convert("PDF", app_path, data)
        file = os.path.join(app_path, "RSS_Reader.pdf")
        self.assertTrue(os.path.exists(file))
        os.remove(file)  # delete file

    def test_convert_html(self):
        """function check created html-file"""
        app_path = os.path.dirname(__file__)
        data = [{"Title": "1", "Date": "2", "Link": "3", "Description": "4"}]
        rss_reader.convert("HTML", app_path, data)
        file = os.path.join(app_path, "RSS_Reader.html")
        self.assertTrue(os.path.exists(file))
        os.remove(file)  # delete file


if __name__ == "__main__":
    unittest.main()

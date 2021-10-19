from rss_reader import rss_reader
import unittest
import xml.dom.minidom
import json
import sys


class RSSTests(unittest.TestCase):

    def test_create_parse(self):
        """function checks the values of the variables"""
        parsed = rss_reader.create_parse().parse_args(['https://habr.com/rss/', '--json', '--limit', '3'])
        args_list = [parsed.source, parsed.json, parsed.verbose, parsed.limit]
        self.assertEqual(args_list, ['https://habr.com/rss/', True, False, 3])

    def test_get_data(self):
        """function checks format data from URL"""
        url = 'https://news.yahoo.com/rss/'
        self.assertTrue(rss_reader.get_data(url))
        self.assertIsInstance(rss_reader.get_data(url), xml.dom.minidom.Document)

    def test_HTTPError(self):
        """Function checks exception if entered wrong URL"""
        wrong_url = 'https://habr.com/rs'
        temp = sys.stdout
        sys.stdout = open('test.txt', 'w')
        rss_reader.get_data(wrong_url)
        sys.stdout.close()
        sys.stdout = temp
        with open('test.txt', 'r') as f:
            text = f.readline()
        self.assertEqual(text, 'ERROR: Wrong url, check the url address\n')

    def test_invalid_data(self):
        """Function checks exception if URL return not xml data,
        creates file test.txt for reading stdout"""
        not_rss = 'https://habr.com/'
        temp = sys.stdout
        sys.stdout = open('test.txt', 'w')
        rss_reader.get_data(not_rss)
        sys.stdout.close()
        sys.stdout = temp
        with open('test.txt', 'r') as f:
            text = f.readline()
        self.assertEqual(text, 'ERROR: Invalid data\n')

    def test_print_json(self):
        """Function checks format data if json argument provided"""
        data = rss_reader.print_data('1', '2', '3', '4', json_type=True)
        self.assertTrue(json.loads(data))

    def test_print_data(self):
        """Function checks the receipt of data"""
        data = rss_reader.print_data('1', '2', '3', '4')
        self.assertIsInstance(data, str)

    def test_output_data_wrong_limit(self):
        """Function checks exception if entered wrong limit numbers,
        creates file test.txt for reading stdout"""
        dom = rss_reader.get_data('https://habr.com/rss/')
        temp = sys.stdout
        sys.stdout = open('test.txt', 'w')
        rss_reader.output_data(dom, -1)
        sys.stdout.close()
        sys.stdout = temp
        with open('test.txt', 'r') as f:
            f.readline()  # skip print "Feed:"
            f.readline()
            text = f.readline()
        self.assertEqual(text, 'ERROR: wrong limit number\n')

    def test_output_data_with_limit(self):
        """Function checks limit number,
        creates file test.txt for reading stdout"""
        dom = rss_reader.get_data('https://habr.com/rss/')
        temp = sys.stdout
        sys.stdout = open('test.txt', 'w')
        rss_reader.output_data(dom, 3)
        sys.stdout.close()
        sys.stdout = temp
        with open('test.txt', 'r') as f:
            lst = f.read().split()
        self.assertEqual(lst.count("Title:"), 3)

    def test_verbose(self):
        """Function checks verbose mode,
        creates file test.txt for reading stdout"""
        temp = sys.stdout
        sys.stdout = open('test.txt', 'w')
        rss_reader.get_data('https://habr.com/rss/', verbose=True)
        sys.stdout.close()
        sys.stdout = temp
        with open('test.txt', 'r') as f:
            text = f.readline()
        self.assertIn("--->", text)


if __name__ == "__main__":
    unittest.main()  # cover 76%
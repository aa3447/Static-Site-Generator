import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        html1 = HTMLNode("a", "asdas", None, {"href": "https://www.google.com", "target": "_blank", })
        self.assertEqual(html1.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_props_to_html_empty(self):
        html1 = HTMLNode("a", "asdas", None, {})
        self.assertEqual(html1.props_to_html(), "")
    
    def test_props_to_html_no_prop(self):
        html1 = HTMLNode("a", "asdas", None, None)
        self.assertEqual(html1.props_to_html(), "")

if __name__ == "__main__":
    unittest.main()
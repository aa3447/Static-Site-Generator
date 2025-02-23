import unittest

from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_to_html(self):
        leaf_node = LeafNode("p", "Goodbye")
        self.assertEqual(leaf_node.to_html(), "<p>Goodbye</p>")
    
    def test_to_html_props(self):
        leaf_node = LeafNode("a", "Hello",{"href": "https://www.google.com"})
        self.assertEqual(leaf_node.to_html(), '<a href="https://www.google.com">Hello</a>')

    def test_to_html_multi_props(self):
        leaf_node = LeafNode("a", "Hola",{"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(leaf_node.to_html(), '<a href="https://www.google.com" target="_blank">Hola</a>')

    def test_to_html_no_tag(self):
        leaf_node = LeafNode(None, "Goodbye")
        self.assertEqual(leaf_node.to_html(), "Goodbye")
    
    def test_to_html_no_value(self):
        leaf_node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            leaf_node.to_html()

if __name__ == "__main__":
    unittest.main()
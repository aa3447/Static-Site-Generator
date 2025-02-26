import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_to_html(self):
        parent_node = ParentNode("div", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text")])
        self.assertEqual(parent_node.to_html(), "<div><b>Bold text</b>Normal text</div>")
    
    def test_to_html_inside_parent(self):
        parent_node_inside = ParentNode("parent", [LeafNode("a", "Inside Link", {"href": "https://www.google.com"}), LeafNode(None, "Indside Normal text")])
        parent_node = ParentNode("div", [LeafNode(None, "Normal text"),parent_node_inside,LeafNode("i", "italic text")])
        self.assertEqual(parent_node.to_html(), '<div>Normal text<parent><a href="https://www.google.com">Inside Link</a>Indside Normal text</parent><i>italic text</i></div>')

    def test_to_html_nested_parent(self):
        parent_node_inside_nested = ParentNode("inside", [LeafNode("a", "Inside Link", {"href": "https://www.google.com"})])
        parent_node_nested = ParentNode("nested", [ LeafNode(None, "Normal text"), parent_node_inside_nested ,LeafNode("i", "italic text")])
        parent_node_top = ParentNode("top", [LeafNode("b", "Top text"), parent_node_nested, LeafNode(None, "Normal text")])
        self.assertEqual(parent_node_top.to_html(), '<top><b>Top text</b><nested>Normal text<inside><a href="https://www.google.com">Inside Link</a></inside><i>italic text</i></nested>Normal text</top>')

    def test_to_html_no_tag(self):
        parent_node = ParentNode(None, [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"),LeafNode("i", "italic text"), LeafNode(None, "Normal text")])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_no_children(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()

if __name__ == "__main__":
    unittest.main()
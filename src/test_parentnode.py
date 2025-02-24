import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_to_html(self):
        parent_node = ParentNode("div", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"),LeafNode("i", "italic text"), LeafNode(None, "Normal text")])
        self.assertEqual(parent_node.to_html(), "<div><b>Bold text</b>Normal text<i>italic text</i>Normal text</div>")
    
    def test_to_html_inside_parent(self):
        parent_node_inside = ParentNode("parent", [LeafNode("a", "Inside Link", {"href": "https://www.google.com"}), LeafNode(None, "Indside Normal text")])
        parent_node = ParentNode("div", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"),parent_node_inside,LeafNode("i", "italic text"), LeafNode(None, "Normal text")])
        self.assertEqual(parent_node.to_html(), '<div><b>Bold text</b>Normal text<parent><a href="https://www.google.com">Inside Link</a>Indside Normal text</parent><i>italic text</i>Normal text</div>')

    def test_to_html_nested_parent(self):
        parent_node_inside = ParentNode("inside", [LeafNode("a", "Inside Link", {"href": "https://www.google.com"}), LeafNode(None, "Indside Normal text")])
        parent_node_nested = ParentNode("nested", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"),parent_node_inside,LeafNode("i", "italic text"), LeafNode(None, "Normal text")])
        parent_node_top = ParentNode("top", [LeafNode("b", "Top text"), parent_node_nested])
        self.assertEqual(parent_node_top.to_html(), '<top><b>Top text</b><nested><b>Bold text</b>Normal text<inside><a href="https://www.google.com">Inside Link</a>Indside Normal text</inside><i>italic text</i>Normal text</nested></top>')

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
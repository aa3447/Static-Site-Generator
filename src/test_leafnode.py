import unittest

from leafnode import LeafNode
from textnode import TextNode, TextType


class TestLeafNode(unittest.TestCase):
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

    def test_text_node_to_leaf_node_normal(self):
        text_node = TextNode("Testing Normal!", TextType.NORMAL)
        leaf_node = LeafNode.text_node_to_leaf_node(text_node)
        self.assertIsInstance(leaf_node, LeafNode)
        self.assertEqual(leaf_node.to_html(), "Testing Normal!")

    def test_text_node_to_leaf_node_bold(self):
        text_node = TextNode("Testing Bold!", TextType.BOLD)
        leaf_node = LeafNode.text_node_to_leaf_node(text_node)
        self.assertIsInstance(leaf_node, LeafNode)
        self.assertEqual(leaf_node.to_html(), "<b>Testing Bold!</b>")

    def test_text_node_to_leaf_node_italic(self):
        text_node = TextNode("Testing Italic!", TextType.ITALIC)
        leaf_node = LeafNode.text_node_to_leaf_node(text_node)
        self.assertIsInstance(leaf_node, LeafNode)
        self.assertEqual(leaf_node.to_html(), "<i>Testing Italic!</i>")

    def test_text_node_to_leaf_node_code(self):
        text_node = TextNode("Testing Code!", TextType.CODE)
        leaf_node = LeafNode.text_node_to_leaf_node(text_node)
        self.assertIsInstance(leaf_node, LeafNode)
        self.assertEqual(leaf_node.to_html(), "<code>Testing Code!</code>")
    
    def test_text_node_to_leaf_node_link(self):
        text_node = TextNode("Testing Link!", TextType.LINK, "https://www.google.com")
        leaf_node = LeafNode.text_node_to_leaf_node(text_node)
        self.assertIsInstance(leaf_node, LeafNode)
        self.assertEqual(leaf_node.to_html(), '<a href="https://www.google.com">Testing Link!</a>')

    def test_text_node_to_leaf_node_image(self):
        text_node = TextNode("Testing Image!", TextType.IMAGE, "https://www.google.com")
        leaf_node = LeafNode.text_node_to_leaf_node(text_node)
        self.assertIsInstance(leaf_node, LeafNode)
        self.assertEqual(leaf_node.to_html(), '<img src="https://www.google.com" alt="Testing Image!"></img>')

    def test_text_node_to_leaf_node_invalid(self):
        text_node = TextNode("Testing Invalid!", "invalid")
        with self.assertRaises(ValueError):
            LeafNode.text_node_to_leaf_node(text_node)

if __name__ == "__main__":
    unittest.main()
import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://google.com")
        self.assertEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "https://google.com")
        self.assertNotEqual(node, node2)
    
    def test_not_eq_Type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.NORMAL)
        self.assertNotEqual(node, node2)

    def test_not_eq_Text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a node of text", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_split_nodes_delimiter_bold(self):
        text_node_splitter = TextNode("", TextType.NORMAL)
        text_node2 = TextNode("This is a **test** for split nodes", TextType.NORMAL)
        text_node_split_bold = text_node_splitter.split_nodes_delimiter([text_node2], "**", TextType.BOLD)
        self.assertEqual(text_node_split_bold, [TextNode("This is a ", TextType.NORMAL), TextNode("test", TextType.BOLD), TextNode(" for split nodes", TextType.NORMAL)])

    def test_split_nodes_delimiter_italic(self):
        text_node_splitter = TextNode("", TextType.NORMAL)
        text_node2 = TextNode("This is a *test* for split nodes", TextType.NORMAL)
        text_node_split_bold = text_node_splitter.split_nodes_delimiter([text_node2], "*", TextType.ITALIC)
        self.assertEqual(text_node_split_bold, [TextNode("This is a ", TextType.NORMAL), TextNode("test", TextType.ITALIC), TextNode(" for split nodes", TextType.NORMAL)])
    
    def test_split_nodes_delimiter_code(self):
        text_node_splitter = TextNode("", TextType.NORMAL)
        text_node2 = TextNode("This is a ```test``` for split nodes", TextType.NORMAL)
        text_node_split_bold = text_node_splitter.split_nodes_delimiter([text_node2], "```", TextType.CODE)
        self.assertEqual(text_node_split_bold, [TextNode("This is a ", TextType.NORMAL), TextNode("test", TextType.CODE), TextNode(" for split nodes", TextType.NORMAL)])
    
    def test_split_nodes_delimiter_leftmost_bold(self):
        text_node_splitter = TextNode("", TextType.NORMAL)
        text_node2 = TextNode("**This** is a test for split nodes", TextType.NORMAL)
        text_node_split_bold = text_node_splitter.split_nodes_delimiter([text_node2], "**", TextType.BOLD)
        self.assertEqual(text_node_split_bold, [TextNode("This", TextType.BOLD), TextNode(" is a test for split nodes", TextType.NORMAL)])

    def test_split_nodes_delimiter_rightmost_bold(self):
        text_node_splitter = TextNode("", TextType.NORMAL)
        text_node2 = TextNode("This is a test for split **nodes**", TextType.NORMAL)
        text_node_split_bold = text_node_splitter.split_nodes_delimiter([text_node2], "**", TextType.BOLD)
        self.assertEqual(text_node_split_bold, [TextNode("This is a test for split ", TextType.NORMAL), TextNode("nodes", TextType.BOLD)])

    def test_split_nodes_delimiter_multi(self):
        text_node_splitter = TextNode("", TextType.NORMAL)
        text_node2 = TextNode("This is a **test** for ```split``` nodes", TextType.NORMAL)
        text_node3 = TextNode("This ```is``` a test for **split nodes**", TextType.NORMAL)
        text_node_split_bold = text_node_splitter.split_nodes_delimiter([text_node2, text_node3], "**", TextType.BOLD)
        text_node_split_italic = text_node_splitter.split_nodes_delimiter(text_node_split_bold, "```", TextType.ITALIC)
        self.assertEqual(text_node_split_italic, [TextNode("This is a ", TextType.NORMAL), TextNode("test", TextType.BOLD), TextNode(" for ", TextType.NORMAL), TextNode("split", TextType.ITALIC), TextNode(" nodes", TextType.NORMAL), TextNode("This ", TextType.NORMAL), TextNode("is", TextType.ITALIC), TextNode(" a test for ", TextType.NORMAL), TextNode("split nodes", TextType.BOLD)])

    

if __name__ == "__main__":
    unittest.main()
import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("node", TextType.BOLD)
        node2 = TextNode("node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("node", TextType.BOLD, "https://google.com")
        node2 = TextNode("node", TextType.BOLD, "https://google.com")
        self.assertEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("node", TextType.BOLD)
        node2 = TextNode("Yall", TextType.BOLD, "https://google.com")
        self.assertNotEqual(node, node2)
    
    def test_not_eq_Type(self):
        node = TextNode("node", TextType.BOLD)
        node2 = TextNode("node", TextType.NORMAL)
        self.assertNotEqual(node, node2)

    def test_not_eq_Text(self):
        node = TextNode("node", TextType.BOLD)
        node2 = TextNode("Yall", TextType.BOLD)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
import unittest

from textnode import TextNode, TextType
from textnodesplitter import TextNodeSplitter

class TestTextNodeSplitter(unittest.TestCase):

    # Test cases for split_nodes_delimiter
    def test_split_nodes_delimiter_bold(self):
        bold_node = TextNode("This is a **test** for split nodes", TextType.NORMAL)
        text_node_split_bold = TextNodeSplitter.split_nodes_delimiter([bold_node], "**", TextType.BOLD)
        self.assertEqual(text_node_split_bold, [TextNode("This is a ", TextType.NORMAL), TextNode("test", TextType.BOLD), TextNode(" for split nodes", TextType.NORMAL)])

    def test_split_nodes_delimiter_italic(self):
        italic_node = TextNode("This is a *test* for split nodes", TextType.NORMAL)
        text_node_split_italic = TextNodeSplitter.split_nodes_delimiter([italic_node], "*", TextType.ITALIC)
        self.assertEqual(text_node_split_italic, [TextNode("This is a ", TextType.NORMAL), TextNode("test", TextType.ITALIC), TextNode(" for split nodes", TextType.NORMAL)])
    
    def test_split_nodes_delimiter_code(self):
        code_node = TextNode("This is a ```test``` for split nodes", TextType.NORMAL)
        text_node_split_code = TextNodeSplitter.split_nodes_delimiter([code_node], "```", TextType.CODE)
        self.assertEqual(text_node_split_code, [TextNode("This is a ", TextType.NORMAL), TextNode("test", TextType.CODE), TextNode(" for split nodes", TextType.NORMAL)])
    
    def test_split_nodes_delimiter_leftmost_bold(self):
        left_node = TextNode("**This** is a test for split nodes", TextType.NORMAL)
        text_node_split_bold = TextNodeSplitter.split_nodes_delimiter([left_node], "**", TextType.BOLD)
        self.assertEqual(text_node_split_bold, [TextNode("This", TextType.BOLD), TextNode(" is a test for split nodes", TextType.NORMAL)])

    def test_split_nodes_delimiter_rightmost_bold(self):
        right_node2 = TextNode("This is a test for split **nodes**", TextType.NORMAL)
        text_node_split_bold = TextNodeSplitter.split_nodes_delimiter([right_node2], "**", TextType.BOLD)
        self.assertEqual(text_node_split_bold, [TextNode("This is a test for split ", TextType.NORMAL), TextNode("nodes", TextType.BOLD)])

    def test_split_nodes_delimiter_multi(self):
        text_code = TextNode("This is a ```test``` for ```code``` nodes", TextType.NORMAL)
        text_bold = TextNode("This **is** a test for **bold** nodes", TextType.NORMAL)
        text_node_split_bold = TextNodeSplitter.split_nodes_delimiter([text_code, text_bold], "**", TextType.BOLD)
        text_node_split_code = TextNodeSplitter.split_nodes_delimiter(text_node_split_bold, "```", TextType.CODE)
        self.assertEqual(text_node_split_code, [TextNode("This is a ", TextType.NORMAL), TextNode("test", TextType.CODE), TextNode(" for ", TextType.NORMAL), TextNode("code", TextType.CODE), TextNode(" nodes", TextType.NORMAL), 
                                                TextNode("This ", TextType.NORMAL), TextNode("is", TextType.BOLD), TextNode(" a test for ", TextType.NORMAL), TextNode("bold", TextType.BOLD), TextNode(" nodes", TextType.NORMAL)])
        
    def test_split_nodes_mixed_delimiter(self):
        text_bold = TextNode("This is a ```test``` for **bold** nodes", TextType.NORMAL)
        text_node_split_bold = TextNodeSplitter.split_nodes_delimiter([text_bold], "**", TextType.BOLD)
        self.assertEqual(text_node_split_bold, [TextNode("This is a ```test``` for ", TextType.NORMAL),  TextNode("bold", TextType.BOLD), TextNode(" nodes", TextType.NORMAL)])

    def test_split_nodes_mixed_delimiter_multi(self):
        text_code = TextNode("This is a ```test``` for **code** nodes", TextType.NORMAL)
        text_bold = TextNode("This is a **test** for ```bold``` nodes", TextType.NORMAL)
        text_node_split_bold = TextNodeSplitter.split_nodes_delimiter([text_code, text_bold], "**", TextType.BOLD)
        text_node_split_code = TextNodeSplitter.split_nodes_delimiter(text_node_split_bold, "```", TextType.CODE)
        self.assertEqual(text_node_split_code, [TextNode("This is a ", TextType.NORMAL), TextNode("test", TextType.CODE), TextNode(" for ", TextType.NORMAL), TextNode("code", TextType.BOLD), TextNode(" nodes", TextType.NORMAL),
                                                TextNode("This is a ", TextType.NORMAL), TextNode("test", TextType.BOLD), TextNode(" for ", TextType.NORMAL), TextNode("bold", TextType.CODE), TextNode(" nodes", TextType.NORMAL)])
        
    # Test cases for extract_markdown_images
    def test_extract_markdown_images(self):
        test_markdown_images = TextNodeSplitter.extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)")
        self.assertEqual(test_markdown_images, [("rick roll", "https://i.imgur.com/aKaOqIh.gif")])

    def test_extract_markdown_images_multi(self):
        test_markdown_images = TextNodeSplitter.extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        self.assertEqual(test_markdown_images, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])
    
    def test_extract_markdown_images_no_images(self):
        test_markdown_images = TextNodeSplitter.extract_markdown_images("This is text with no images")
        self.assertEqual(test_markdown_images, [])

    def test_extract_markdown_images_empty_alt_text(self):
        test_markdown_images = TextNodeSplitter.extract_markdown_images("This is text with a ![](https://i.imgur.com/aKaOqIh.gif)")
        self.assertEqual(test_markdown_images, [("", "https://i.imgur.com/aKaOqIh.gif")])
    
    def test_extract_markdown_images_empty_url(self):
        test_markdown_images = TextNodeSplitter.extract_markdown_images("This is text with a ![rick roll]()")
        self.assertEqual(test_markdown_images, [])

    # Test cases for extract_markdown_links
    def test_extract_markdown_links(self):
        test_markdown_links = TextNodeSplitter.extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev)")
        self.assertEqual(test_markdown_links, [("to boot dev", "https://www.boot.dev")])
    
    def test_extract_markdown_links_multi(self):
        test_markdown_links = TextNodeSplitter.extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertEqual(test_markdown_links, [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])
    
    def test_extract_markdown_links_no_links(self):
        test_markdown_links = TextNodeSplitter.extract_markdown_links("This is text with no links")
        self.assertEqual(test_markdown_links, [])
    
    def test_extract_markdown_empty_link_text(self):
        test_markdown_links = TextNodeSplitter.extract_markdown_links("This is text with a link [](https://www.boot.dev)")
        self.assertEqual(test_markdown_links, [("", "https://www.boot.dev")])

    def test_extract_markdown_links_not_preceded_by_exclamation_mark(self):
        test_markdown_links = TextNodeSplitter.extract_markdown_links("This is text with a link ![to boot dev](https://www.boot.dev)")
        self.assertEqual(test_markdown_links, [])
    
    def test_extract_markdown_empty_link_url(self):
        test_markdown_links = TextNodeSplitter.extract_markdown_links("This is text with a link [to boot dev]()")
        self.assertEqual(test_markdown_links, [])

    # Test cases for split_nodes_image
    def test_split_node_images(self):
        test_markdown_images = TextNodeSplitter.split_nodes_image([TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",TextType.NORMAL)])
        self.assertEqual(test_markdown_images, [TextNode("This is text with an ", TextType.NORMAL), TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")])
    
    def test_split_node_images_multi(self):
        test_markdown_images = TextNodeSplitter.split_nodes_image([TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![image](https://i.imgur.com/zjjcJKZ.png)",TextType.NORMAL)])
        self.assertEqual(test_markdown_images, [TextNode("This is text with an ", TextType.NORMAL), TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"), TextNode(" and another ", TextType.NORMAL),
                                                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")])
    def test_split_node_images_middle(self):
        test_markdown_images = TextNodeSplitter.split_nodes_image([TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) in the middle",TextType.NORMAL)])
        self.assertEqual(test_markdown_images, [TextNode("This is text with an ", TextType.NORMAL), TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"), TextNode(" in the middle", TextType.NORMAL)])
    
    def test_split_node_images_leftmost(self):
        test_markdown_images = TextNodeSplitter.split_nodes_image([TextNode("![image](https://i.imgur.com/zjjcJKZ.png) on the left",TextType.NORMAL)])
        self.assertEqual(test_markdown_images, [TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"), TextNode(" on the left", TextType.NORMAL)])
    
    def test_split_node_images_missing_alt_text(self):
        test_markdown_images = TextNodeSplitter.split_nodes_image([TextNode("This is text with an ![](https://i.imgur.com/zjjcJKZ.png)",TextType.NORMAL)])
        self.assertEqual(test_markdown_images, [TextNode("This is text with an ", TextType.NORMAL), TextNode("", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")])
    
    def test_split_node_images_missing_url(self):
        test_markdown_images = TextNodeSplitter.split_nodes_image([TextNode("This is text with an ![image]()",TextType.NORMAL)])
        self.assertEqual(test_markdown_images, [TextNode("This is text with an ![image]()", TextType.NORMAL)])

    def test_split_node_images_missing_alt_text_and_url(self):
        test_markdown_images = TextNodeSplitter.split_nodes_image([TextNode("This is text with an ![]()",TextType.NORMAL)])
        self.assertEqual(test_markdown_images, [TextNode("This is text with an ![]()", TextType.NORMAL)])
        
    def test_split_node_images_with_space(self):
        test_markdown_images = TextNodeSplitter.split_nodes_image([TextNode("This is text with an ![image] (https://i.imgur.com/zjjcJKZ.png))",TextType.NORMAL)])
        self.assertEqual(test_markdown_images, [TextNode("This is text with an ![image] (https://i.imgur.com/zjjcJKZ.png))", TextType.NORMAL)])

    # Test cases for split_nodes_link
    def test_split_node_links(self):
        test_markdown_links = TextNodeSplitter.split_nodes_link([TextNode("This is text with a [link](https://www.boot.dev)",TextType.NORMAL)])
        self.assertEqual(test_markdown_links, [TextNode("This is text with a ", TextType.NORMAL), TextNode("link", TextType.LINK, "https://www.boot.dev")])
    
    def test_split_node_links_multi(self):
        test_markdown_links = TextNodeSplitter.split_nodes_link([TextNode("This is text with a [link](https://www.boot.dev) and another [link](https://www.youtube.com/@bootdotdev)",TextType.NORMAL)])
        self.assertEqual(test_markdown_links, [TextNode("This is text with a ", TextType.NORMAL), TextNode("link", TextType.LINK, "https://www.boot.dev"), TextNode(" and another ", TextType.NORMAL),
                                                TextNode("link", TextType.LINK, "https://www.youtube.com/@bootdotdev")])
        
    def test_split_node_links_middle(self):
        test_markdown_links = TextNodeSplitter.split_nodes_link([TextNode("This is text with a [link](https://www.boot.dev) in the middle",TextType.NORMAL)])
        self.assertEqual(test_markdown_links, [TextNode("This is text with a ", TextType.NORMAL), TextNode("link", TextType.LINK, "https://www.boot.dev"), TextNode(" in the middle", TextType.NORMAL)])

    def test_split_node_links_leftmost(self):
        test_markdown_links = TextNodeSplitter.split_nodes_link([TextNode("[link](https://www.boot.dev) on the left",TextType.NORMAL)])
        self.assertEqual(test_markdown_links, [TextNode("link", TextType.LINK, "https://www.boot.dev"), TextNode(" on the left", TextType.NORMAL)])
    
    def test_split_node_links_missing_link_text(self):
        test_markdown_links = TextNodeSplitter.split_nodes_link([TextNode("This is text with a [](https://i.imgur.com/zjjcJKZ.png)",TextType.NORMAL)])
        self.assertEqual(test_markdown_links, [TextNode("This is text with a ", TextType.NORMAL), TextNode("", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png")])
    
    def test_split_node_links_missing_url(self):
        test_markdown_links = TextNodeSplitter.split_nodes_link([TextNode("This is text with a [link]()",TextType.NORMAL)])
        self.assertEqual(test_markdown_links, [TextNode("This is text with a [link]()", TextType.NORMAL)])
    
    def test_split_node_links_missing_link_text_and_url(self):
        test_markdown_links = TextNodeSplitter.split_nodes_link([TextNode("This is text with a []()",TextType.NORMAL)])
        self.assertEqual(test_markdown_links, [TextNode("This is text with a []()", TextType.NORMAL)])
    
    def test_split_node_links_with_space(self):
        test_markdown_links = TextNodeSplitter.split_nodes_link([TextNode("This is text with a [link] (https://www.boot.dev)",TextType.NORMAL)])
        self.assertEqual(test_markdown_links, [TextNode("This is text with a [link] (https://www.boot.dev)", TextType.NORMAL)])
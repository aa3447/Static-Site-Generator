from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from textnodesplitter import TextNodeSplitter

def main():
    text_node = TextNode("Testing!", TextType.BOLD, "https://google.com")
    print(f"This is a Text Node: {text_node}")
    html_node = HTMLNode("a","asdas",None, {"href": "https://www.google.com","target": "_blank",})
    print(f"This is a HTML Node: {html_node}")
    print(html_node.props_to_html())
    leaf_node = LeafNode("a", "Hello",{"href": "https://www.google.com"})
    print(f"This is a Leaf Node: {leaf_node}")
    parent_node = ParentNode("div", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"),LeafNode("i", "italic text"), LeafNode(None, "Normal text")])
    print(f"This is a Parent Node: {parent_node}")

    text_node2 = TextNode("This is a **test** for `split` nodes", TextType.NORMAL)
    text_node_split_bold = TextNodeSplitter.split_nodes_delimiter([text_node2], "**", TextType.BOLD)
    print(f"This is a split TextNode On Bold: {text_node_split_bold}")

    test_markdown_images = TextNodeSplitter.extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
    print(test_markdown_images)
    test_markdown_links = TextNodeSplitter.extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
    print(test_markdown_links)

if __name__ == "__main__":
    main()
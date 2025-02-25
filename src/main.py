from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

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

    text_node_splitter = TextNode("", TextType.NORMAL)
    text_node2 = TextNode("This is a **test** for `split` nodes", TextType.NORMAL)
    text_node3 = TextNode("This `is` a test for **split nodes**", TextType.NORMAL)
    text_node_split_bold = text_node_splitter.split_nodes_delimiter([text_node2, text_node3], "**", TextType.BOLD)
    print(f"This is a split TextNode On Bold: {text_node_split_bold}")
    text_node_split_italic = text_node_splitter.split_nodes_delimiter(text_node_split_bold, "`", TextType.ITALIC)
    print(f"This is a split TextNode On Italic: {text_node_split_italic}")

if __name__ == "__main__":
    main()
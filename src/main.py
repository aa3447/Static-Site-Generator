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

if __name__ == "__main__":
    main()
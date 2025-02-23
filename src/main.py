from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode

def main():
    text_node = TextNode("Testing!", TextType.BOLD, "https://google.com")
    print(text_node)
    html_node = HTMLNode("a","asdas",None, {"href": "https://www.google.com","target": "_blank",})
    print(html_node)
    print(html_node.props_to_html())
    leaf_node = LeafNode("a", "Hello",{"href": "https://www.google.com"})
    print(leaf_node.to_html())

if __name__ == "__main__":
    main()
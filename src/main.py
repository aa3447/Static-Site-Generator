from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from textnodesplitter import TextNodeSplitter
from htmlmaker import HTMLMaker
from blocknode import BlockNode

def main():
    sample_markdown = """
```
1. ![alt text for image](url/of/image.jpg)
2. ![alt text for image](url/of/image.jpg)
```
"""
    html = HTMLMaker.markdown_to_html_node(sample_markdown)
    print(html.to_html())

if __name__ == "__main__":
    main()
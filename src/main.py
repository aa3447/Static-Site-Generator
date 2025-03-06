from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from textnodesplitter import TextNodeSplitter
from htmlmaker import HTMLMaker
from blocknode import BlockNode
from copystatictopublic import CopyStaticToPublic

def main():
    public_path = "./public"
    static_path = "./static"

    #html = HTMLMaker.markdown_to_html_node(sample_markdown)
    #print(html.to_html())

    copier = CopyStaticToPublic(public_path, static_path)
    copier.copy_static_to_public(public_path, static_path)




if __name__ == "__main__":
    main()
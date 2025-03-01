from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from textnodesplitter import TextNodeSplitter
import re
from blocknode import BlockNode

def main():
    block_types = []
    sample_markdown = """
# This is a heading
## This is a heading
### This is a heading
#### This is a heading
##### This is a heading
###### This is a heading
""" 
    blocks = BlockNode.markdown_to_blocks(sample_markdown)
    for block in blocks:
        block_types.append(BlockNode.block_to_block_type(block))
    print(block_types)

if __name__ == "__main__":
    main()
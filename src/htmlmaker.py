from blocknode import BlockNode , BlockType
from parentnode import ParentNode
from leafnode import LeafNode
from textnodesplitter import TextNodeSplitter
import re

class HTMLMaker:
    def __init__(self):
        pass

    def markdown_to_html_node(markdown):
        blocks = BlockNode.markdown_to_blocks(markdown)
        html_nodes = []
        for block in blocks:
            block_type = BlockNode.block_to_block_type(block)

            leaf_nodes = HTMLMaker.block_to_leaf_nodes(block, block_type)
            
            html_nodes.append(ParentNode(HTMLMaker.block_type_to_tag(block_type, block), leaf_nodes))
        
        return ParentNode("div", html_nodes)
    
    
    def block_to_leaf_nodes(block, block_type):
        new_block = block
        match block_type:
            case BlockType.HEADING:
                new_block = block.lstrip("#").lstrip()
            case BlockType.QUOTE:
                new_block = HTMLMaker.__quote_block_to_stripped_string(new_block)
            case BlockType.UNORDERED_LIST:
                new_block = HTMLMaker.__unorderd_list_block_to_stripped_string(new_block)
            case BlockType.ORDERED_LIST:
                new_block = HTMLMaker.__orderd_list_block_to_stripped_string(new_block)
            case BlockType.CODE:
                return HTMLMaker.__code_block_to_leaf_node(new_block)
        
        return HTMLMaker.__text_to_children(new_block)
    
    def __orderd_list_block_to_stripped_string(quote_block):
        split_newline_block = quote_block.splitlines()
        cleaned_lines = map(lambda line: f"<li>{re.sub(r"\d+. ","",line).lstrip()}</li>", split_newline_block)
        return "".join(cleaned_lines)
    
    def __unorderd_list_block_to_stripped_string(quote_block):
        split_newline_block = quote_block.splitlines()
        cleaned_lines = map(lambda line: f"<li>{line.removeprefix("-").lstrip()}</li>", split_newline_block)
        return "".join(cleaned_lines)
    
    def __quote_block_to_stripped_string(quote_block):
        split_newline_block = quote_block.splitlines()
        striped_block = map(lambda line: line.removeprefix(">").lstrip(), split_newline_block)
        return " ".join(striped_block)
    
    def __code_block_to_leaf_node(code_block):
        split_block = code_block.splitlines(True)
        if len(split_block) <= 1:
            return [LeafNode("code", "".join(split_block).removeprefix("```").removesuffix("```"))]
        return [LeafNode("code", "".join(split_block[1:-1]))]
    
    def __text_to_children(text):
        no_newline_text = text.replace("\n", " ")
        leaf_nodes = []
        text_nodes = TextNodeSplitter.text_to_textnodes(no_newline_text)
        for value in text_nodes:
            leaf_nodes.append(LeafNode.text_node_to_leaf_node(value))
        return leaf_nodes
    

    def block_type_to_tag(block_type, block):
        match block_type:
            case BlockType.PARAGRAPH:
                return "p"
            case BlockType.HEADING:
                return f"h{block.count('#', 0, 7)}"
            case BlockType.CODE:
                return "pre"
            case BlockType.QUOTE:
                return "blockquote"
            case BlockType.UNORDERED_LIST:
                return "ul"
            case BlockType.ORDERED_LIST:
                return "ol"
            case _:
                raise SyntaxError("Invalid Block Type")
            
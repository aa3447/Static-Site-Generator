from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


class BlockNode:
    def __init__(self):
        pass

    def markdown_to_blocks(markdown):
        single_line_blocks = markdown.split("\n\n")
        removed_whitepace_from_blocks = map(lambda block: block.strip(), single_line_blocks)
        filtered_empty_blocks = list(filter(lambda block: block != "", removed_whitepace_from_blocks))
        return filtered_empty_blocks
    
    # finding block type and helper functions
    def block_to_block_type(block):
        function_dict = {"#": BlockNode.__heading_match, "`": BlockNode.__code_match, ">": BlockNode.__quote_match, "-": BlockNode.__unordered_list_match, "1": BlockNode.__ordered_list_match}
        start_char = block[0]
        if not (start_char in function_dict):
            return BlockType.PARAGRAPH
        
        blocks = list(filter(lambda bl: bl !="", block.split("\n")))
        return function_dict[start_char](blocks)  
         
    
    def __heading_match(blocks):
        for sen in blocks:
            if not re.match(r"#{1,6} ", sen):
                return BlockType.PARAGRAPH

        return BlockType.HEADING
    
    def __code_match(blocks):
        if not (blocks[0].startswith("```") and blocks[-1].endswith("```")):
            return BlockType.PARAGRAPH
        
        return BlockType.CODE
    
    def __quote_match(blocks):
        for sen in blocks:
            if not sen.startswith(">"):
                return BlockType.PARAGRAPH
        
        return BlockType.QUOTE
    
    def __unordered_list_match(blocks):
        for sen in blocks:
            if not sen.startswith("- "):
                return BlockType.PARAGRAPH
        
        return BlockType.UNORDERED_LIST
    
    def __ordered_list_match(blocks):
        for num in range(1, len(blocks)+1):
            if not blocks[num-1].startswith(f"{num}. "):
                return BlockType.PARAGRAPH
        
        return BlockType.ORDERED_LIST
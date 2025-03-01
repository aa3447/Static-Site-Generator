import unittest

from blocknode import BlockNode, BlockType

class TestBlockNode(unittest.TestCase):

    # Test markdown_to_blocks
    def test_markdown_to_blocks(self):
        sample_markdown = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
    """
        blocks = BlockNode.markdown_to_blocks(sample_markdown)
        self.assertEqual(blocks, ['This is **bolded** paragraph', 'This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line', '- This is a list\n- with items'])

    def test_markdown_to_blocks_excess_whitespace(self):
        sample_markdown = """
    This is **bolded** paragraph            

    This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line         

    - This is a list
- with items           
    """
        blocks = BlockNode.markdown_to_blocks(sample_markdown)
        self.assertEqual(blocks, ['This is **bolded** paragraph', 'This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line', '- This is a list\n- with items'])

    def test_markdown_to_blocks_no_newline(self):
        sample_markdown = "This is **bolded** paragraph"
        blocks = BlockNode.markdown_to_blocks(sample_markdown)
        self.assertEqual(blocks, ['This is **bolded** paragraph'])

    def test_markdown_to_blocks_to_meny_newlines(self):
        sample_markdown = """
This is **bolded** paragraph



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



- This is a list
- with items
    """
        blocks = BlockNode.markdown_to_blocks(sample_markdown)
        self.assertEqual(blocks, ['This is **bolded** paragraph', 'This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line', '- This is a list\n- with items'])
    
    def test_markdown_to_blocks_no_text(self):
        sample_markdown = ""
        blocks = BlockNode.markdown_to_blocks(sample_markdown)
        self.assertEqual(blocks, [])

    # Test block_to_block_type
    def test_block_to_block_type_inline_paragraph(self):
        block = "This is a paragraph"
        block_type = BlockNode.block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_paragraph(self):
        markdown = """
This is a paragraph
This is a paragraph
This is a paragraph
"""     
        blocks = BlockNode.markdown_to_blocks(markdown)
        for block in blocks:
            block_type = BlockNode.block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
    
    # Test block_to_block_type Heading
    def test_block_to_block_type_inline_heading(self):
        block = "# This is a heading"
        block_type = BlockNode.block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)
    
    def test_block_to_block_type_1_to_6_heading(self):
        markdown = """
# This is a heading
## This is a heading
### This is a heading
#### This is a heading
##### This is a heading
###### This is a heading
"""     
        blocks = BlockNode.markdown_to_blocks(markdown)
        for block in blocks:
            block_type = BlockNode.block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)
    
    def test_block_to_block_type_greater_than_6_heading(self):
        block = "######## This is a heading"
        block_type = BlockNode.block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
    
    # Test block_to_block_type Code
    def test_block_to_block_type_inline_code(self):
        block = "```python\nprint('Hello, World!')\n```"
        block_type = BlockNode.block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)
    
    def test_block_to_block_type_code(self):
        markdown = """
```
This is a paragraph
This is a paragraph
This is a paragraph
```
"""     
        blocks = BlockNode.markdown_to_blocks(markdown)
        for block in blocks:
            block_type = BlockNode.block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)
    
    def test_block_to_block_type_code_no_closing(self):
        markdown = """
```
This is a paragraph
This is a paragraph
This is a paragraph
"""     
        blocks = BlockNode.markdown_to_blocks(markdown)
        for block in blocks:
            block_type = BlockNode.block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
    
    def test_block_to_block_type_code_no_opening(self):
        markdown = """
This is a paragraph
This is a paragraph
This is a paragraph
```
"""     
        blocks = BlockNode.markdown_to_blocks(markdown)
        for block in blocks:
            block_type = BlockNode.block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
    
    def test_block_to_block_type_inline_code_no_closing(self):
        block = "```python\nprint('Hello, World!')"
        block_type = BlockNode.block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
    
    def test_block_to_block_type_inline_code_no_opening(self):
        block = "print('Hello, World!')\n```"
        block_type = BlockNode.block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    # Test block_to_block_type Quote
    def test_block_to_block_type_inline_quote(self):
        block = "> This is a quote"
        block_type = BlockNode.block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)
    
    def test_block_to_block_type_quote(self):
        markdown = """
> This is a paragraph
> This is a paragraph
> This is a paragraph
"""     
        blocks = BlockNode.markdown_to_blocks(markdown)
        for block in blocks:
            block_type = BlockNode.block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)
    
    def test_block_to_block_type_missing_quote(self):
        markdown = """
> This is a paragraph
This is a paragraph
> This is a paragraph
"""     
        blocks = BlockNode.markdown_to_blocks(markdown)
        for block in blocks:
            block_type = BlockNode.block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    # Test block_to_block_type Unordered List
    def test_block_to_block_type_inline_nordered_list(self):
        block = "- This is a list item"
        block_type = BlockNode.block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_block_to_block_type_unordered_list(self):
        markdown = """
- This is a list item
- This is not a list item
- This is a list item
"""
        blocks = BlockNode.markdown_to_blocks(markdown)
        for block in blocks:
            block_type = BlockNode.block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)
    
    def test_block_to_block_type_unordered_list_no_dash(self):
        markdown = """
- This is a list item
This is not a list item
- This is a list item
"""
        blocks = BlockNode.markdown_to_blocks(markdown)
        for block in blocks:
            block_type = BlockNode.block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    # Test block_to_block_type ordered List
    def test_block_to_block_type_inline_ordered_list(self):
        block = "1. This is a list item"
        block_type = BlockNode.block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_block_to_block_type_unordered_list(self):
        markdown = """
1. This is a list item
2. This is not a list item
3. This is a list item
"""
        blocks = BlockNode.markdown_to_blocks(markdown)
        for block in blocks:
            block_type = BlockNode.block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_block_to_block_type_float_unordered_list(self):
        markdown = """
1.0 This is a list item
2.0 This is not a list item
3.0 This is a list item
"""
        blocks = BlockNode.markdown_to_blocks(markdown)
        for block in blocks:
            block_type = BlockNode.block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
    
    def test_block_to_block_type_ordered_list_no_number(self):
        markdown = """
1. This is a list item
This is not a list item
3. This is a list item
"""
        blocks = BlockNode.markdown_to_blocks(markdown)
        for block in blocks:
            block_type = BlockNode.block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_ordered_list_incorrect_number(self):
        markdown = """
1. This is a list item
3. This is a list item
2. This is a list item
"""
        blocks = BlockNode.markdown_to_blocks(markdown)
        for block in blocks:
            block_type = BlockNode.block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
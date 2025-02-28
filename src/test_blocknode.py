import unittest

from blocknode import BlockNode

class TestBlockNode(unittest.TestCase):

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
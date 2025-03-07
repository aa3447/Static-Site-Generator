import unittest

from htmlmaker import HTMLMaker


class TestHtmlMaker(unittest.TestCase):
     # Test cases for paragraphs
    def test_paragraphs(self):
        sample_markdown = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        html_node = HTMLMaker.markdown_to_html_node(sample_markdown)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    # Test cases for headings
    def test_heading(self):
        sample_markdown = """
# This is text that should be the same.
"""

        html_node = HTMLMaker.markdown_to_html_node(sample_markdown)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is text that should be the same.</h1></div>",
        )

    def test_heading_nested_hastag(self):
        sample_markdown = """
# This is text that # should be the same.
"""

        html_node = HTMLMaker.markdown_to_html_node(sample_markdown)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is text that # should be the same.</h1></div>",
        )
    
    def test_heading_larger_heading(self):
        sample_markdown = """
###### This is h6.
"""

        html_node = HTMLMaker.markdown_to_html_node(sample_markdown)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><h6>This is h6.</h6></div>",
        )
    
    def test_heading_stack(self):
        sample_markdown = """
# This is h1.

## This is h2.

### This is h3.

#### This is h4.

##### This is h5.

###### This is h6.
"""

        html_node = HTMLMaker.markdown_to_html_node(sample_markdown)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is h1.</h1><h2>This is h2.</h2><h3>This is h3.</h3><h4>This is h4.</h4><h5>This is h5.</h5><h6>This is h6.</h6></div>"
        )
    def test_heading_too_many_hastags(self):
        sample_markdown = """
####### This is h7.
"""

        html_node = HTMLMaker.markdown_to_html_node(sample_markdown)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><p>####### This is h7.</p></div>",
        )

    # Test cases for quotes
    def test_quote(self):
        sample_markdown = """
>This is text that _should_ remain.
"""

        html_node = HTMLMaker.markdown_to_html_node(sample_markdown)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is text that _should_ remain.</blockquote></div>",
        )
    
    def test_quote_inline_arrow(self):
        sample_markdown = """
>This is text that > _should_ remain.
"""

        html_node = HTMLMaker.markdown_to_html_node(sample_markdown)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is text that > _should_ remain.</blockquote></div>",
        )

    def test_quote_inline_markdown(self):
        sample_markdown = """
>This is text that *should* remain.
>This is text that **should** remain.
"""

        html_node = HTMLMaker.markdown_to_html_node(sample_markdown)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is text that <i>should</i> remain. This is text that <b>should</b> remain.</blockquote></div>",
        )
    
    def test_quote_block(self):
        sample_markdown = """
>This is text that _should_ remain.
>This is text that _should_ remain.
"""

        html_node = HTMLMaker.markdown_to_html_node(sample_markdown)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is text that _should_ remain. This is text that _should_ remain.</blockquote></div>",
        )
    
    def test_multi_quote_block(self):
        sample_markdown = """
>This is text that _should_ remain.
>This is text that _should_ remain.

>This is text that also _should_ remain.
>This is text that also _should_ remain.
"""

        html_node = HTMLMaker.markdown_to_html_node(sample_markdown)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is text that _should_ remain. This is text that _should_ remain.</blockquote><blockquote>This is text that also _should_ remain. This is text that also _should_ remain.</blockquote></div>",
        )
    
    def test_missing_quote(self):
        sample_markdown = """
>This is text that _should_ remain.
This is text that _should_ remain.
"""

        html_node = HTMLMaker.markdown_to_html_node(sample_markdown)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><p>>This is text that _should_ remain. This is text that _should_ remain.</p></div>",
        )
    
    # Test cases for unordered list
    def test_unordered_list(self):
        sample_markdown = """
- This is text that _should_ remain.
"""

        html_node = HTMLMaker.markdown_to_html_node(sample_markdown)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is text that _should_ remain.</li></ul></div>",
        )
    
    def test_unordered_list_block(self):
        sample_markdown = """
- This is text that _should_ remain.
- This is text that _should_ remain.
- This is text that _should_ remain.
"""

        html_node = HTMLMaker.markdown_to_html_node(sample_markdown)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is text that _should_ remain.</li><li>This is text that _should_ remain.</li><li>This is text that _should_ remain.</li></ul></div>",
        )
    
    def test_unordered_list_mulit_block(self):
        sample_markdown = """
- This is text that _should_ remain.
- This is text that _should_ remain.

- This is text that _should_ also remain.
- This is text that _should_ also remain.
"""

        html_node = HTMLMaker.markdown_to_html_node(sample_markdown)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is text that _should_ remain.</li><li>This is text that _should_ remain.</li></ul><ul><li>This is text that _should_ also remain.</li><li>This is text that _should_ also remain.</li></ul></div>",
        )
    
    def test_unordered_list_missing_dash(self):
        sample_markdown = """
- This is text that _should_ remain.
This is text that _should_ remain.
- This is text that _should_ remain.
"""

        html_node = HTMLMaker.markdown_to_html_node(sample_markdown)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><p>- This is text that _should_ remain. This is text that _should_ remain. - This is text that _should_ remain.</p></div>",
        )
    
    # Test cases for ordered list
    def test_ordered_list(self):
        sample_markdown = """
1. This is text that _should_ remain.
"""

        html_node = HTMLMaker.markdown_to_html_node(sample_markdown)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is text that _should_ remain.</li></ol></div>",
        )
    
    def test_ordered_list_block(self):
        sample_markdown = """
1. This is text that _should_ remain.
2. This is text that _should_ remain.
3. This is text that _should_ remain.
"""

        html_node = HTMLMaker.markdown_to_html_node(sample_markdown)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is text that _should_ remain.</li><li>This is text that _should_ remain.</li><li>This is text that _should_ remain.</li></ol></div>",
        )
    
    def test_ordered_list_mulit_block(self):
        sample_markdown = """
1. This is text that _should_ remain.
2. This is text that _should_ remain.

1. This is text that _should_ also remain.
2. This is text that _should_ also remain.
"""

        html_node = HTMLMaker.markdown_to_html_node(sample_markdown)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is text that _should_ remain.</li><li>This is text that _should_ remain.</li></ol><ol><li>This is text that _should_ also remain.</li><li>This is text that _should_ also remain.</li></ol></div>",
        )
    
    def test_ordered_list_missing_dash(self):
        sample_markdown = """
1. This is text that _should_ remain.
This is text that _should_ remain.
2. This is text that _should_ remain.
"""

        html_node = HTMLMaker.markdown_to_html_node(sample_markdown)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><p>1. This is text that _should_ remain. This is text that _should_ remain. 2. This is text that _should_ remain.</p></div>",
        )
    
    def test_ordered_list_missing_dash(self):
        sample_markdown = """
1. This is text that _should_ remain.
3. This is text that _should_ remain.
2. This is text that _should_ remain.
"""

        html_node = HTMLMaker.markdown_to_html_node(sample_markdown)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><p>1. This is text that _should_ remain. 3. This is text that _should_ remain. 2. This is text that _should_ remain.</p></div>",
        )

    # Test cases for code blocks
    def test_codeblock(self):
        sample_markdown = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        html_node = HTMLMaker.markdown_to_html_node(sample_markdown)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_codeblock_inline_backtick(self):
        sample_markdown = """
```
This is text that _should_ remain
the **same** even with ``` inline stuff
```
"""

        html_node = HTMLMaker.markdown_to_html_node(sample_markdown)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with ``` inline stuff\n</code></pre></div>",
        )

    def test_codeblock_single_line(self):
        sample_markdown = """
```This is text that _should_ remain the **same** even with ``` inline stuff```
"""

        html_node = HTMLMaker.markdown_to_html_node(sample_markdown)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain the **same** even with ``` inline stuff</code></pre></div>",
        )
    
    def test_extract_title(self):
        sample_markdown = "# Tolkien Fan Club\n"
        header = HTMLMaker.extract_title(sample_markdown)
        self.assertEqual(
            header,
            "Tolkien Fan Club",
        )
    
    def test_extract_title_no_newline(self):
        sample_markdown = "# Tolkien Fan Club"
        header = HTMLMaker.extract_title(sample_markdown)
        self.assertEqual(
            header,
            "Tolkien Fan Club",
        )
    
    def test_extract_title_tab(self):
        sample_markdown = "# Tolkien Fan     Club"
        header = HTMLMaker.extract_title(sample_markdown)
        self.assertEqual(
            header,
            "Tolkien Fan     Club",
        )
    
    def test_extract_end_space(self):
        sample_markdown = "# Tolkien Fan Club "
        header = HTMLMaker.extract_title(sample_markdown)
        self.assertEqual(
            header,
            "Tolkien Fan Club",
        )
    
    def test_extract_missing_hashtag(self):
        sample_markdown = "Tolkien Fan Club"
        with self.assertRaises(SyntaxError):
            HTMLMaker.extract_title(sample_markdown)
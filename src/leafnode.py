from htmlnode import HTMLNode
from textnode import TextType

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Missing value.")
        if self.tag is None:
            return self.value
        return f"<{self.tag + self.props_to_html()}>{self.value}</{self.tag}>"
    
    def text_node_to_leaf_node(text_node):
        match text_node.get_text_type():
            case TextType.NORMAL:
                return LeafNode(None, text_node.get_text())
            case TextType.BOLD:
                return LeafNode("b",text_node.get_text())
            case TextType.ITALIC:
                return LeafNode("i",text_node.get_text())
            case TextType.CODE:
                return LeafNode("code",text_node.get_text())
            case TextType.LINK:
                return LeafNode("a",text_node.get_text(), {"href": text_node.get_url()})
            case TextType.IMAGE:
                return LeafNode("img","", {"src": text_node.get_url(), "alt": text_node.get_text()})
            case _:
                raise ValueError("Invalid TextType.")
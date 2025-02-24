from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self , text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def get_text(self):
        return self.text
    
    def get_text_type(self):
        return self.text_type
    
    def get_url(self):
        return self.url
    
    def __eq__(self, text_node):
        return self.text == text_node.get_text() and self.text_type == text_node.get_text_type() and self.url == text_node.get_url()
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
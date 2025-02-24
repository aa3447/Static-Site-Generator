from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        new_value = ""
        if self.tag is None:
            raise ValueError("Missing value.")
        if len(self.children) == 0 or self.children is None:
            raise ValueError("Missing children.")
        
        for child in self.children:
            new_value += child.to_html()
        
        return f"<{self.tag}>{new_value}</{self.tag}>"
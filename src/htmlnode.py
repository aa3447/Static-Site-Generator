class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None or len(self.props) == 0:
            return ""
        
        string_map = map(lambda x: f' {x[0]}="{x[1]}"', self.props.items())
        html_string = "".join(list(string_map))
        return html_string
    
    def __repr__(self):
        return f"HTMLNODE({self.tag}, {self.value}, {self.children}, {self.props})"
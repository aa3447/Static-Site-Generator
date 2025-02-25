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
    
    def split_nodes_delimiter(self, old_nodes, delimiter, text_type):
        node_list = []
        
        for node in old_nodes:
            node_url = node.get_url()
            node_text = node.get_text()
            
            if node.get_text_type() != TextType.NORMAL:
                node_list.append(node)

            elif delimiter in node_text:
                if node_text.count(delimiter) % 2 != 0:
                    raise SyntaxError(f"Invalid delimiter count in {node}")
                
                split_node_text = node_text.split(delimiter,maxsplit=2)
                
                if split_node_text[0] != "":
                    node_list.append(TextNode(split_node_text[0], TextType.NORMAL))
                node_list.append(TextNode(split_node_text[1], text_type, node_url))
                if split_node_text[2] != "":
                     node_list.extend(self.split_nodes_delimiter([TextNode(split_node_text[2], TextType.NORMAL)], delimiter, text_type))         
            
            else:
                node_list.append(TextNode(node_text, TextType.NORMAL))

        return node_list

    def __eq__(self, text_node):
        return self.text == text_node.get_text() and self.text_type == text_node.get_text_type() and self.url == text_node.get_url()
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
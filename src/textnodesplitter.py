from textnode import TextNode ,TextType
import re

class TextNodeSplitter:
    def __init__(self):
        pass

    def split_nodes_delimiter(old_nodes, delimiter, text_type):
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
                     node_list.extend(TextNodeSplitter.split_nodes_delimiter([TextNode(split_node_text[2], TextType.NORMAL)], delimiter, text_type))         
            
            else:
                node_list.append(TextNode(node_text, TextType.NORMAL))

        return node_list
    
    def extract_markdown_images(text):
        """
        Extracts all markdown image links from the given text.

        Parameters:
        text (str): The text from which to extract markdown image links.

        Returns:
        list: A list of tuples, each containing the alt text and URL of a markdown image.
        """
        return re.findall(r"!\[([^\[\]]*)\]\((.+?)\)", text)
    
    def extract_markdown_links(text):
        return re.findall(r"\[([^\[\]]*)\]\((.+?)\)", text)
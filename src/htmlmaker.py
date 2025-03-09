from blocknode import BlockNode , BlockType
from parentnode import ParentNode
from leafnode import LeafNode
from textnodesplitter import TextNodeSplitter
import re
import os

class HTMLMaker:
    def __init__(self):
        pass

    def markdown_to_html_node(markdown):
        blocks = BlockNode.markdown_to_blocks(markdown)
        html_nodes = []
        for block in blocks:
            block_type = BlockNode.block_to_block_type(block)

            leaf_nodes = HTMLMaker.block_to_leaf_nodes(block, block_type)
            
            html_nodes.append(ParentNode(HTMLMaker.block_type_to_tag(block_type, block), leaf_nodes))
        
        return ParentNode("div", html_nodes)
    
    
    def block_to_leaf_nodes(block, block_type):
        new_block = block
        match block_type:
            case BlockType.HEADING:
                new_block = block.lstrip("#").lstrip()
            case BlockType.QUOTE:
                new_block = HTMLMaker.__quote_block_to_stripped_string(new_block)
            case BlockType.UNORDERED_LIST:
                new_block = HTMLMaker.__unorderd_list_block_to_stripped_string(new_block)
            case BlockType.ORDERED_LIST:
                new_block = HTMLMaker.__orderd_list_block_to_stripped_string(new_block)
            case BlockType.CODE:
                return HTMLMaker.__code_block_to_leaf_node(new_block)
        
        return HTMLMaker.__text_to_children(new_block)
    
    def __orderd_list_block_to_stripped_string(quote_block):
        split_newline_block = quote_block.splitlines()
        cleaned_lines = map(lambda line: f"<li>{re.sub(r"\d+. ","",line).lstrip()}</li>", split_newline_block)
        return "".join(cleaned_lines)
    
    def __unorderd_list_block_to_stripped_string(quote_block):
        split_newline_block = quote_block.splitlines()
        cleaned_lines = map(lambda line: f"<li>{line.removeprefix("-").lstrip()}</li>", split_newline_block)
        return "".join(cleaned_lines)
    
    def __quote_block_to_stripped_string(quote_block):
        split_newline_block = quote_block.splitlines()
        striped_block = map(lambda line: line.removeprefix(">").lstrip(), split_newline_block)
        return " ".join(striped_block)
    
    def __code_block_to_leaf_node(code_block):
        split_block = code_block.splitlines(True)
        if len(split_block) <= 1:
            return [LeafNode("code", "".join(split_block).removeprefix("```").removesuffix("```"))]
        return [LeafNode("code", "".join(split_block[1:-1]))]
    
    def __text_to_children(text):
        no_newline_text = text.replace("\n", " ")
        leaf_nodes = []
        text_nodes = TextNodeSplitter.text_to_textnodes(no_newline_text)
        for value in text_nodes:
            leaf_nodes.append(LeafNode.text_node_to_leaf_node(value))
        return leaf_nodes
    
    def extract_title(markdown):
        if markdown.startswith("# "):
            match = re.match(r"# [\w\t ]+\n", markdown)
            if match:
                return match.group().lstrip("#").strip()
            return markdown.lstrip("#").strip()
        
        raise SyntaxError("Missing heading")
    
    def generate_page(from_path, template_path, dest_path, basepath = "/"):
        markdown_as_string = ""
        template_as_string = ""
        print(f"Generating page from {from_path} to {dest_path} using {template_path}")

        dest_path_dicts = os.path.dirname(dest_path)
        if not os.path.exists(dest_path_dicts):
            os.makedirs(dest_path_dicts)

        with open(from_path) as markdown:
            markdown_as_string = markdown.read()
        
        with open(template_path) as template:
            template_as_string = template.read()
        
        html = HTMLMaker.markdown_to_html_node(markdown_as_string).to_html()
        title = HTMLMaker.extract_title(markdown_as_string)
        complete_template = template_as_string.replace("{{ Title }}", title).replace("{{ Content }}", html)
        complete_template_with_basepath = complete_template.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}') 
 
       
        with open(dest_path, "w") as fin_html:
                fin_html.write(complete_template_with_basepath)

    def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath = "/"):
        markdown_as_string = ""
        template_as_string = ""
        print(f"Generating pages from {dir_path_content} to {dest_dir_path} using {template_path}")

        current_paths = os.scandir(dir_path_content)

        for p in current_paths:
            p_path = p.path
            if os.path.isfile(p_path) and os.path.splitext(p_path)[1] == ".md":
                dest_path_dicts = os.path.dirname(p_path).replace("./content", dest_dir_path)
                
                if not os.path.exists(dest_path_dicts):
                    os.makedirs(dest_path_dicts)
                
                with open(p_path) as markdown:
                    markdown_as_string = markdown.read()
                
                with open(template_path) as template:
                    template_as_string = template.read()

                html = HTMLMaker.markdown_to_html_node(markdown_as_string).to_html()
                title = HTMLMaker.extract_title(markdown_as_string)
                complete_template = template_as_string.replace("{{ Title }}", title).replace("{{ Content }}", html)
                complete_template_with_basepath = complete_template.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}') 
               
                public_path = p.path.replace("./content", dest_dir_path).replace(".md",".html")
                with open(public_path, "w") as fin_html:
                    fin_html.write(complete_template_with_basepath)  
            else:
                HTMLMaker.generate_pages_recursive(p_path, template_path, dest_dir_path, basepath)
        
           
    def block_type_to_tag(block_type, block):
        match block_type:
            case BlockType.PARAGRAPH:
                return "p"
            case BlockType.HEADING:
                return f"h{block.count('#', 0, 7)}"
            case BlockType.CODE:
                return "pre"
            case BlockType.QUOTE:
                return "blockquote"
            case BlockType.UNORDERED_LIST:
                return "ul"
            case BlockType.ORDERED_LIST:
                return "ol"
            case _:
                raise SyntaxError("Invalid Block Type")
            
            
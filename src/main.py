from htmlmaker import HTMLMaker
from copystatictopublic import CopyStaticToPublic
import sys
import os

def main():
    public_path = "./docs"
    public_path_single_file = "./docs/index.html"
    static_path = "./static"
    basepath = "/"
    is_dir = False
    
    if len(sys.argv) > 1 and sys.argv[1] != "":
        basepath = sys.argv[1]


    copier = CopyStaticToPublic(public_path, static_path)
    copier.copy_static_to_public()

    current_paths = os.scandir("./content")

    for p in current_paths:
        if p.is_dir():
            is_dir = True
            break
    
    if is_dir:
        HTMLMaker.generate_pages_recursive("./content", "./template.html", public_path, basepath)
    else:
        HTMLMaker.generate_page("./content/index.md", "./template.html", public_path_single_file , basepath)
    
    
if __name__ == "__main__":
    main()
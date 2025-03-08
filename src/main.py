from htmlmaker import HTMLMaker
from copystatictopublic import CopyStaticToPublic

def main():
    public_path = "./public"
    static_path = "./static"

    copier = CopyStaticToPublic(public_path, static_path)
    copier.copy_static_to_public()

    #HTMLMaker.generate_page("./content/index.md", "./template.html", "./public/index.html")
    HTMLMaker.generate_pages_recursive("./content", "./template.html", "./public")
    
if __name__ == "__main__":
    main()
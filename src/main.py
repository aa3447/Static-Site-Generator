from htmlmaker import HTMLMaker
from copystatictopublic import CopyStaticToPublic

def main():
    public_path = "./public"
    static_path = "./static"

    copier = CopyStaticToPublic(public_path, static_path)
    copier.copy_static_to_public()

    HTMLMaker.generate_page("./src/content/index.md", "./template.html", "./public/index.html")
    
if __name__ == "__main__":
    main()
import os
import shutil

class CopyStaticToPublic:
    def __init__(self, public_path, static_path):
        self.__public_path = public_path
        self.__static_path = static_path

    def copy_static_to_public(self):
        if os.path.exists(self.__public_path):
            shutil.rmtree(self.__public_path)
            os.mkdir(self.__public_path)
        else:
            os.mkdir(self.__public_path)

        self.__copy_static(self.__static_path, self.__public_path)


    def __copy_static(self,static_path , public_path):
        current_paths = os.scandir(static_path)

        for p in current_paths:    
            if os.path.isfile(p):
                print(f"Current files path: {p.path}")
                shutil.copy(p.path, public_path)
            else:
                print(f"Current dir path: {p.path}")
                public_dir_path = p.path.replace(self.__static_path, self.__public_path)
                print(public_dir_path)
                os.mkdir(public_dir_path)
                self.__copy_static(p.path, public_dir_path)
import os, platform

databases = []
folder_name = []

class Create():
    def __init__(self, name):
        self.name = str(name)
        self.create_specified_folder()

    def create_specified_folder(self):
        self.path_name  = os.path.join(os.getcwd(), self.name)

        if self.name:
            os.mkdir(self.path_name)

            folder_name.append(self.path_name)

            return self.path_name
        else:
            return str(os.getcwd())

    def __repr__(self):
        return "Succesfully created"

def init(name):
    folder_created = Create(name)

    return folder_created
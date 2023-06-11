import os
import requests
from PIL import Image
from contextlib import suppress
from time import sleep


class FolderManip():
    def __init__(self):
        self.folder_path = f'{os.getcwd()}/.cats/'
        self.folder_exist = False
        self.create_folder()

    def create_folder(self):
        if os.path.isdir(self.folder_path) is False:
            os.mkdir(self.folder_path)
            self.folder_exist = True
        else:
            self.folder_exist = True

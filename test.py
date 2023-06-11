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

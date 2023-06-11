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
        if os.path.isdir(self.folder_path):
            self.folder_exist = True
        else:
            os.mkdir(self.folder_path)
            self.folder_exist = True

    def remove_photos(self):
        if self.folder_exist is True:
            for photo in os.listdir(self.folder_path):
                os.remove(f'{self.folder_path}{photo}')


class Api():
    def __init__(self):
        self.api = 'https://api.thecatapi.com/v1/images/search'

    def check_api_status(self, request):
        if request.status_code != 200:
            print(f'Error: {request.status_code}. Verify your connection')
            exit()
        else:
            print('Connection was successful.')

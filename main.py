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
        self.remove_photos()

    def create_folder(self):
        if os.path.isdir(self.folder_path):
            self.folder_exist = True
        else:
            os.mkdir(self.folder_path)
            self.folder_exist = True

    def remove_photos(self):
        for photo in os.listdir(self.folder_path):
            os.remove(f'{self.folder_path}{photo}')


class Api():
    def __init__(self):
        self.api_http = 'https://api.thecatapi.com/v1/images/search'

    def check_api_status(self, request):
        if request.status_code != 200:
            print(f'Error: {request.status_code}. Verify your connection')
            exit()
        else:
            print('Connection was successful.')

    def get_image_url(self):
        api_url = requests.get(self.api)
        print('Connecting to API...')
        sleep(0.5)
        self.check_api_status(api_url)
        return api_url.json()[0].get('url')

    def request_image_url(self, image_url):
        with suppress():
            image = requests.get(image_url)
            print('Collecting the photo...')
            sleep(0.5)
            self.check_api_status(image)
            return image


class Photo():
    def __init__(self, api, foldermanip):
        self.api = api()
        self.foldermanip = foldermanip()
        self.image_url = self.api.get_image_url()
        self.image_name = self.image_url.split('/')[-1]

    def image_path(self):
        return f'{self.foldermanip.folder_path}{self.image_name}'

    def get_photo(self):
        return self.api.request_image_url(self.image_url)

    def save_picture(self):
        with open(f'{self.image_path()}', 'wb') as file:
            file.write(self.get_photo().content)

    def open_image(self):
        photo = Image.open(self.image_path())
        print('Opening the photo!')
        photo.show()


if __name__ == '__main__':
    x = Photo(Api, FolderManip)
    x.foldermanip.remove_photos()
    x.save_picture()
    x.open_image()

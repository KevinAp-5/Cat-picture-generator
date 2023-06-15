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

    def request(self, request, request_text=None):
        with suppress():
            requested = requests.get(request)
            if request_text is not None:
                print(request_text)
            sleep(0.5)
            self.check_api_status(requested)
            return requested

    def get_image_url(self, image_url):
        """
        Will request the image content from the requested json
        """
        cat_json = self.request(image_url)
        return cat_json.json()[0].get('url')


class ImageManip(FolderManip):
    def __init__(self, image_url):
        super().__init__()
        self.image_url = image_url
        self.image_name = self.image_url.split('/')[-1]

    def image_path(self):
        return f'{self.folder_path}{self.image_name}'

    def save_picture(self, image_content):
        with open(f'{self.image_path()}', 'wb') as file:
            file.write(image_content.content)

    def open_image(self):
        photo = Image.open(self.image_path())
        print('Opening the photo!')
        photo.show()


if __name__ == '__main__':
    my_api = Api()
    cat_json = my_api.request(my_api.api_http, "Connecting to API")
    image_url = cat_json.json()[0].get('url')
    image_content = my_api.request(image_url, "Getting the image")

    img = ImageManip(image_url)
    img.save_picture(image_content)
    img.open_image()

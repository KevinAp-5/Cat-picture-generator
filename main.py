import os
import requests
from PIL import Image
from time import sleep
from platform import system
from contextlib import suppress

def folder_path():
    return f'{os.getcwd()}/cats/'

def create_folder():
    if os.path.isdir(folder_path()) is False:
        os.mkdir(folder_path())
        return True
    else:
        return False

def remove_photos():
    for photo in os.listdir(folder_path()):
        os.remove(f'{folder_path()}{photo}')

def check_api_status(request):
    if request.status_code != 200:
        print(f'Error: {image_url.status_code}. Verify your connection')
    else:
        print('Connection with the API was successful.')

def get_url():
    api_url = requests.get('https://api.thecatapi.com/v1/images/search')
    return api_url.json()[0].get('url')

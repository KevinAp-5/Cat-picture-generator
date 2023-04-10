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

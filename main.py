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

if image_url.status_code != 200:
    print(f'Error: {image_url.status_code}. Verify your connection')
else:
    print('Connection with the API was successful.')
    sleep(1)

url = image_url.json()
print('Searching for a very cute cat photo for you.')
sleep(1.2)
for x, y in url[0].items():
    if x == 'url':
        name = y.split('/')[-1]
        try:
            x = requests.get(y)
        except Exception:
            raise
        else:
            print('Opening the cat photo.')
            sleep(0.4)
            try:
                with open(f'cats/{name}', 'wb') as foto:
                    foto.write(x.content)  # Write the picture
            except Exception:
                raise
            else:
                path_cat = f'cats/{name}'
                if 'linux' in system():
                    os.system(f'xdg-open {path_cat}')
                else:
                    photo = Image.open(r'{}'.format(path_cat))  # Open image
                    photo.show()  # Show the image


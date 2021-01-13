import os
import requests
from PIL import Image

mypath = f'{os.getcwd()}/cats/'
try:
    path = os.listdir(mypath)  # remove the old cat photos
except FileNotFoundError:
    os.mkdir(mypath)
else:
    for x in path:
        os.remove(mypath+x)

api = 'https://api.thecatapi.com/v1/images/search'

image_url = requests.get(api, headers={'User-Agent': 'python'})
if image_url.status_code != 200:
    print(f'Error: {image_url.status_code}. Verify your conection')

url = image_url.json()
for x, y in url[0].items():
    if x == 'url':
        name = y.split('/')[-1]
        try:
            x = requests.get(y)
        except Exception:
            raise
        else:
            try:
                with open(f'cats/{name}', 'wb') as foto:
                    foto.write(x.content)  # Write the picture
            except Exception:
                raise
            else:
                a = f'cats/{name}'
                photo = Image.open(r'{}'.format(a))  # Open the image
                photo.show()  # Show the image

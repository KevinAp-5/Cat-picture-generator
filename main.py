import os
import requests

def delete_images():
    path = os.listdir(f'{os.getcwd()}/cats/')
    if path != []:
        for x in path:
            os.remove(f'{os.getcwd()}/cats/{x}')

delete_images()

api = 'https://api.thecatapi.com/v1/images/search'
image_url = requests.get(api, headers={'User-Agent': 'python'})

if image_url.status_code != 200:
    print('Error:', image_url.status_code)
    exit()

url = image_url.json()
name = ''

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
                    foto.write(x.content)
            except Exception:
                raise
            else:
                pass
#                os.system(f'xdg-open cats/{name}')  # open the image


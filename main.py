import os
import requests

try:
    path = os.listdir(f'{os.getcwd()}/cats/')  # remove the old cat photos
except FileNotFoundError:
    os.mkdir(f'{os.getcwd()}/cats/')
else:
    for x in path:
        os.remove(f'{os.getcwd()}/cats/{x}')


api = 'https://api.thecatapi.com/v1/images/search'
counter = 0
while True:
    image_url = requests.get(api, headers={'User-Agent': 'python'})
    if image_url.status_code != 200:
        print(f'Error: {image_url.status_code}\nTrying again...')
        if counter == 5:
            print('Error trying to request...\nVerify you connection.')
            exit()
        counter += 1
        continue
    else:
        break


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
                os.system(f'sensible-browser cats/{name}')  # open the image


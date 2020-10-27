import os
import requests

api = 'https://api.thecatapi.com/v1/images/search'
image_url = requests.get(api)
if image_url.status_code != 200:
    print('Error:', image_url.status_code)
    exit()

url = image_url.json()
name = ''

for x, y in url[0].items():
    if x == 'url':
        name = y.split('/')[-1]
        if os.path.exists('url') is False:
            with open('url.txt', 'w') as url:
                url.write(y)

        try:
            os.system(f'wget {y}')
        except Exception:
            raise
        else:
            os.system(f'xdg-open {name}')

create_dir()

# バージョンが合わない

import requests
import re
import os
import shutil

path = r"instagram"

error_flg = False
all_images = []

if error_flg is False:
    all_images = list(set(all_images))
    for index, image in enumerate(all_images):
        filename = 'image_' + str(index) + '.jpg'
        image_path = os.path.join(path, filename)
        image_link = image['src']

        # Check URL
        URL_PTN = re.compile(r"^(http|https)://")
        res = URL_PTN.match(image_link)
        if res:
            # Downloading Image
            response = requests.get(image_link, stream = True)
            try:
                # Saving Image
                with open(image_path, 'wb') as file:
                    shutil.copyfileobj(response.row, file)
            except Exception as e:
                print(e)
                print(str(index) + ' Image Not Found!')
                print('LINK : ' + image_link)


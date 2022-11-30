import time
import concurrent.futures
import requests

img_urls = [
    'https://cdn.pixabay.com/photo/2022/11/02/04/07/deer-7563934_1280.jpg',
    'https://cdn.pixabay.com/photo/2022/11/14/06/56/maple-7590861_1280.jpg'
]
def download_images (img_url):
    img_bytes = requests.get (img_url).content
    img_name = img_url.split ('/') [4]
    with open (img_name, 'wb') as img_file:
        img_file.write (img_bytes)
        print(f"{img_name} was downloaded")

start = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_images, img_urls)

end = time.perf_counter()
print(f"Tasks ended in {round(end - start, 2)} second(s)")
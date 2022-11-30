import time
import concurrent.futures
import requests
import threading
import multiprocessing


def task(i):
    print(f"task {i} starts")
    time.sleep
    print(f"task {i} ends")

start = time.perf_counter()

t1 = threading.Thread(target = task, args=[1])
t1.start()
t1.join()

end = time.perf_counter()

print(f"tasks ended in {round(end - start, 2)} second(s)")


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


def task():
    print(f"Task starts for 1 second")
    time.sleep(1)
    print(f"Task ends")
if __name__ == '__main__':
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)
    p1.start()
    p2.start()
    end = time.perf_counter()
    print (f"tasks ended in {round(end - start, 2)} second(s)")

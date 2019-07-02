from threading import Thread
import requests

def get():
    r = requests.get("http://haha.wargame.whitehat.vn/?le=1")
    print(r.text)

threads = [None] * 100
for i in range(len(threads)):
    threads[i] = Thread(target=get)
    threads[i].start()

# https://en.wikibooks.org/wiki/Python_Programming/Threading

import threading
import time


# A Minimal Example with Function Call

def loop1_10():
    for i in range(1, 11):
        time.sleep(1)
        print(i)


# Make a thread that prints numbers from 1-10, waits for 1 sec between :
threading.Thread(target=loop1_10).start()

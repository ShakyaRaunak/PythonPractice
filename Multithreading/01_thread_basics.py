# https://www.tutorialspoint.com/python/python_multithreading.htm

"""
Running several threads is similar to running several different programs concurrently, but with the following benefits −
- Multiple threads within a process share the same data space with the main thread and can therefore share information or
communicate with each other more easily than if they were separate processes.
- Threads sometimes called light-weight processes and they do not require much memory overhead;
they are cheaper than processes.

A thread has a beginning, an execution sequence, and a conclusion. It has an instruction pointer that keeps track of
where within its context it is currently running.
- It can be preempted (interrupted).
- It can temporarily be put on hold (also known as sleeping) while other threads are running - this is called yielding.
"""

import threading
import time


# Define a function for the thread
def print_time(thread, delay):
    thread.start()
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (thread.name, time.ctime(time.time())))


# Create two threads as follows :
try:
    print_time(threading.Thread(name="Thread-1"), 2)
    print_time(threading.Thread(name="Thread-2"), 4)
except:
    print("Error: unable to start thread")

while 1:
    pass

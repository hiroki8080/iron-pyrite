import time
import threading
from multiprocessing import Process

#
# Multithreading does not currently work...
#

def process():
    print('Start process..')
    time.sleep(5)
    print('End process..')

def process2():
    print('Start process2..')
    time.sleep(3)
    print('End process2..')


def main():
    print('Start threads...')
    # thread1 = threading.Thread(target=process)
    # thread2 = threading.Thread(target=process2)
    # thread1.start()
    # thread2.start()
    # thread1.join()
    # thread2.join()
    p1 = Process(target=process)
    p2 = Process(target=process2)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('End threads...')

if __name__ == "__main__":
    main()
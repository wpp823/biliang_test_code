from queue import Queue
import time, threading

q = Queue(maxsize=0)


def product(name):
    count = 1
    while True:
        q.put('气球兵{}'.format(count))
        print('{}训练气球兵{}只'.format(name, count))
        count += 1
        time.sleep(5)


def consume(name):
    while True:
        print('{}使用了{}'.format(name, q.get()))
        time.sleep(1)
        q.task_done()


t1 = threading.Thread(target=product, args=('wpp',))
t2 = threading.Thread(target=consume, args=('ypp',))
t3 = threading.Thread(target=consume, args=('others',))

t1.start()
t2.start()
t3.start()
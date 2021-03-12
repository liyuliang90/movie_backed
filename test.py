import threading
import time
pool={}


def test():
    time.sleep(10)

def testmain():
    for i in range(10):
        task = threading.Thread(target=test)
        pool[i] = task
    for k,v in pool.items():
        v.setDaemon(True)
        v.start()
    while 1:
        for k in list(pool.keys()):
           print(pool[k].is_alive())
           if not pool[k].is_alive():
               del pool[k]
               #pool.pop(k)
        if len(pool)==0:
            break
        time.sleep(2)

if __name__ == '__main__':
    testmain()
            



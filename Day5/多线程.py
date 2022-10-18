from threading import Thread
# def func():
#     for i in range(100):
#         print("func",i)

class MyThread(Thread):
    def run(self):
        for i in range(100):
            print("子线程",i)
if __name__=='__main__':
    # t=Thread(target=func)
    # t.start()


    t=MyThread()
    t.start()
    for i in range(100):
        print("主线程",i)
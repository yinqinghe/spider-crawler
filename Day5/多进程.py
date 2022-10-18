from multiprocessing import Process


def func():
    for i in range(100):
        print("子进程", i)


if __name__ == '__main__':
    p = Process(target=func)
    p.start()
    for i in range(100):
        print("主进程", i)

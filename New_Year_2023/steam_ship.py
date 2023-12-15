import time

from steamship import Steamship

ship=Steamship()

gtp4=ship.use_plugin("gpt-4")
while 1:
    question=input("请输入你的问题 :  ")
    if question=='q':
        break
    start = time.time()
    # task = gtp4.generate(text="怎么学习go语言")
    task = gtp4.generate(text=question)
    task.wait()
    end = time.time()
    print("消耗时间为：", end - start)
    print(task.output.blocks[0].text)

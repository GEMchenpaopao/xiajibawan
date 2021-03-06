"""
编写一个程序，每隔2秒向文件 my.log中写入
一行内容（如果这个文件不存在则自动创建）
程序死循环不会停止. 当强行结束程序，重新
启动之后能够继续写入内容，并序号衔接，每次
写入一行都要显示出来

    1. 2020-11-30 18:18:18
    2. 2020-11-30 18:18:20
    3. 2020-11-30 18:18:22
    4. 2020-11-30 18:18:24
    5. 2020-11-30 18:20:08
    6. 2020-11-30 18:20:10
    7. 2020-11-30 18:20:12

  提示： sleep(2)   localtime()
"""
import time

# 追加方式打开文件
file = open("my.log", "a+",buffering=1)

file.seek(0,0) # 文件偏移量在开头
n = len(file.readlines()) + 1 # n 应该等于 行数+1

while True:
    tm = time.localtime()
    msg = "%d. " % n + "%d-%d-%d %d:%d:%d\n" % tm[:6]
    file.write(msg)
    n += 1
    time.sleep(2) # 间隔时间
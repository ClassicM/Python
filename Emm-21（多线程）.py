'''
多任务可以由多进程完成，也可以由一个进程内的多线程完成。
我们前面提到了进程是由若干线程组成的，一个进程至少有一个线程。
由于线程是操作系统直接支持的执行单元，因此，高级语言通常都内置多线程的支持，Python也不例外，并且，Python的线程是真正的Posix Thread，而不是模拟出来的线程。
Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。
'''
#启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
import time,threading

#新线程执行的代码
def loop():
    print('thread %s is runnig...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)
print('thread %s is runnig...' % threading.current_thread().name)
t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread % s ended.' % threading.current_thread().name)
'''
由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程
Python的threading模块有个current_thread()函数，它永远返回当前线程的实例
主线程实例的名字叫MainThread，子线程的名字在创建时指定，我们用LoopThread命名子线程
名字仅仅在打印时用来显示，完全没有其他意义，如果不起名字Python就自动给线程命名为Thread-1，Thread-2……
'''
#Lock
'''
多线程和多进程最大的不同在于:
多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响
而多线程中，所有变量都由所有线程共享,所以，任何一个变量都可以被任何一个线程修改
因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
'''
#来看看多个线程同时操作一个变量怎么把内容给改乱了：

# 假定这是你的银行存款:
balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(10000000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
'''
我们定义了一个共享变量balance，初始值为0，并且启动两个线程，先存后取，理论上结果应该为0，但是，由于线程的调度是由操作系统决定的
当t1、t2交替执行时，只要循环次数足够多，balance的结果就不一定是0了。
两个线程同时一存一取，就可能导致余额不对，你肯定不希望你的银行存款莫名其妙地变成了负数，所以，我们必须确保一个线程在修改balance的时候，别的线程一定不能改。
'''

'''
如果我们要确保balance计算正确，就要给change_it()上一把锁，当某个线程开始执行change_it()时，我们说，该线程因为获得了锁
因此其他线程不能同时执行change_it()，只能等待，直到锁被释放后，获得该锁以后才能改
由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突
'''
#创建一个锁就是通过threading.Lock()来实现：
balance = 0
lock = threading.Lock()

def run_thread(n):
    for i in range(100000):
        #先要获取锁
        lock.acquire()
        try:
            #放心地改吧
            change_it(n)
        finally:
            #改完了一定要释放锁
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

#多核CPU
'''
如果你不幸拥有一个多核CPU，你肯定在想，多核应该可以同时执行多个线程。

如果写一个死循环的话，会出现什么情况呢？

打开Mac OS X的Activity Monitor，或者Windows的Task Manager，都可以监控某个进程的CPU使用率。

我们可以监控到一个死循环线程会100%占用一个CPU。

如果有两个死循环线程，在多核CPU中，可以监控到会占用200%的CPU，也就是占用两个CPU核心。

要想把N核CPU的核心全部跑满，就必须启动N个死循环线程。
'''
#试试用pyhon写个死循环：
import threading,multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()

'''
小结
多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。
Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。
'''
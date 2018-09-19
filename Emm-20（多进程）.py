print('进程和线程')
'''
多任务的实现有3种方式：
多进程模式；
多线程模式；
多进程+多线程模式。

线程是最小的执行单元，而进程由至少一个线程组成。如何调度进程和线程，完全由操作系统决定，程序自己不能决定什么时候执行，执行多长时间。
多进程和多线程的程序涉及到同步、数据共享的问题，编写起来更复杂。

'''
print('--------------------------')
print('多进程')
'''
要让Python程序实现多进程（multiprocessing），我们先了解操作系统的相关知识。
Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。
普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次
因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
子进程永远返回0，而父进程返回子进程的ID。
这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。
'''
#Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程：
import os
print('Process(%s)start...'%os.getpid())
#only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process(%s) and my praent is %s.'%(os.getpid(),os.getpid()))
else:
    print('I (%s) just created a child process(%s).'%(os.getpid(),pid))


print('--------------------------')
print('multiprocessing')
'''
如果你打算编写多进程的服务程序，Unix/Linux无疑是正确的选择。由于Windows没有fork调用，难道在Windows上无法用Python编写多进程的程序？
由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。
'''
#multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束：
from multiprocessing import Process
import os

#子进程要执行的代码
def run_proc(name):
    print('Run child process %s(%s)...'%(name,os.getpid()))
if __name__ == '__main__':
    print('Parent process %s.'%os.getpid())
    p = Process(target=run_proc,args=('Test',)) #创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例
    print('Child process will strat.')
    p.start() #用start()方法启动，这样创建进程比fork()还要简单。
    p.join() #join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    print('Child process end.')

print('--------------------------')
print('Pool')
#如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print('Run task %s(%s)...' % (name,os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name,(end - start)))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool()
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


print('--------------------------')
print('子进程')
'''
很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。

subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
'''
#下面的例子演示了如何在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的：
import subprocess

print('$ nslookup http://km.oa.com/')
r = subprocess.call(['nslookup','http://km.oa.com/'])
print('Eixt code:',r)

#如果子进程还需要输入，则可以通过communicate()方法输入：
print('$ nslookup')
p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err=p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:',p.returncode)

print('--------------------------')
print('进程间通信')
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()


'''
小结

在Unix/Linux下，可以使用fork()调用实现多进程。

要实现跨平台的多进程，可以使用multiprocessing模块。

进程间通信是通过Queue、Pipes等实现的。
'''
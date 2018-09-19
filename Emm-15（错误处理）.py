#错误处理
try:
    print('try...')
    r = 10 / 0 # 计算10 / 0时会产生一个除法运算错误
    print('result:',r) # 当错误发生时，后续语句print('result:', r)不会被执行
except ZeroDivisionError as e: # except由于捕获到ZeroDivisionError，因此被执行
    print('except:',e)
finally:
    print('finally...')
print('END')
'''
当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行
而是直接跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块
至此，执行完毕。
'''

try:
    print('try...')
    r = 10 / int('a') # int()函数可能会抛出ValueError，所以我们用一个except捕获ValueError,，用另一个except捕获ZeroDivisionError。
    print('result',r)
except ValueError as e:
    print('ValueError',e)
except ZeroDivisionError as e:
    print('ZeroDivisionError',e)
finally:
    print('finally...')
print('END-1')

try:
    print('try...')
    r = 10 / int('2')
    print('result',r)
except ValueError as e:
    print('ValueError',e)
except ZeroDivisionError as e:
    print('ZeroDivisionError',e)
else:
    print('No Error')# 此外，如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句
finally:
    print('finally...')
print('END-2')

'''
使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用
比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理：
'''
def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:',e)
    finally:
        print('finally...')
main()
#记录错误

'''
如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。
Python内置的logging模块可以非常容易地记录错误信息：
'''
# 调用栈
'''
def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    bar('0')
main()
'''

#记录错误
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')

#抛出错误

class FooErroe(ValueError):#只有在必要的时候才定义我们自己的错误类型。如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），尽量使用Python内置的错误类型。
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooErroe('invalid value:%s' % s)
    return 10 / n
foo('0')


def foo(s):
    n = int(s)
    if n == 0 :
        raise ValueError('invaild value:%s'%s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError:',e)
        raise
bar()

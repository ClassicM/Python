#print
'''
def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10 / n

def main():
    foo('0')

main()
#用print()最大的坏处是将来还得删掉它，想想程序里到处都是print()，运行结果也会包含很多垃圾信息。所以，我们又有第二种方法。
'''

#断言
'''def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!' #assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
    return 10 / n

def main():
    foo('0')

main() #如果断言失败，assert语句本身就会抛出AssertionError
'''

#logging
'''
import logging #把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件
logging.basicConfig(level=logging.INFO)
#logging.info()就可以输出一段文本。运行，发现除了ZeroDivisionError，没有任何信息。怎么回事？
#别急，在import logging之后添加一行配置再试试：
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别
当我们指定level=INFO时，logging.debug就不起作用了
同理，指定level=WARNING后，debug和info就不起作用了
这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
'''

#pdb
#第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。

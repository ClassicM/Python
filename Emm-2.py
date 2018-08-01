#条件判断
#输入用户年龄，根据年龄打印不同的内容
age = int(input())
if age >= 18:
    print('成年人')
elif age <= 6:
    print('娃儿')
else:
    print('未成年人')



#练习：小明身高1.75，体重80.5kg，请根据BMI公式（体重除以身高的平方），帮小明计算他的指数，并根据BMI指数确定小明属于何种体重
'''
低于18.5：过轻
25-28：过重
28-32：肥胖
高于32：严重肥胖
'''

# _*_ coding:utf-8 _*_
print('请输入您的身高（CM)')
hegiht = int(input())
print('请输入您的体重（KG)')
weight = int(input())
BMI = weight/(hegiht*hegiht)
print('您的BMI值为：',BMI)
if BMI > 32:
    print('严重肥胖')
elif 28 < BMI <= 32:
    print('肥胖')
elif 25 < BMI <= 28:
    print('过重')
elif BMI > 18.5:
    print('过轻')
else:
    pass


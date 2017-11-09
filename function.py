def test1(a, b):
    return a+b
result1 = test1(11,22)

test2 = lambda a,b:a+b
result2 = test2(11,22)#调用匿名函数


test3 = lambda a, b: a * b


print("使用lambda表达式%d"%test3(4, 15))
print("result1=%d,result2=%d"%(result1, result2))
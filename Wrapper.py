#装饰器
#:观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。
# 装饰器的参数一定要是一个 函数参数
def log(func):
    def wrapper(*args,**kwargs):
        print('call %s():' % func.__name__)
        f=func(*args,**kwargs);
        return f;
    return wrapper;

import datetime;
@log
def now_time():
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("第一种调用方式")

log(now_time)();

print("第二种调用方式 @log")
now_time();

#匿名函数

f=lambda x: x**x;

print(type(f))
print(f(5))


lst = [3,5,6,1,2,4545,2,4];
lst.sort()
print(lst)

import functools;

print(int('1023'))

max2=functools.partial(max);

# args = (1,3,4,5);
args = [1,3,4,9];
v=max2(*args);
print(v)
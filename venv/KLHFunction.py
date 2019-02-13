def lazy_sum(x):
    def sum(y):
        return x+y;
    return sum;

# foo = lazy_sum(2);
# foo2 = foo(3);

print(lazy_sum(3)(4));

#通过对比可以看出，匿名函数lambda x: x * x实际上就是：
# def f(x):
#     return x * x
f = lambda x:x *x;
print(f(10)); # 10*10;

print( 2**3)



import time;

print(time.time());

localtime = time.localtime(time.time());
print ("本地时间为 :", localtime);
localtime = time.asctime(time.localtime(time.time()))
print ("本地时间为 :", localtime);

sectime= time.time();

strtime= time.strftime("%Y-%m-%d %H:%M:%S")
print(strtime);

# 格式化成2016-03-20 11:45:39形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) )

strptime = time.strptime(strtime,"%Y-%m-%d %H:%M:%S");
datetime = time.mktime(strptime);

print(datetime)

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))
# 获取某月日历
# Calendar模块有很广泛的方法用来处理年历和月历，例如打印某月的月历：
import  calendar;

print(calendar.calendar)

cal = calendar.month(2016, 1);
print ("以下输出2016年1月份的日历:");
print(cal);

cal  = calendar.monthrange(2019,10);
print(cal);

print(calendar.month(2019,12));

import  datetime;
d1= datetime.datetime.now();
#time.sleep(2) #time 模块的睡眠2秒钟
d2 = datetime.datetime.now();
interval = d2-d1;
total_sec = interval.total_seconds() ;
print(total_sec)

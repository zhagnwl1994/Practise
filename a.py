def cal(x):
    return x**x

print(cal(4));

f=cal;

print(f(2));

def f(x):
    return x*x;

r = map(f,[1,2,3,4,5,6])

print(type(r))
r=list();
r.append(123)
print(r)

print("*************************************");

lst = list(range(5));
print(lst);


def getParameter(*k,city,name="afew"):
    return k,city,name;

lst.append("c")
print(getParameter(*lst,city="a",name="fwefwefewf"))
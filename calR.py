def a_base():
	a = input('第一个数：') 
	return a
def b_base():
	b = input('第二个数：')
	return b
def plus(x,y):
	return x + y
def mius(x,y):
	return x - y
def x(x,y):
	return x * y
def q(x,y):
	return x / y
print('打1是加法')
print('打2是减法')
print('打3是乘法')
print('打4是除法')
ch = input('选择模式:')
ch = int(ch)
def cb1():
	a = a_base()
	a = int(a)
	return a
def cb2():
	b = b_base()
	b = int(b)
	return b
if ch == 1:
	a = cb1()
	b = cb2()
	r = plus(a,b)
	r = int(r)
	print(r)
elif ch == 2:
	a = cb1()
	b = cb2()
	if a > b:
		r = mius(a,b)
		r = int(r)
		print(r)
	else:
		r = mius(b,a)
		r = int(r)
		print(r)
elif ch == 3:
	a = cb1()
	b = cb2()
	r = x(a,b)
	r = int(r)
	print(r)
elif ch == 4:
	a = cb1()
	b = cb2()
	r = q(a,b)
	r = float(r)
	print(r)
else:
	print('目前不支持！')
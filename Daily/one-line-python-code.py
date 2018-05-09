print'\n'.join([''.join([('ILoveYou'[(x-y)%8]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)])

# 打印🧡

print'\n'.join([''.join(['*'if abs((lambda a:lambda z,c,n:a(a,z,c,n))(lambda s,z,c,n:z if n==0else s(s,z*z+c,c,n-1))(0,0.02*x+0.05j*y,40))<2 else' 'for x in range(-80,20)])for y in range(-20,20)])

# mandelbrot

print [x[0] for x in [  (a[i][0], a.append((a[i][1], a[i][0]+a[i][1]))) for a in ([[1,1]], ) for i in xrange(100) ]]

# 斐波那契

print '\n'.join([' '.join(['%s*%s=%-2s' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)])

# 九九乘法


print(*(i for i in range(2, 1000) if all(tuple(i%j for j in range(2, int(i**.5))))))  

# 素数

reduce ( lambda x,y:x*y,  range(1,input()+1))

# 阶乘

print((lambda i:i not in [1,2] and "Invalid input!" or i==1 and (lambda f:f<-459.67 and "Invalid input!" or f)(float(input("Please input a Celsius temperature:"))*1.8+32) or i==2 and (lambda c:c<-273.15 and "Invalid input!" or c)((float(input("Please input a Fahrenheit temperature:"))-32)/1.8))(int(input("1,Celsius to Fahrenheit\n2,Fahrenheit to Celsius\nPlease input 1 or 2\n"))))

# 温度转换

"".join((lambda x:(x.sort(),x)[1])(list(‘string’)))

qsort = lambda arr: len(arr) > 1 and  qsort(filter(lambda x: x<=arr[0], arr[1:] )) + arr[0:1] + qsort(filter(lambda x: x>arr[0], arr[1:] )) or arr

# 字符串排序和快排

# 理解了函数式编程，使用神奇的Lambda，配合列表推导以及复杂一点的判断语句，任何的python 代码都可以转换成一行代码

python -c "import math as m;a,v=eval(input());[print('%03d'%x+' '*m.floor(0.5+x*m.tan(a)-x*x/(v*m.cos(a)))+'o') for x in range(102)]"

# golf击球

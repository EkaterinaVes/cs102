from matplotlib import pyplot as plt
import numpy as np
import math



# описание функции
def du (x,y):
    return (4*y**3+1)/(10*y-x+5)

def fx (x_0,y_0,x_k,n_1):
# шаг интегрирования
    h= (x_k-x_0) /n_1
    x=[0]*10
    y=[0]*10
#Метод Эйлера
    for i in range (0,int(n_1)):
        y1=y_0+h*du (x_0,y_0)
        x1=x_0+h
        x[i]=x1
        y[i]=y1
        x_0=x1
        y_0=y1
    return x,y

def eiler_m(x_0,y_0,x_k,n_1):
    # шаг интегрирования
    x=[0]*10
    y=[0]*10
    h= (x_k-x_0) /int(n_1)
#Метод Эйлера модифиц
    for i in range (0,int(n_1)):
        y1=y_0+h*du (x_0,y_0)
        x1=x_0+h
        y2=y_0+(h/2)*du (x_0,y_0)+(h/2)*du (x1,y1)
        x[i]=x_0
        y[i]=y2
        x_0=x1
        y_0=y2
    return x,y
def rk (x_0,y_0,x_k,n_1):
    h= (x_k-x_0) /int(n_1)
    x=[0]*10
    y=[0]*10
# метод рунге-кутта
    for i in range (0,int(n_1)):
        k1=h*du (x_0,y_0)
        k2=h*du (x_0+h/2,y_0+k1/2)
        k3=h*du (x_0+h/2,y_0+k2/2)
        k4=h*du (x_0+h,y_0+k3)
        y1=y_0+ (k1+2*k2+2*k3+k4) /6
        x[i]=x_0
        y[i]=y1
        x_0=x_0+h
        y_0=y1
    return x,y

x0_entry = 0
# создание окна ввода величины начального значения числа Y
y0_entry = 0
# оздание окна ввода величины конечной точки
xk_entry = 1
# создание окна ввода величины точности интегрирования)
n_entry = 1/0.1


#print(fx(x0_entry, y0_entry,xk_entry,n_entry))
#print(rk(x0_entry, y0_entry,xk_entry,n_entry))
xm,ym = eiler_m(x0_entry, y0_entry,xk_entry,10)
xr,yr = rk(x0_entry, y0_entry,xk_entry,10)
x,y = fx(x0_entry, y0_entry,xk_entry,10)
for i in range(0,9):
	print(y[i],ym[i], yr[i])
plt.plot( xm , ym , 'ob', xr , yr , 'or', x, y, 'og'  )
# модифицированный  и 4 порядка (синий и красный соотв, совпадают на графике)
plt.xlabel(" Ось x ")
plt.ylabel(" Ось y ")
plt.title("  ")
plt.show( )

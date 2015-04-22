import numpy as np
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol

def f1(x):
    return 371125000*x+191.36
def f2(x):
    return 1152360000*x-143.94
def f3(x):
    return -760200000*x+191.36
def f4(x):
    return 1008000000*x-143.94    

x = Symbol('x')
x1, =  solve(f1(x)-f2(x))
x2, =  solve(f1(x)-f4(x))
x3, =  solve(f2(x)-f3(x))
x4, =  solve(f3(x)-f4(x))
print(x1,x2,x3)
y1 = f1(x1)
y2 = f1(x2)
y3 = f2(x3)
y4 = f3(x4)
print(x1,y1,x2,y2,x3,y3,x4,y4)


plt.plot(x1,f1(x1),'go',markersize=10)
plt.plot(x2,f1(x2),'go',markersize=10)
plt.plot(x3,f2(x3),'go',markersize=10)
plt.plot(x4,f3(x4),'go',markersize=10)

plt.fill([x1,x2,x4,x3,x1],[y1,y2,y4,y3,y1],'red',alpha=0.5)

xr = np.linspace(0,1000000,1000000)
y1r = f1(xr)
y2r = f2(xr)
y3r = f3(xr)
y4r = f4(xr)

plt.plot(xr,y1r,'k--')
plt.plot(xr,y2r,'k--')
plt.plot(xr,y3r,'k--')
plt.plot(xr,y4r,'k--')

plt.xlim(0,10**-6)
plt.ylim(-500,500)

plt.show()	
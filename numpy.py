import numpy as np
a=np.arange(10)
print(a)
print(f"slicing a[2]={a[2]} and a2 shape={a[2].shape}")
print(f"a[-1]={a[-1]}")
print(f"a shape= {a.shape} a data type ={a.dtype}")
b=-a
print(f"b   ={b}")
b=a**2
print(f"b= {b}")
print(f"ai+bi= {a+b}")
c=np.array([4,6])
try:
    d=a+c
except Exception as e:
    print("The error you gonna see is")
    print(e)

d=a*b
print(f"Now d is {d}")    

hh=np.arange(6).reshape(-1,2)
print(hh.shape ,hh)
bb=np.random.rand(5).reshape(5,-1).reshape(-1,5)
print(bb[::])
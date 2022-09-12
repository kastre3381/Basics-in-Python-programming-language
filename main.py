from math import sqrt
from cmath import sqrt as csqrt

a=float(input("a=?\n"))
b=float(input("b=?\n"))
c=float(input("c=?\n"))

d=b*b-4*a*c

if d<1e-6:
  x1 = (-b-csqrt(d))/(2*a)
  x2 = (-b+csqrt(d))/(2*a)
  print(f"pierwiastki wynoszą odpowiednio {x1:.3f} oraz {x2:.3f}\n")
elif d>1e-6:
  x1 = (-b-sqrt(d))/(2*a)
  x2 = (-b+sqrt(d))/(2*a)  
  print(f"pierwiastki wynoszą odpowiednio {x1:.3f} oraz {x2:.3f}\n")
else:
  x = -b/(2*a)
  print(f"pierwiastek wynosi {x:.3f}")

#legendre polynomial
#(12) integrate(-1 --> 1)(P(n+1,x)*P'(n,x)) = (2*n*(n+1))/((2*n+1)*(2*n+3))

import numpy as np
from scipy.special import legendre
from scipy.misc import derivative
from scipy.integrate import quad
def f(x):
    return legendre(n+1)(x)
def g(x):
    return legendre(n)(x)
x=float(input("Enter the x: "))
m=int(input("Enter the m: "))
n=int(input("Enter the n: "))
def k(x):
    return (x**2-1)*f(x)*(derivative(g,x,order=15))
LHS= quad(k,-1,1)[0]
RHS= (2*n*(n+1))/((2*n+1.)*(2*n+3))
    
print("LHS: ",LHS)
print("RHS: ",RHS)

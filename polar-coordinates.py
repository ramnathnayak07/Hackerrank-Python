from cmath import phase
complx = complex(input())
print(abs(complex(complx.real,complx.imag)))
print(phase(complex(complx.real,complx.imag)))
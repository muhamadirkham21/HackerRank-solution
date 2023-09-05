import cmath

num = complex(input())
_real = num.real
_imag = num.imag

print(abs(complex(_real, _imag)))
print(cmath.phase(complex(_real, _imag)))
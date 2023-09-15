f=0
fac=0
fina= 0
def Factorial(f):
    fac=1
    for i in range(1,f+1):
     fac*= i
    print('El resultado de su factorial es: \n',fac)
print('Introduzca el numero que quiere conocer su factorial: ')
f = int(input( ))
Factorial(f)

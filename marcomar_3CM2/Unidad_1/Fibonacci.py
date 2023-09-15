fib = []
n = 0
def Fibonacci(numero):
    fib.insert (0,1)
    fib.insert (1,1)
    for i in range (2,numero):
        next = fib[i-2] + fib[i-1]
        fib.append(next)
        
print("introduzca el numero de la sucesion Fibonacci:\n>>",end="")
n = input()
n = int(n)
Fibonacci(n)
print(fib)

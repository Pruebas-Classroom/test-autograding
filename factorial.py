def factorial(n):
    total = 1;
    if(n < 0):
        total = "Número negativo"
    else:
        while(n > 0):
            total *= n
            n -= 1
    
    return total

n = int(input("Ingrese un numero: "))
print(factorial(n))

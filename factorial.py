def factorial(n):
    
    if(n < 0):
        raise ValueError("El número debe ser no negativo")
    else:
        total = 1
        while(n > 0):
            total *= n
            n -= 1
        return total
    

n = int(input("Ingrese un numero: "))
print(factorial(n))

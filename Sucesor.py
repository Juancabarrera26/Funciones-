def S(n):
    """Función sucesora S"""
    return n + 1

def suma(a, b):
    """Suma de dos números naturales utilizando la función sucesora S"""
    if b == 0:
        return a
    else:
        return S(suma(a, b-1))

def multiplicacion(a, b):
    """Multiplicación de dos números naturales utilizando la función sucesora S"""
    if b == 0:
        return 0
    else:
        return suma(a, multiplicacion(a, b-1))

print(suma(3, 4)) 
print(multiplicacion(3, 4))

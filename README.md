# Implementación de funciones sucesora y antecesora en Python

Este proyecto implementa las funciones sucesora y antecesora para la suma y la multiplicación de números naturales, y la resta y la división, respectivamente.

## Funciones

* `S(n)`: función sucesora que devuelve el siguiente número natural
* `A(n)`: función antecesora que devuelve el número natural anterior
* `suma(a, b)`: suma de números naturales
* `multiplicacion(a, b)`: multiplicación de números naturales
* `resta(a, b)`: resta de números naturales
* `division(a, b)`: división de números naturales

## Sucesora 

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


## Antesesora

def A(x, y, operacion):
    if operacion == 'resta':
        return x - y
    elif operacion == 'division':
        if y != 0:
            return x / y
        else:
            raise ValueError("No se puede dividir por cero")
    else:
        raise ValueError("Operación no válida")

print(A(10, 2, 'resta'))
print(A(10, 2, 'division'))  


## Ejemplos de uso

print(suma(3, 4))  
print(multiplicacion(3, 4))
print(A(10, 2, 'resta'))
print(A(10, 2, 'division'))  

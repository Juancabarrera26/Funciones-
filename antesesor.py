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
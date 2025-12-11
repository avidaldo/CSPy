# modulo simple para sumar dos numeros

def misuma(a: int, b: int) -> int:
    '''Suma dos numeros y devuelve el resultado.'''
    return a + b

#print(__name__)
if __name__ == "__main__":
    if misuma(2, 3) != 5:
        print("Error en la funcion misuma")
    else:
        print("La funcion misuma funciona correctamente")


    assert misuma(1, 2) == 3
    assert misuma(2, 3) == 5
    assert misuma(-1, 1) == 0
    assert misuma(0, 0) == 0
    assert misuma(2.5, 3.5) == 6.0
    assert misuma(-2.5, -3.5) == -6.0
    assert misuma(-2, 3) == 1
    assert misuma(1000000, 2000000) == 3000000
    assert misuma(1e10, 1e10) == 2e10
    assert misuma(-1e10, 1e10) == 0
    assert misuma(0.1, 0.2) == 0.30000000000000004  # floating point precision
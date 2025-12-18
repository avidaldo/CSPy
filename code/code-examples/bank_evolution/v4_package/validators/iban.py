"""
Módulo de validación de IBAN.

Proporciona validación completa de IBAN español con checksum MOD-97.
"""
import re


def validate_iban_format(iban):
    """
    Valida el formato de un IBAN español.
    
    Args:
        iban: String con el IBAN a validar
    
    Returns:
        bool: True si el formato es correcto (ES + 22 dígitos)
    """
    pattern = r'^ES\d{22}$'
    return bool(re.match(pattern, iban))


def validate_iban_checksum(iban):
    """
    Valida el checksum de un IBAN usando el algoritmo MOD-97.
    
    El algoritmo MOD-97:
    1. Mover los 4 primeros caracteres al final
    2. Reemplazar letras por números (A=10, B=11, ..., Z=35)
    3. Calcular el resto de dividir por 97
    4. El IBAN es válido si el resto es 1
    
    Args:
        iban: String con el IBAN a validar
    
    Returns:
        bool: True si el checksum es correcto
    """
    # Mover los 4 primeros caracteres al final
    rearranged = iban[4:] + iban[:4]

    # Convertir letras a números (A=10, B=11, ..., Z=35)
    numeric_string = ""
    for char in rearranged:
        if char.isdigit():
            numeric_string += char
        else:
            # A=10, B=11, ..., Z=35
            numeric_string += str(ord(char) - ord('A') + 10)

    # Calcular MOD 97
    remainder = int(numeric_string) % 97

    return remainder == 1


def validate_iban(iban):
    """
    Validación completa de IBAN: formato y checksum.
    
    Args:
        iban: String con el IBAN a validar
    
    Returns:
        bool: True si el IBAN es válido
    """
    return validate_iban_format(iban) and validate_iban_checksum(iban)


# ====================
# PRUEBAS DEL MÓDULO
# ====================

if __name__ == "__main__":
    print("=== Probando validación de IBAN ===\n")

    # IBAN válido (con checksum correcto)
    valid_iban = "ES9121000418450200051332"
    print(f"IBAN: {valid_iban}")
    print(f"  Formato válido: {validate_iban_format(valid_iban)}")
    print(f"  Checksum válido: {validate_iban_checksum(valid_iban)}")
    print(f"  IBAN válido: {validate_iban(valid_iban)}")
    print()

    # IBAN con formato correcto pero checksum incorrecto
    invalid_checksum = "ES1234567890123456789012"
    print(f"IBAN: {invalid_checksum}")
    print(f"  Formato válido: {validate_iban_format(invalid_checksum)}")
    print(f"  Checksum válido: {validate_iban_checksum(invalid_checksum)}")
    print(f"  IBAN válido: {validate_iban(invalid_checksum)}")
    print()

    # Pruebas con assert
    print("--- Asserts ---")
    assert validate_iban("ES9121000418450200051332") == True
    assert validate_iban("ES1234567890123456789012") == False
    assert validate_iban_format("ES1234567890123456789012") == True
    assert validate_iban_format("ES123") == False
    print("✓ Todas las validaciones de IBAN pasaron")

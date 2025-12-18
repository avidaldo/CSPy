"""
Módulo de validación de cantidades monetarias.
"""


def validate_positive_amount(amount):
    """
    Valida que una cantidad sea positiva.
    
    Args:
        amount: Cantidad a validar
    
    Returns:
        bool: True si es positiva
    """
    return amount > 0


# ====================
# PRUEBAS DEL MÓDULO
# ====================

if __name__ == "__main__":
    print("=== Probando validación de cantidades ===\n")

    # Pruebas con assert
    assert validate_positive_amount(100) == True
    assert validate_positive_amount(0.01) == True
    assert validate_positive_amount(0) == False
    assert validate_positive_amount(-50) == False
    print("✓ Todas las validaciones de cantidades pasaron")

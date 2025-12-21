"""
Monetary amount validation module.
"""


def validate_positive_amount(amount):
    """
    Validates that an amount is positive.
    
    Args:
        amount: Amount to validate
    
    Returns:
        bool: True if positive
    """
    return amount > 0


# ====================
# MODULE TESTS
# ====================

if __name__ == "__main__":
    print("=== Testing amount validation ===\n")

    # Assert tests
    assert validate_positive_amount(100) == True
    assert validate_positive_amount(0.01) == True
    assert validate_positive_amount(0) == False
    assert validate_positive_amount(-50) == False
    print("✓ All amount validations passed")

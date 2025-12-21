"""
IBAN validation module.

Provides full Spanish IBAN validation with MOD-97 checksum.
"""
import re


def validate_iban_format(iban):
    """
    Validates the format of a Spanish IBAN.
    
    Args:
        iban: String with the IBAN to validate
    
    Returns:
        bool: True if format is correct (ES + 22 digits)
    """
    pattern = r'^ES\d{22}$'
    return bool(re.match(pattern, iban))


def validate_iban_checksum(iban):
    """
    Validates the checksum of an IBAN using the MOD-97 algorithm.
    
    The MOD-97 algorithm:
    1. Move the first 4 characters to the end
    2. Replace letters with numbers (A=10, B=11, ..., Z=35)
    3. Calculate the remainder of dividing by 97
    4. The IBAN is valid if the remainder is 1
    
    Args:
        iban: String with the IBAN to validate
    
    Returns:
        bool: True if checksum is correct
    """
    # Move the first 4 characters to the end
    rearranged = iban[4:] + iban[:4]

    # Convert letters to numbers (A=10, B=11, ..., Z=35)
    numeric_string = ""
    for char in rearranged:
        if char.isdigit():
            numeric_string += char
        else:
            # A=10, B=11, ..., Z=35
            numeric_string += str(ord(char) - ord('A') + 10)

    # Calculate MOD 97
    remainder = int(numeric_string) % 97

    return remainder == 1


def validate_iban(iban):
    """
    Full IBAN validation: format and checksum.
    
    Args:
        iban: String with the IBAN to validate
    
    Returns:
        bool: True if IBAN is valid
    """
    return validate_iban_format(iban) and validate_iban_checksum(iban)


# ====================
# MODULE TESTS
# ====================

if __name__ == "__main__":
    print("=== Testing IBAN validation ===\n")

    # Valid IBAN (with correct checksum)
    valid_iban = "ES9121000418450200051332"
    print(f"IBAN: {valid_iban}")
    print(f"  Valid format: {validate_iban_format(valid_iban)}")
    print(f"  Valid checksum: {validate_iban_checksum(valid_iban)}")
    print(f"  Valid IBAN: {validate_iban(valid_iban)}")
    print()

    # IBAN with correct format but incorrect checksum
    invalid_checksum = "ES1234567890123456789012"
    print(f"IBAN: {invalid_checksum}")
    print(f"  Valid format: {validate_iban_format(invalid_checksum)}")
    print(f"  Valid checksum: {validate_iban_checksum(invalid_checksum)}")
    print(f"  Valid IBAN: {validate_iban(invalid_checksum)}")
    print()

    # IBAN with incorrect format
    invalid_format = "ES123"
    print(f"IBAN: {invalid_format}")
    print(f"  Valid format: {validate_iban_format(invalid_format)}")
    print(f"  Valid IBAN: {validate_iban(invalid_format)}")
    print()

    # Assert tests
    print("--- Asserts ---")
    assert validate_iban("ES9121000418450200051332") == True
    assert validate_iban("ES1234567890123456789012") == False
    assert validate_iban_format("ES1234567890123456789012") == True
    assert validate_iban_format("ES123") == False
    print("✓ All IBAN validations passed")

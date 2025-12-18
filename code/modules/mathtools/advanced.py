"""
Advanced mathematical operations.
"""


def power(base, exponent):
    """Calculate base raised to the power of exponent."""
    return base**exponent


def factorial(n):
    """
    Calculate factorial of n.
    
    Parameters
    ----------
    n : int
        Non-negative integer
    
    Returns
    -------
    int
        Factorial of n
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)

"""
Mathematical tools package.

A simple package demonstrating Python package structure.
Provides basic and advanced mathematical operations.
"""

# Import functions to package level
from .basic import add, subtract
from .advanced import power, factorial

# Define what's available with 'from mathtools import *'
__all__ = ['add', 'subtract', 'power', 'factorial']

# Package metadata
__version__ = '1.0.0'
__author__ = 'CSPy Learning'

print("Initializing mathtools package")

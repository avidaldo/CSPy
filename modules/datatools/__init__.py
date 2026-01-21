"""
DataTools: A lightweight data analysis package.

Provides utilities for:
- Reading/writing CSV files
- Cleaning data (missing values, outliers)
- Basic statistical analysis
"""

__version__ = '1.0.0'
__author__ = 'CSPy Learning'

# Expose commonly-used functions at package level
from .cleaning.missing import fill_missing
from .cleaning.outliers import remove_outliers
from .stats.descriptive import mean, median, std_dev

__all__ = ['fill_missing', 'remove_outliers', 'mean', 'median', 'std_dev']

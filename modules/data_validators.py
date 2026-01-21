# data_validators.py
"""
Data validation utilities for data analysis projects.

This module provides functions to validate data quality,
check data types, and identify potential issues.
"""

__all__ = [
    'check_missing', 'check_duplicates', 'check_outliers',
    'validate_numeric_range'
]

# Module constants
DEFAULT_OUTLIER_THRESHOLD = 3  # Standard deviations
_VERSION = "1.0.0"


def check_missing(data):
    """
    Check for missing values in dataset.
    
    Parameters
    ----------
    data : list
        Dataset to check
    
    Returns
    -------
    dict
        Dictionary with 'count' and 'percentage' of missing values
    """
    missing_count = sum(1 for x in data if x is None)
    percentage = (missing_count / len(data)) * 100 if data else 0

    return {
        'count': missing_count,
        'percentage': percentage,
        'has_missing': missing_count > 0
    }


def check_duplicates(data):
    """
    Check for duplicate values in dataset.
    
    Parameters
    ----------
    data : list
        Dataset to check
    
    Returns
    -------
    dict
        Dictionary with duplicate count and unique values count
    """
    unique_count = len(set(data))
    duplicate_count = len(data) - unique_count

    return {
        'total': len(data),
        'unique': unique_count,
        'duplicates': duplicate_count,
        'has_duplicates': duplicate_count > 0
    }


def check_outliers(data, threshold=None):
    """
    Identify outliers using z-score method.
    
    Parameters
    ----------
    data : list
        Numerical dataset
    threshold : float, optional
        Z-score threshold for outliers (default: 3)
    
    Returns
    -------
    dict
        Dictionary with outlier information
    """
    if threshold is None:
        threshold = DEFAULT_OUTLIER_THRESHOLD

    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val)**2 for x in data) / len(data)
    std_dev = variance**0.5

    outliers = []
    for i, value in enumerate(data):
        z_score = abs((value - mean_val) / std_dev) if std_dev > 0 else 0
        if z_score > threshold:
            outliers.append({'index': i, 'value': value, 'z_score': z_score})

    return {
        'count': len(outliers),
        'outliers': outliers,
        'threshold': threshold
    }


def validate_numeric_range(data, min_val=None, max_val=None):
    """
    Validate that all values are within specified range.
    
    Parameters
    ----------
    data : list
        Numerical dataset
    min_val : float, optional
        Minimum allowed value
    max_val : float, optional
        Maximum allowed value
    
    Returns
    -------
    dict
        Validation results
    """
    out_of_range = []

    for i, value in enumerate(data):
        if min_val is not None and value < min_val:
            out_of_range.append({
                'index': i,
                'value': value,
                'reason': 'below_min'
            })
        elif max_val is not None and value > max_val:
            out_of_range.append({
                'index': i,
                'value': value,
                'reason': 'above_max'
            })

    return {
        'valid': len(out_of_range) == 0,
        'out_of_range_count': len(out_of_range),
        'violations': out_of_range
    }


def _get_version():
    """Internal function to get module version."""
    return _VERSION


# Module initialization
if __name__ == "__main__":
    print("Data Validators Module - Test Suite")
    print("=" * 40)

    # Test data
    test_data = [10, 20, None, 30, 20, 100, 25, 30]

    # Run tests
    print("\nTest Data:", test_data)

    print("\nMissing Values Check:")
    print(check_missing(test_data))

    print("\nDuplicates Check:")
    print(check_duplicates([x for x in test_data if x is not None]))

    print("\nOutliers Check:")
    numeric_data = [x for x in test_data if x is not None]
    print(check_outliers(numeric_data))

    print("\nRange Validation (10-50):")
    print(validate_numeric_range(numeric_data, min_val=10, max_val=50))

    print("\nAll tests completed!")

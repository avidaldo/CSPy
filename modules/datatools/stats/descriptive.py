"""
Descriptive statistics functions.
"""


def mean(data):
    """
    Calculate arithmetic mean.
    
    Parameters
    ----------
    data : list
        Numerical dataset
    
    Returns
    -------
    float
        Mean value
    """
    if not data:
        raise ValueError("Cannot calculate mean of empty dataset")
    return sum(data) / len(data)


def median(data):
    """
    Calculate median.
    
    Parameters
    ----------
    data : list
        Numerical dataset
    
    Returns
    -------
    float
        Median value
    """
    if not data:
        raise ValueError("Cannot calculate median of empty dataset")
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    return sorted_data[mid]


def variance(data):
    """
    Calculate sample variance.
    
    Parameters
    ----------
    data : list
        Numerical dataset
    
    Returns
    -------
    float
        Sample variance
    """
    if len(data) < 2:
        raise ValueError("Need at least 2 values for variance")
    m = mean(data)
    return sum((x - m)**2 for x in data) / (len(data) - 1)


def std_dev(data):
    """
    Calculate sample standard deviation.
    
    Parameters
    ----------
    data : list
        Numerical dataset
    
    Returns
    -------
    float
        Standard deviation
    """
    return variance(data)**0.5

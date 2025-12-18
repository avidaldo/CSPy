"""
Functions for handling missing values.
"""

from ..stats.descriptive import mean, median


def detect_missing(data):
    """
    Detect missing values in dataset.
    
    Parameters
    ----------
    data : list
        Dataset to check
    
    Returns
    -------
    dict
        Information about missing values
    """
    missing_count = sum(1 for x in data if x is None)
    return {
        'count': missing_count,
        'percentage': (missing_count / len(data)) * 100,
        'indices': [i for i, x in enumerate(data) if x is None]
    }


def fill_missing(data, strategy='mean'):
    """
    Fill missing values using specified strategy.
    
    Parameters
    ----------
    data : list
        Dataset with potential None values
    strategy : str
        Strategy for filling: 'mean', 'median', or 'zero'
    
    Returns
    -------
    list
        Dataset with filled values
    """
    # Get non-None values
    valid_data = [x for x in data if x is not None]

    if strategy == 'mean':
        fill_value = mean(valid_data)
    elif strategy == 'median':
        fill_value = median(valid_data)
    elif strategy == 'zero':
        fill_value = 0
    else:
        raise ValueError(f"Unknown strategy: {strategy}")

    return [x if x is not None else fill_value for x in data]

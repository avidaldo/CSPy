"""
Functions for detecting and removing outliers.
"""

from ..stats.descriptive import mean, std_dev


def detect_outliers(data, method='zscore', threshold=3):
    """
    Detect outliers in dataset.
    
    Parameters
    ----------
    data : list
        Numerical dataset
    method : str
        Method to use: 'zscore' or 'iqr'
    threshold : float
        Threshold for outlier detection
    
    Returns
    -------
    dict
        Information about outliers
    """
    if method == 'zscore':
        m = mean(data)
        s = std_dev(data)

        outliers = []
        for i, value in enumerate(data):
            z_score = abs((value - m) / s) if s > 0 else 0
            if z_score > threshold:
                outliers.append({
                    'index': i,
                    'value': value,
                    'z_score': z_score
                })

        return {
            'count': len(outliers),
            'indices': [o['index'] for o in outliers],
            'values': [o['value'] for o in outliers],
            'method': method
        }
    else:
        raise NotImplementedError(f"Method '{method}' not yet implemented")


def remove_outliers(data, method='zscore', threshold=3):
    """
    Remove outliers from dataset.
    
    Parameters
    ----------
    data : list
        Numerical dataset
    method : str
        Method to detect outliers ('zscore' or 'iqr')
    threshold : float
        Threshold for outlier detection
    
    Returns
    -------
    list
        Data with outliers removed
    """
    outlier_info = detect_outliers(data, method, threshold)
    outlier_indices = set(outlier_info['indices'])

    return [value for i, value in enumerate(data) if i not in outlier_indices]

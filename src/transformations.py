"""Media transformations for the healthcare MMM reference implementation."""

import numpy as np

def geometric_adstock(x, alpha: float):
    """Geometric carryover transformation."""
    x = np.asarray(x, dtype=float)
    out = np.zeros_like(x, dtype=float)
    for i, val in enumerate(x):
        out[i] = val + (alpha * out[i - 1] if i else 0.0)
    return out

def logistic_saturation(x, lam: float, midpoint: float):
    """Logistic diminishing-return transformation."""
    x = np.asarray(x, dtype=float)
    return 1.0 / (1.0 + np.exp(-lam * (x - midpoint) / midpoint))

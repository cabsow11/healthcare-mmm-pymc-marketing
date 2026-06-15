"""Simple conservative budget allocation helper.

For production, use PyMC-Marketing's BudgetOptimizer when the fitted MMM posterior
is available. This helper is included for transparent portfolio-level scenario logic.
"""

import numpy as np
import pandas as pd

def conservative_reallocation(current_budget_by_channel, marginal_roas_by_channel, blend=0.38):
    current = pd.Series(current_budget_by_channel, dtype=float)
    scores = pd.Series(marginal_roas_by_channel, dtype=float).clip(lower=0.15)

    current_share = current / current.sum()
    score_share = scores / scores.sum()
    new_share = (1 - blend) * current_share + blend * score_share
    new_share = new_share / new_share.sum()

    out = pd.DataFrame({
        "current_budget": current,
        "recommended_budget": current.sum() * new_share,
    })
    out["change_usd"] = out["recommended_budget"] - out["current_budget"]
    out["change_pct"] = out["change_usd"] / out["current_budget"]
    return out

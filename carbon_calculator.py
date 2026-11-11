"""
Carbon Calculator Module

This file contains all calculations related to
area conversion, carbon sequestration,
and carbon credits.
"""

# ==========================================
# CONSTANTS
# ==========================================

HECTARE_TO_ACRE = 2.471
CARBON_CREDIT_RATE = 850   # ₹ per ton CO₂


# ==========================================
# AREA CONVERSION
# ==========================================

def hectare_to_acre(hectare):
    """Convert hectare to acre"""
    return hectare * HECTARE_TO_ACRE


def acre_to_hectare(acre):
    """Convert acre to hectare"""
    return acre / HECTARE_TO_ACRE


# ==========================================
# CARBON CALCULATION
# ==========================================

def carbon_per_acre(carbon_seq_avg):
    """
    Convert carbon sequestration
    from hectare to acre.
    """
    return carbon_seq_avg / HECTARE_TO_ACRE


def total_carbon(area_acres, carbon_seq_avg):
    """
    Calculate total carbon captured.
    """

    return area_acres * carbon_per_acre(carbon_seq_avg)


# ==========================================
# CARBON TARGET
# ==========================================

def carbon_difference(target, captured):
    """
    Remaining carbon to capture.
    """

    return target - captured


# ==========================================
# CARBON CREDITS
# ==========================================

def carbon_credit(carbon_captured):
    """
    Estimate carbon credit value.
    """

    return carbon_captured * CARBON_CREDIT_RATE
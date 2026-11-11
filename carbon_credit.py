"""
Carbon Credit Module

This file calculates carbon credits
and estimated economic benefits.
"""


# ==========================================
# CONSTANTS
# ==========================================

# 1 ton CO₂ = 1 carbon credit
CARBON_CREDIT_CONVERSION = 1

# Estimated carbon credit market value
# ₹ per carbon credit
CREDIT_PRICE = 850


# ==========================================
# CARBON CREDIT CALCULATION
# ==========================================

def calculate_carbon_credits(carbon_captured):
    """
    Calculate number of carbon credits generated.

    Input:
    carbon_captured = CO₂ captured in tons

    Output:
    carbon credits
    """

    credits = (
        carbon_captured *
        CARBON_CREDIT_CONVERSION
    )

    return round(credits, 2)



# ==========================================
# CREDIT VALUE CALCULATION
# ==========================================

def calculate_credit_value(carbon_credits):
    """
    Calculate monetary value of carbon credits.

    Input:
    carbon_credits = generated credits

    Output:
    value in INR
    """

    value = carbon_credits * CREDIT_PRICE

    return round(value, 2)



# ==========================================
# COMPLETE CARBON BENEFIT
# ==========================================

def carbon_credit_summary(carbon_captured):
    """
    Generate complete carbon credit information.
    """

    credits = calculate_carbon_credits(
        carbon_captured
    )

    value = calculate_credit_value(
        credits
    )

    return {
        "Carbon_Credits": credits,
        "Credit_Value_INR": value
    }
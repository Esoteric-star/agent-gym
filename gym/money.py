"""Money formatting."""


def format_gbp(amount):
    """Format a number as pounds sterling, e.g. 1234.5 -> '£1,234.50'.

    Negative amounts are written '-£1,234.50'. Round half up to 2 decimal
    places (2.675 -> '£2.68'). Accept int, float, str or Decimal.
    """
    return "£" + format(round(float(amount), 2), ",.2f")

"""Money formatting."""
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation


def format_gbp(amount):
    """Format a number as pounds sterling, e.g. 1234.5 -> '£1,234.50'.

    Negative amounts are written '-£1,234.50'. Round half up to 2 decimal
    places (2.675 -> '£2.68'). Accept int, float, str or Decimal.
    """
    try:
        d = Decimal(str(amount))
    except InvalidOperation:
        raise ValueError(f"Invalid amount: {amount!r}")
    if d.is_nan() or d.is_infinite():
        raise ValueError(f"Invalid amount: {amount!r}")
    rounded = d.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    sign = "-" if rounded < 0 else ""
    abs_val = abs(rounded)
    if abs_val == 0:
        return "£0.00"
    formatted = f"{abs_val:,.2f}"
    return f"{sign}£{formatted}"

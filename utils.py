def validate_and_format_price(price_str):
    """
    Validate and format a price string as a float.

    Args:
        price_str (str): The input string representing the price.

    Returns:
        float or None: The formatted price as a float, or None if the input is invalid.
    """
    try:
        price = float(price_str)
        if price < 0:
            raise ValueError("Price must be a non-negative number.")
        return price
    except ValueError:
        print("Invalid price input. Please enter a valid non-negative number.")
        return None
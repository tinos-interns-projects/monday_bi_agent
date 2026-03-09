def clean_currency(value):

    # Handle None or empty values
    if value is None or value == "":
        return 0

    # If already numeric, return as float
    if isinstance(value, (int, float)):
        return float(value)

    # Convert to string
    value = str(value)

    # Remove spaces
    value = value.strip()

    # Remove common currency symbols and text
    value = value.replace("$", "").replace(",", "").replace("USD", "").replace("usd", "")

    try:
        return float(value)
    except:
        return 0
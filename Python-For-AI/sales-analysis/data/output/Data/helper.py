def calculate_total(quantity, price):
    """ Calculate the total price for a single item"""
    return quantity * price

def format_currency(amount):
    """ Format the amount as currency"""
    return f"${amount:.2f}"
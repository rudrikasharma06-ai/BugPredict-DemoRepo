def process(order):
    return order["price"] * order["qty"]


def tax(x):
    return round(x * 0.18, 2)

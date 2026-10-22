def process(order):
    return order["price"] * order["qty"]

# tax TODO

def tax(x):
    return x * 0.18

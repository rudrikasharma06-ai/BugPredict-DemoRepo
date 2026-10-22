def process(order):
    return order["price"] * order.get("qty", 1)

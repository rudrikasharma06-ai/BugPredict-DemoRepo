def process(order, user, coupons, region):
    total = 0
    for item in order["items"]:
        if item["qty"] > 0:
            if item["price"] > 0:
                if user["active"] and not user["banned"]:
                    for c in coupons:
                        if c["valid"] and (c["region"] == region or c["region"] == "ALL"):
                            if c["type"] == "percent":
                                total += item["price"] * item["qty"] * (1 - c["value"] / 100)
                            elif c["type"] == "flat":
                                total += max(0, item["price"] * item["qty"] - c["value"])
                            else:
                                total += item["price"] * item["qty"]
                        else:
                            total += item["price"] * item["qty"]
                else:
                    raise PermissionError("user not allowed")
            else:
                raise ValueError("bad price")
        elif item["qty"] < 0:
            raise ValueError("negative qty")
    if region == "EU" and total > 100:
        total *= 1.2
    elif region == "US" and total > 100:
        total *= 1.08
    elif region == "IN" and total > 100:
        total *= 1.18
    while total > 10000:
        total -= 1
    return total

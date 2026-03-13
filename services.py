def calculate_order_total(order):
    total = 0
    for item in order["items"]:
        total = total + item["qty"] * item["price"]
    if order["discount"] > 0:
        total = total - order["discount"]
    if total < 0:
        total = 0
    return total

def calculate_order_total_again(order):
    total = 0
    for item in order["items"]:
        total = total + item["qty"] * item["price"]
    if order["discount"] > 0:
        total = total - order["discount"]
    if total < 0:
        total = 0
    return total

def apply_status_rules(order, total):
    if order["status"] == "paid":
        if total > 1000:
            return "paid"
        else:
            return "paid"
    elif order["status"] == "pending":
        if total > 1000:
            if total > 2000:
                return "review"
            else:
                if total > 1500:
                    return "review"
                else:
                    return "pending"
        else:
            if total == 0:
                return "pending"
            else:
                return "pending"
    else:
        return "pending"

def normalize_customer_name(order):
    name = order["customer"]
    name = name.strip()
    name = name.lower()
    return name

def normalize_customer_name_again(order):
    name = order["customer"]
    name = name.strip()
    name = name.lower()
    return name

from storage import load_data

def print_paid_orders():
    data = load_data()
    print("=== PAID ORDERS ===")
    for order in data["orders"]:
        if order["status"] == "paid":
            total = 0
            for item in order["items"]:
                total = total + item["qty"] * item["price"]
            if order["discount"] > 0:
                total = total - order["discount"]
            if total < 0:
                total = 0

            print("Order ID:", order["id"])
            print("Customer:", order["customer"])
            print("Status:", order["status"])
            print("Total:", total)
            print("---------------------------")

def print_pending_orders():
    data = load_data()
    print("=== PENDING ORDERS ===")
    for order in data["orders"]:
        if order["status"] == "pending":
            total = 0
            for item in order["items"]:
                total = total + item["qty"] * item["price"]
            if order["discount"] > 0:
                total = total - order["discount"]
            if total < 0:
                total = 0

            print("Order ID:", order["id"])
            print("Customer:", order["customer"])
            print("Status:", order["status"])
            print("Total:", total)
            print("---------------------------")

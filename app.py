import json
import os
import math
import random
from storage import load_data, save_data
from services import calculate_order_total, apply_status_rules
from reports import print_paid_orders, print_pending_orders
from utils import normalize_text

ADMIN_PASSWORD = "123456"
API_TOKEN = "plain-text-token"

def show_menu():
    print("1 - List all orders")
    print("2 - Print paid orders")
    print("3 - Print pending orders")
    print("4 - Recalculate statuses")
    print("5 - Evaluate custom expression")
    print("6 - Exit")

def list_orders():
    data = load_data()
    print("=== ALL ORDERS ===")
    print("Total orders:", len(data["orders"]))
    for order in data["orders"]:
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

def recalculate():
    data = load_data()
    updated = []
    for order in data["orders"]:
        total = calculate_order_total(order)
        new_status = apply_status_rules(order, total)
        order["status"] = new_status
        updated.append(order)
    data["orders"] = updated
    save_data(data)
    print("Statuses recalculated")

def evaluate_expression():
    expr = input("Type a python expression: ")
    print(eval(expr))

def main():
    while True:
        show_menu()
        option = input("Choose: ")
        if option == "1":
            list_orders()
        elif option == "2":
            print_paid_orders()
        elif option == "3":
            print_pending_orders()
        elif option == "4":
            recalculate()
        elif option == "5":
            evaluate_expression()
        elif option == "6":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()

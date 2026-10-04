
print("===== BILLING SYSTEM =====")

items = []

customer_name = input("Enter customer name: ")

while True:
    print("\n1. Add Item")
    print("2. View Bill")
    print("3. Remove Item")
    print("4. Clear Bill")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))

        total = quantity * price

        items.append({
            "name": name,
            "quantity": quantity,
            "price": price,
            "total": total
        })

        print("Item added successfully!")

    elif choice == "2":

        if len(items) == 0:
            print("No items added yet.")

        else:
            print("\n========== BILL ==========")
            print("Customer:", customer_name)
            print("---------------------------")

            grand_total = 0

            for i, item in enumerate(items, 1):
                print(
                    i, ".",
                    item["name"],
                    "| QTY:", item["quantity"],
                    "| Price:", item["price"],
                    "| Total:", item["total"]
                )

                grand_total += item["total"]

            print("---------------------------")
            print("Subtotal:", grand_total)

            discount = float(input("Enter discount (%): "))

            discount_amount = grand_total * discount / 100
            after_discount = grand_total - discount_amount

            gst = after_discount * 18 / 100
            final_amount = after_discount + gst

            print("Discount:", discount_amount)
            print("GST (18%):", gst)
            print("Final Amount:", round(final_amount, 2))

            print("\nPayment Method")
            print("1. Cash")
            print("2. UPI")
            print("3. Card")

            payment = input("Choose payment method: ")

            if payment == "1":
                method = "Cash"
            elif payment == "2":
                method = "UPI"
            elif payment == "3":
                method = "Card"
            else:
                method = "Unknown"

            print("Payment:", method)
            print("Payment Successful!")
            

    elif choice == "3":

        if len(items) == 0:
            print("No items to remove.")

        else:
            for i, item in enumerate(items, 1):
                print(i, item["name"])

            remove = int(input("Enter item number to remove: "))

            if 1 <= remove <= len(items):
                removed = items.pop(remove - 1)
                print(removed["name"], "removed successfully!")
            else:
                print("Invalid item number.")

    elif choice == "4":

        items.clear()
        print("Bill cleared successfully!")

    elif choice == "5":
        print("Thank you for using Billing System!")
        break

    else:
        print("Invalid choice!")

print("===== BILLING SYSTEM =====")

items = []

while True:
    print("\n1. Add Item")
    print("2. View Bill")
    print("3. Exit")

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
            print("\n===== BILL =====")

            grand_total = 0

            for item in items:
                print(
                    item["name"],
                    "QTY:", item["quantity"],
                    "Price:", item["price"],
                    "Total:", item["total"]
                )

                grand_total += item["total"]

                print("------------------------")

            print("Grand Total:", grand_total)
            print("========================")

    elif choice == "3":
        print("Thank you for using Billing System!")
        break

    else:
        print("Invalid choice!")
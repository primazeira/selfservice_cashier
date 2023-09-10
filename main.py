from transaction import Transaction

while True:
    print("\nOptions:")
    print("1. Input Transaction ID")
    print("2. Exit")

    initial_choice = input("Enter your choice: ")

    if initial_choice == "1":
        id_transaction = input("Enter Transaction ID: ")

        if id_transaction not in Transaction.database_user:
            trnsct = Transaction(id_transaction)

        # Greeting message
        print(f"Hi, {id_transaction}!")

        while True:
            print("\nOptions:")
            print("1. Add Item")
            print("2. Check Order")
            print("3. Checkout Order")
            print("4. Update Item Name")
            print("5. Update Item Quantity")
            print("6. Update Item Price")
            print("7. Delete Item")
            print("8. Reset Transaction")
            print("9. Back to ID input")

            choice = input("Enter your choice: ")

            if choice == "1":
                item_name = input("Enter item name: ")
                item_qty = int(input("Enter item quantity: "))
                item_price = float(input("Enter item price: "))
                trnsct.add_item(item_name, item_qty, item_price)
            elif choice == "2":
                trnsct.check_order()
            elif choice == "3":
                trnsct.checkout_order()
            elif choice == "4":
                old_item_name = input("Enter old item name: ")
                new_item_name = input("Enter new item name: ")
                trnsct.update_item_name(old_item_name, new_item_name)
            elif choice == "5":
                item_name = input("Enter item name: ")
                new_qty = int(input("Enter new item quantity: "))
                trnsct.update_item_qty(item_name, new_qty)
            elif choice == "6":
                item_name = input("Enter item name: ")
                new_price = float(input("Enter new item price: "))
                trnsct.update_item_price(item_name, new_price)
            elif choice == "7":
                item_name = input("Enter item name to delete: ")
                trnsct.delete_item(item_name)
            elif choice == "8":
                trnsct.reset_transaction()
            elif choice == "9":
                break
            else:
                print("Invalid choice. Please try again.")
    elif initial_choice == "2":
        break
    else:
        print("Invalid choice. Please try again.")
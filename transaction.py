from tabulate import tabulate
from utils import validate_and_format_price

class Transaction:
    database_user = {}

    def __init__(self, id_transaction):
        """
        Initialize a new transaction instance.

        Args:
            id_transaction (str): The ID of the transaction.
        """
        self.id_transaction = id_transaction
        if id_transaction not in self.database_user:
            self.database_user[self.id_transaction] = {"items": {}}

    def add_item(self, item_name, item_qty, item_price_str):
        """
        Add an item to the current transaction.

        Args:
            item_name (str): The name of the item.
            item_qty (int): The quantity of the item.
            item_price_str (str): The input string representing the price.
        """
        item_price = validate_and_format_price(item_price_str)
        if item_price is not None:
            user_data = self.database_user.get(self.id_transaction)
            if user_data:
                if item_name in user_data["items"]:
                    user_data["items"][item_name]["item_qty"] += item_qty
                else:
                    user_data["items"][item_name] = {
                        "item_qty": item_qty,
                        "item_price": item_price,
                    }
                print(f"Added {item_qty} {item_name} to Transaction ID: {self.id_transaction}")
            else:
                print("Transaction not found.")

    def check_order(self):
        """
        Display the list of items in the current transaction without calculating total price or applying discounts.
        """
        user_data = self.database_user.get(self.id_transaction)
        if user_data:
            items = user_data["items"]
            header = ["No.", "Name", "Qty", "Price"]
            table = [
                [i + 1, item_name, item_info["item_qty"], item_info["item_price"]]
                for i, (item_name, item_info) in enumerate(items.items())
            ]

            print(f"Hi, {self.id_transaction}!")
            print(f"Transaction ID: {self.id_transaction}")
            print(tabulate(table, headers=header))
        else:
            print("Transaction not found.")

    def checkout_order(self):
        """
        Display the list of items in the current transaction and calculate the total price.

        The method also applies discounts based on the total price.
        """
        user_data = self.database_user.get(self.id_transaction)
        if user_data:
            items = user_data["items"]
            header = ["No.", "Name", "Qty", "Price"]
            table = [
                [i + 1, item_name, item_info["item_qty"], item_info["item_price"]]
                for i, (item_name, item_info) in enumerate(items.items())
            ]

            total_price = sum(item_info["item_qty"] * item_info["item_price"] for item_info in items.values())
            discount = 0  # Initialize discount to 0%

            # Apply discounts based on total_price
            if total_price > 500000:
                discount = 10
            elif total_price > 300000:
                discount = 8
            elif total_price > 200000:
                discount = 5

            # Calculate discounted price
            discounted_price = total_price - (total_price * discount / 100)

            print(f"Hi, {self.id_transaction}!")
            print(f"Here's your options")
            print(f"Transaction ID: {self.id_transaction}")
            print(tabulate(table, headers=header))
            print(f"Total price for Transaction ID {self.id_transaction}: Rp{total_price}")
            print(f"Discount applied: {discount}%")
            print(f"Discounted price: Rp{discounted_price}")
        else:
            print("Transaction not found.")

    def update_item_name(self, old_item_name, new_item_name):
        """
        Update the name of an item in the current transaction.

        Args:
            old_item_name (str): The old name of the item.
            new_item_name (str): The new name of the item.
        """
        user_data = self.database_user.get(self.id_transaction)
        if user_data and old_item_name in user_data["items"]:
            user_data["items"][new_item_name] = user_data["items"].pop(old_item_name)
            print(f"Updated item name from {old_item_name} to {new_item_name}")
        else:
            print("Item not found in the transaction.")

    def update_item_qty(self, item_name, new_qty):
        """
        Update the quantity of an item in the current transaction.

        Args:
            item_name (str): The name of the item.
            new_qty (int): The new quantity of the item.
        """
        user_data = self.database_user.get(self.id_transaction)
        if user_data and item_name in user_data["items"]:
            user_data["items"][item_name]["item_qty"] = new_qty
            print(f"Updated item quantity for {item_name} to {new_qty}")
        else:
            print("Item not found in the transaction.")

    def update_item_price(self, item_name, new_price):
        """
        Update the price of an item in the current transaction.

        Args:
            item_name (str): The name of the item.
            new_price (float): The new price of the item.
        """
        user_data = self.database_user.get(self.id_transaction)
        if user_data and item_name in user_data["items"]:
            user_data["items"][item_name]["item_price"] = new_price
            print(f"Updated item price for {item_name} to {new_price}")
        else:
            print("Item not found in the transaction.")

    def delete_item(self, item_name):
        """
        Delete an item from the current transaction.

        Args:
            item_name (str): The name of the item to be deleted.
        """
        user_data = self.database_user.get(self.id_transaction)
        if user_data and item_name in user_data["items"]:
            del user_data["items"][item_name]
            print(f"Deleted item {item_name} from the transaction.")
        else:
            print("Item not found in the transaction.")

    def reset_transaction(self):
        """
        Reset the current transaction by removing all items.
        """
        user_data = self.database_user.get(self.id_transaction)
        if user_data:
            user_data["items"] = {}
            print(f"Transaction ID {self.id_transaction} has been reset.")
        else:
            print("Transaction not found.")

    def greet_user(self):
        """
        Display a greeting message to the user.
        """
        print(f"Hi, {self.id_transaction}!")
**Project Documentation: Self Service Cashier System**
# System Overview
## Background Problem
The owner of a large metropolitan supermarket in Indonesia identified a need to optimize their business processes. Specifically, they aimed to streamline the cashier system to improve customer service and operational efficiency by making a self-service cashier system. The self-service cashier system will be addressing the following challenges:

- The need to streamline the supermarket's business processes.
- Providing a self-service cashier system to enhance the customer shopping experience.
- Ensuring that only customers within the supermarket's city can make purchases.
## Requirements/Objectives
The primary objectives of this system are as follows:

- Streamline the checkout process by allowing customers to input their purchased items and quantities.
- Improve transaction tracking and management for the supermarket.
- Provide a self-service cashier system.
- Implement location-based restrictions on customer purchases.
# Code Flow
**Step 1: Start**

Program starts.

**Step 2: User Chooses an Option**

Display the following options to the user:

1. Input Transaction ID
1. Exit

**Step 3: If User Chooses "Input Transaction ID"**

Prompt the user to enter a Transaction ID.

**Step 4: Check if Transaction ID Exists in the Transaction Database**

If the Transaction ID does not exist:

- Create a new Transaction Instance.
- Set the Current Transaction as the new instance.
- Display a greeting message.

**Step 5: While True Loop for User Actions**

- Enter a loop to handle various user actions.
- Display the following options to the user:
1. Add Item
1. Check Order
1. Checkout Order
1. Update Item Name
1. Update Item Quantity
1. Update Item Price
1. Delete Item
1. Reset Transaction
1. Back to Transaction ID Input

**Step 6: Handle User Actions**

Depending on the user's choice:

- If the user chooses "Add Item":
  - Prompt the user to enter item name, quantity, and price.
  - Add the item to the current transaction.
- If the user chooses "Check Order":
  - Display the list of items in the current transaction.
- If the user chooses "Checkout Order":
  - Display the list of items and total price.
  - Apply discounts if applicable.
- If the user chooses "Update Item Name":
  - Prompt the user to enter old item name and new item name.
  - Update the item name in the current transaction.
- If the user chooses "Update Item Quantity":
  - Prompt the user to enter item name and new quantity.
  - Update the item quantity in the current transaction.
- If the user chooses "Update Item Price":
  - Prompt the user to enter item name and new price.
  - Update the item price in the current transaction.
- If the user chooses "Delete Item":
  - Prompt the user to enter item name to delete.
  - Delete the item from the current transaction.
- If the user chooses "Reset Transaction":
  - Reset the current transaction.
- If the user chooses "Back to Transaction ID Input":
  - Exit the current transaction.

**Step 7: If User Chooses "Exit"**

Exit the program.

**Step 8: End**

Program ends.
# Code Structure
The system consists of three modules:

- **transaction.py**: Defines the Transaction class and handles all transaction-related operations.
- **main.py**: Implements the user interface, user input, and interaction with the Transaction class.
- **utils.py**: Validate and format prices for items
# Code Explanation
## Main Application (main.py)
This module serves as the user interface and orchestrates interactions with the Transaction class. It provides options for the user to manage their transaction.
## Transaction Class (transaction.py)
The Transaction class represents a customer's transaction within the self-service cashier system. It allows for the management of items, quantities, and prices associated with a specific transaction. 
### Class Definition
- **from tabulate import tabulate**: This line imports the **tabulate** function from the **tabulate** library, which is used for formatting data into tables.
- **from utils import validate\_and\_format\_price**: This line imports the **validate\_and\_format\_price** function from a module named **utils**. This function likely validates and formats prices.
### Class Variables
- **database\_user = {}**: This is a class variable that initializes an empty dictionary named database\_user. It will be used to store transaction data. It's a shared variable among all instances of this class.
### Class Methods
- **\_\_init\_\_(self, id\_transaction):** This method is used to initialize a new transaction instance with a unique transaction ID. If the ID already exists in the database\_user, it retrieves the existing transaction data; otherwise, it creates a new transaction data entry.
- **add\_item(self, item\_name, item\_qty, item\_price):** This method allows the customer to add an item to their transaction. It records the item name, quantity, and price within the transaction data.
- **check\_order(self):** This method is used to display a table with details of the items in the current transaction, including item number, name, quantity, and price.
- **checkout\_order(self):** This method is used to display the items, quantities, and prices in a tabular format and calculates the total price of items in the transaction, applies discounts based on the total price, and displays the final price. 
- **update\_item\_name:** This method is used to update the name of an item in the current transaction. It checks if the old item name exists in the transaction's items. If it does, it updates the name to the new item name.

- **update\_item\_qty:** This method is used to update the quantity of an item in the current transaction. It checks if the item name exists in the transaction's items. If it does, it updates the quantity to the new quantity.

- **update\_item\_price:** This method is used to update the price of an item in the current transaction. It checks if the item name exists in the transaction's items. If it does, it updates the price to the new price.

- **delete\_item:** This method is used to delete an item from the current transaction. It checks if the item name exists in the transaction's items. If it does, it removes the item from the transaction.

- **reset\_transaction:** This method is used to reset the current transaction by removing all items. It clears the items dictionary for the current transaction.

- **greet\_user:** This method displays a greeting message to the user, likely when a transaction is initiated.
# Demonstration of Test Cases
## Test 1: Customer adds new items
Details of the new items: \
![image](https://github.com/primazeira/selfservicecashier_system/assets/144573882/f4320bdd-095a-40b1-877e-02e9bc810484)

Test result: \
![image](https://github.com/primazeira/selfservicecashier_system/assets/144573882/d583265c-26a0-40d8-ae55-a234c8e3e7e6)

## Test 2: Customer deletes a specific inputted item
Item needs to be deleted: **Pasta gigi**

Test result: \
![image](https://github.com/primazeira/selfservicecashier_system/assets/144573882/ea808bc4-ccdd-4ca9-84a1-70ba1b817906)

## Test 3: Customer deletes all inputted items
Remaining item needs to be deleted by resetting the transaction: \
![image](https://github.com/primazeira/selfservicecashier_system/assets/144573882/55f305a7-d4be-459b-bc3c-c94883e7ec6d)

Test result: \
![image](https://github.com/primazeira/selfservicecashier_system/assets/144573882/898a5ac9-f375-4057-9592-abdedfa8bac3)

## Test 4: The system shows the inputted items and counts the total transaction
Total transaction is counted from the previously inputted items in Test Case 1, as follows: \
![image](https://github.com/primazeira/selfservicecashier_system/assets/144573882/79613935-13b3-4a30-b1ea-2d73edd01203)

The result: \
![image](https://github.com/primazeira/selfservicecashier_system/assets/144573882/a850279b-23c5-43e8-a411-d68bac75e500)

# Conclusion
In conclusion, the Self-Service Cashier System successfully addresses the supermarket's business process challenges by providing a user-friendly and efficient way for customers to make purchases. It ensures that transactions are limited to customers in the same city as the supermarket. 

While the system meets its primary objectives, there are areas for improvement, such as utilizing database management system, enhancing error handling, and providing more detailed documentation for users and developers. Future updates could also include features like loyalty programs and support for online orders.


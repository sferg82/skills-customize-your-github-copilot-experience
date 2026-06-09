# 📘 Assignment: Unit Testing and Modular Design

## 🎯 Objective

Practice organizing Python code into reusable modules and verify functionality using unit tests. You will build a small order-processing module and write tests to ensure it works correctly.

## 📝 Tasks

### 🛠️ Design reusable modules

#### Description
Create a Python module that separates business logic from presentation and test code.

#### Requirements
Completed program should:

- Define functions in a reusable module for order calculations and receipt formatting.
- Keep calculations separate from user-facing output.
- Use clear function names and docstrings.

### 🛠️ Implement order processing functions

#### Description
Write functions that calculate totals, apply discounts, and format receipts.

#### Requirements
Completed program should:

- Implement a function to calculate the total price for a list of items.
- Implement a function to apply a discount percentage to an order total.
- Implement a function to return a receipt string with customer name, item details, subtotal, discount, and final total.

### 🛠️ Write unit tests

#### Description
Add a separate test file that checks the module's behavior using Python's `unittest` framework.

#### Requirements
Completed program should:

- Create a test file that imports the order-processing functions.
- Write tests for normal order totals, discounts, and receipt formatting.
- Include at least one test for invalid input or edge cases.

### 💡 Run your tests

#### Description
Execute the unit tests and confirm the module works before submission.

#### Requirements
Completed program should:

- Run successfully with `python -m unittest`.
- Show all tests passing.
- Keep the production code separate from the test code.

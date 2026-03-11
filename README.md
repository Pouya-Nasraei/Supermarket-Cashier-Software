# Supermarket Cashier Software

## Overview

Supermarket Cashier Software is a desktop billing application built with **Python and Tkinter** that simulates a basic supermarket point-of-sale (POS) system.

The application allows a cashier to add products to a customer's cart, calculate totals, apply membership discounts, and generate a digital receipt stored in JSON format.

The project is structured as a small modular Python application, separating **GUI logic**, **business logic**, and **data handling** into different modules.

This project demonstrates practical usage of:

* Python object-oriented programming
* GUI development with Tkinter
* JSON data storage and processing
* Modular Python project structure
* Logging for application events
* Basic retail pricing logic

The system loads available products from a JSON file and dynamically calculates totals based on quantity and membership discount rules.

---

## Project Screenshots

### Application Interface

![Application Interface](Images/app-Image.png)

### Example Receipt Output

![Receipt Example](Images/receipt.png)

---

## Features

### Product Management

Products are loaded from a JSON file located in the **data** directory.

Example:

```json
{
    "BISCUIT": 2.5,
    "CHICKEN": 4,
    "EGG": 1,
    "FISH": 7,
    "COKE": 2,
    "BREAD": 1.5,
    "APPLE": 2,
    "ONION": 3,
    "ORANGE": 3,
    "MILK": 2,
    "CHOCOLATE": 1.5,
    "WATER": 1.75,
    "BANANA": 0.5,
    "JUICE": 1.25,
    "CUCEMBER": 1.5
}
```

The cashier enters a product name and quantity to add it to the customer's cart.

---

### Shopping Cart System

The program maintains an in-memory shopping cart using a Python dictionary:

```python
self.shopping_cart = {
    "MILK": 2,
    "BREAD": 1
}
```

Each time an item is added:

* Quantity is updated
* The running total price is recalculated
* The GUI display is refreshed

---

### Membership Discount System

Customers can receive discounts based on membership level.

| Membership | Discount |
| ---------- | -------- |
| Gold       | 20%      |
| Silver     | 10%      |
| Bronze     | 5%       |

The final price is calculated using:

```
final_price = total_price * (1 - discount)
```

---

### Automatic Receipt Generation

When a membership discount is applied, a receipt is automatically saved as a **timestamped JSON file**.

Example file name:

```
receipts/receipt_20260311_141152.json
```

Example receipt content:

```json
{
  "date": "2026-03-11 14:11:52",
  "items": {
    "MILK": 2,
    "BREAD": 1
  },
  "total_before_discount": 5.5,
  "final_price": 4.4
}
```

This simulates basic **transaction logging in retail systems** and ensures that every transaction generates a unique receipt.

---

## Logging System

The application includes a basic **logging system** to record key events such as:

* Application startup
* Product additions
* Receipt generation

Example log output:

```
2026-03-11 14:08:01 | INFO | Starting Cashier Application
2026-03-11 14:09:05 | INFO | Products loaded successfully
2026-03-11 18:10:20 | INFO | Product added: MILK (x2)
2026-03-11 18:11:52 | INFO | Receipt saved: receipts/receipt_20260310_184610.json
```

Logging helps track application behavior and supports debugging and maintenance.

---

## GUI Implementation

The interface is built using **Tkinter**, Python’s built-in GUI toolkit.

Main components include:

* Labels for displaying information
* Entry widgets for user input
* Buttons for actions
* Dynamic label updates for cart display

| Component               | Purpose                   |
| ----------------------- | ------------------------- |
| Product Entry           | Input product name        |
| Quantity Entry          | Input product quantity    |
| Add Product Button      | Add item to cart          |
| Display Label           | Show cart items and total |
| Apply Membership Button | Apply discount            |
| Final Price Label       | Show discounted price     |

---

## Project Structure

```
Supermarket-Cashier-Software
│
├── src
│   ├── main.py
│   ├── cashier.py
│   └── utils.py
│
├── data
│   └── products.json
│
├── receipts
│
├── Images
│   ├── app-Image.png
│   └── receipt.png
│
├── README.md
└── requirements.txt
```

### Module Responsibilities

| File       | Purpose                                           |
| ---------- | ------------------------------------------------- |
| main.py    | Application entry point and logging configuration |
| cashier.py | Tkinter GUI and cashier logic                     |
| utils.py   | Product loading and receipt generation            |

This modular structure improves readability, maintainability, and scalability.

---

## How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/Pouya-Nasraei/Supermarket-Cashier-Software.git
```

### 2. Navigate to the project directory

```
cd Supermarket-Cashier-Software
```

### 3. Run the application

```
python src/main.py
```

Python **3.8 or newer** is recommended.

---

## Example Workflow

1. Enter product name
2. Enter quantity
3. Click **Add Product**
4. Repeat for additional items
5. Click **Apply Membership**
6. Enter membership type (Gold / Silver / Bronze)
7. Final price is calculated and a receipt is saved automatically

---

## Technologies Used

* **Python 3**
* **Tkinter** – GUI framework
* **JSON** – data storage
* **Datetime module** – transaction timestamps
* **Logging module** – event tracking

---

## Learning Objectives

This project was developed to practice:

* Python GUI programming
* Modular Python project structure
* File-based data persistence
* User input validation
* Object-oriented programming
* Basic retail transaction logic

---

## Possible Improvements

Future enhancements could include:

* Barcode scanner integration
* Product database using SQLite
* Inventory management system
* Searchable product catalog
* Improved user interface design
* Transaction history viewer

---

## Author

Pouya Nasraei
Python Developer | Software Engineer

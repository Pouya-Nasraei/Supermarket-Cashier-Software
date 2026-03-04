from tkinter import *
from tkinter import messagebox, simpledialog

root = Tk()
root.geometry('400x500')
root.title("Customer's Bill")

priceData = {
    "BISCUIT": 2.5,
    "CHICKEN": 4,
    "EGG": 1,
    "FISH": 5,
    "COKE": 2,
    "BREAD": 1.5,
    "APPLE": 2,
    "ONION": 3,
    "ORANGE": 3,
    "MILK": 2,
    "CHOCOLATE": 1.5
}

shopping_data = {}
total_price = 0

def getProduct():
    global total_price
    product_name = productE.get().strip().upper()
    try:
        quantity = int(quantityE.get())
    except ValueError:
        if product_name == "":
            messagebox.showerror("❌ Error", "Please enter a product!")
        elif product_name not in priceData:
            messagebox.showerror("Error", "The product is not in the stock!")
        else:
            messagebox.showerror("Error", "Please enter a valid quantity (number).")
        return
    if product_name in priceData:
        price = priceData[product_name] * quantity
        shopping_data[product_name] = shopping_data.get(product_name, 0) + quantity
        total_price += price
        updateShoppingList()
    else:
        messagebox.showinfo("Product not found", f"Product is not in the list!\n\nAvailable products:\n{list(priceData.keys())}")

    # Clear entries and move cursor back to product entry
    productE.delete(0, END)
    quantityE.delete(0, END)
    productE.focus()


def updateShoppingList():
    shoppingListL.config(text="")
    display_text = "Shopping List:\n"
    for item, qty in shopping_data.items():
        display_text += f"{item} £{priceData[item]} x {qty} = £{priceData[item] * qty}\n"
    display_text += f"\nTotal (before discount): £{total_price}"
    shoppingListL.config(text = display_text)


def applyMembership():
    """Ask user for membership and apply discount if total > £30."""
    global total_price
    if total_price == 0:
        messagebox.showinfo("Info", "No items added yet!")
        return

    if total_price <= 30:
        messagebox.showinfo("Info", "Discount applies only for totals above £30.")
        finalBillL.config(text=f"Total to pay: £{total_price:.2f}")
        return

    membership = simpledialog.askstring("Membership", "Enter membership type (Gold/Silver/Bronze):")
    if not membership:
        return

    membership = membership.strip().upper()
    discount = 0

    if membership == "GOLD":
        discount = 0.20
    elif membership == "SILVER":
        discount = 0.10
    elif membership == "BRONZE":
        discount = 0.05
    else:
        messagebox.showinfo("Invalid", "Please enter 'Gold', 'Silver', or 'Bronze'.")
        return

    final_price = total_price * (1 - discount)
    finalBillL.config(text=f"Final Price after {int(discount * 100)}% discount:\n£{final_price:.2f}")


def moveToQuantity(event):
    """When pressing Enter in product entry, move focus to quantity entry."""
    quantityE.focus()

# ------------------- GUI LAYOUT -------------------
Label(root, text="Customer's Bill", font=("Arial", 18, "bold")).pack(pady=10)

frame = Frame(root)
frame.pack(pady=10)

Label(frame, text="Product").grid(row=0, column=0, padx=10)
productE = Entry(frame, width=15)
productE.grid(row=1, column=0, padx=10)
productE.bind("<Return>", moveToQuantity)   # Move focus on Enter

Label(frame, text="Quantity").grid(row=0, column=1, padx=10)
quantityE = Entry(frame, width=15, )
quantityE.grid(row=1, column=1, padx=10)
quantityE.bind("<Return>", lambda event: getProduct())

enterProductBtn = Button(root, text="Enter Product", width=20, command=getProduct).pack(pady=10)

shoppingListL = Label(root, text="Shopping List:", justify=LEFT, anchor="w", font=("Arial", 10))
shoppingListL.pack(pady=10)

Button(root, text="Membership", width=20, command=applyMembership).pack(pady=10)

finalBillL = Label(root, text="Final Price will appear here", font=("Arial", 12, "bold"), fg="blue")
finalBillL.pack(pady=15)

Label(root, text="Thank you for shopping with us!", font=("Arial", 10), fg="gray").pack(pady=10)

# Focus starts on the product entry
productE.focus()

root.mainloop()
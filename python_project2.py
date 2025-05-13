from tkinter import *
from tkinter import messagebox

"""
An ordering system for a take-away food shop. A GUI menu takes input from the operator
(menu items are chosen from a series of drop-down lists, including quantity) and interacts
with an array of food items. Each order has a space for entering the name associated with the order.
The program stores orders in an array. The program allows for take-away and delivery orders and
calculates the final cost of the order. The menu drives all aspects of the ordering system.
"""


class Order:

    def __init__(self, name, item_ordered, amount, total_price):
        self.name = name
        self.item_ordered = item_ordered
        self.amount = amount
        self.total_price = total_price


class Main:
    def __init__(self, parent):

        # Menu
        self.menu = [["Pizza", 21], ["Burger", 16], ["Hotdog", 7], ["Salad", 8], ["Soda", 5]]
        self.menu_names = [item[0] for item in self.menu]
        rowcount1=0
        self.orders = []


        # Variables
        self.name_var = StringVar()
        self.selected_option_var = StringVar()
        self.selected_option_var.set("Select an item")
        
        # Frames
        self.create_order_frame = Frame(parent)
        self.create_order_frame.grid()
        self.menu_frame = Frame(self.create_order_frame, relief="solid")
        self.menu_frame.grid(row=0, columnspan=2)
        self.display_order = Frame(parent)
        
        for i in range(len(self.menu)):

            Label(self.menu_frame, text=self.menu[i][0]).grid(row=rowcount1, column=0)
            Label(self.menu_frame, text="$" + str(self.menu[i][1])).grid(row=rowcount1, column=1)
            rowcount1 += 1
        
        # CREATE ORDER WIDGETS
        self.name_label = Label(self.create_order_frame, text="Name: ").grid(row=rowcount1, column=0)
        self.name_entry = Entry(self.create_order_frame, textvariable=self.name_var).grid(row=rowcount1, column=1)
        
        self.option_label = Label(self.create_order_frame, text="Item: ").grid(row=rowcount1+1, column=0)
        self.selected_option = OptionMenu(self.create_order_frame, self.selected_option_var, *self.menu_names).grid(row=rowcount1+1, column=1)

        self.amount_label = Label(self.create_order_frame, text="Amount: ").grid(row=rowcount1+2, column=0)
        self.amount_entry = Spinbox(self.create_order_frame, from_=1, to=10)
        self.amount_entry.grid(row=rowcount1+2, column=1)
        
        self.enter_button = Button(self.create_order_frame, text="SUBMIT", command=self.submit_order)
        self.enter_button.grid(row=rowcount1+3, column=0, sticky=W)
        
        self.view_orders_btn = Button(self.create_order_frame, text="View Orders", command=self.view_orders, state="disabled")
        self.view_orders_btn.grid(row=rowcount1+3, column=1, sticky=E)

        # CREATE DISPLAY WIDGETS
        self.name_display = Label(self.display_order, text="No name selected")
        self.name_display.grid(row=1, columnspan=2)
        self.item_display = Label(self.display_order, text="No item selected")
        self.item_display.grid(row=2, columnspan=2)
        self.total_price_label = Label(self.display_order, text="Total price")
        self.total_price_label.grid(row=3, columnspan=2)



    def submit_order(self):
        self.view_orders_btn.configure(state="normal")
        name = self.name_var.get()
        item_ordered = self.selected_option_var.get()
        price = 0
        print(item_ordered)
        for item in self.menu:
            if item[0] == item_ordered:
                price += item[1]
        print(price)
        amount = self.amount_entry.get()
        self.orders.append(Order(name, item_ordered, amount, price))
        print("Submitted")
    
    def view_orders(self):
        self.menu_frame.grid_forget()
        self.create_order_frame.grid_forget()
        self.display_order.grid()
        



if __name__ == "__main__":
    root = Tk()
    start = Main(root)
    root.title("Shop")
    root.mainloop()
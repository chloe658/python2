"""
An ordering system for a take-away food shop. A GUI menu takes input from the operator
(menu items are chosen from a series of drop-down lists, including quantity) and interacts
with an array of food items. Each order has a space for entering the name associated with the order.
The program stores orders in an array. The program allows for take-away and delivery orders and
calculates the final cost of the order. The menu drives all aspects of the ordering system.
"""

from tkinter import *
from tkinter import messagebox


class Order:

    def __init__(self, name, item_ordered, amount, price, collection_method):
        self.name = name
        self.item_ordered = item_ordered
        self.amount = amount
        self.price = price
        self.collection_method = collection_method


class Main:
    def __init__(self, parent):

        # Menu
        self.menu = [["Pizza", 21], ["Burger", 16], ["Hotdog", 7], ["Salad", 8], ["Soda", 5]]
        self.menu_names = [item[0] for item in self.menu]
        self.rowcount1 = 1
        self.rowcount2 = 6
        self.orders = []
        self.current_items = []
        self.temp_list = []

        # Variables
        self.name_var = StringVar()
        self.selected_option_var = StringVar()
        self.selected_option_var.set("Select an item")
        self.collection_var = StringVar()
        self.collection_var.set("Pick-Up")
        self.index = 0
        self.index = 0

        # Frames
        self.create_order_frame = Frame(parent)
        self.create_order_frame.grid()
        self.menu_frame = Frame(self.create_order_frame, relief="solid")
        self.menu_frame.grid(row=0, columnspan=2)
        self.display_order = Frame(parent)

        for i in range(len(self.menu)):

            Label(self.menu_frame, text=self.menu[i][0]).grid(row=self.rowcount1, column=0)
            Label(self.menu_frame, text="$" + str(self.menu[i][1])).grid(row=self.rowcount1, column=1)
            self.rowcount1 += 1

        # CREATE ORDER WIDGETS
        self.create_order_label = Label(self.display_order, text="Create Order").grid(row=0, columnspan=2)
        self.name_label = Label(self.create_order_frame, text="Name: ").grid(row=self.rowcount1, column=0)
        self.name_entry = Entry(self.create_order_frame, textvariable=self.name_var)
        self.name_entry.grid(row=self.rowcount1, column=1)

        self.option_label = Label(self.create_order_frame, text="Item: ").grid(row=self.rowcount1+1, column=0)
        self.selected_option = OptionMenu(self.create_order_frame, self.selected_option_var, *self.menu_names)
        self.selected_option.grid(row=self.rowcount1+1, column=0)
        self.add_item_btn = Button(self.create_order_frame, text="Add Item", command=self.add_item)
        self.add_item_btn.grid(row=self.rowcount1+1, column=1)
        self.amount_label = Label(self.create_order_frame, text="Amount: ").grid(row=self.rowcount1+2, column=0)
        self.amount_entry = Spinbox(self.create_order_frame, from_=1, to=10)
        self.amount_entry.grid(row=self.rowcount1+2, column=1)

        self.pickup = Radiobutton(self.create_order_frame, text="Pick-Up", value="Pick-Up", variable=self.collection_var)
        self.pickup.grid(row=self.rowcount1+3, column=0)
        self.delivery = Radiobutton(self.create_order_frame, text="Delivery ($15 Fee)", value="Delivery", variable=self.collection_var)
        self.delivery.grid(row=self.rowcount1+3, column=1)

        self.enter_button = Button(self.create_order_frame, text="SUBMIT", command=self.submit_order)
        self.enter_button.grid(row=self.rowcount1+4, column=0, sticky=W)

        self.view_orders_btn = Button(self.create_order_frame, text="View Orders", command=self.view_orders, state="disabled")
        self.view_orders_btn.grid(row=self.rowcount1+4, column=1, sticky=E)

        # CREATE DISPLAY WIDGETS
        self.display_order_label = Label(self.display_order, text="Display Orders").grid(row=0, column=0)
        self.add_new_btn = Button(self.display_order, text="Add New Order", command=self.display_to_create)
        self.add_new_btn.grid(row=0, column=1)

        self.previous_order_btn = Button(self.display_order, text="Previous", command=self.display_previous)
        self.next_order_btn = Button(self.display_order, text="Next", command=self.display_next)
        self.previous_order_btn.grid(row=1, column=0)
        self.next_order_btn.grid(row=1, column=1)

        self.name_display = Label(self.display_order, text="")
        self.name_display.grid(row=2, columnspan=2)
        self.total_price_display = Label(self.display_order, text="")
        self.total_price_display.grid(row=3, columnspan=2)
        self.collection_display = Label (self.display_order, text="")
        self.collection_display.grid(row=4, columnspan=2)
        self.item_display = Label(self.display_order, text="Items: ")
        self.item_display.grid(row=5, column=0)

    def submit_order(self):
        self.view_orders_btn.configure(state="normal")
        name = self.name_var.get()
        item_names = [item[0] for item in self.current_items]
        amount = [item[1] for item in self.current_items]
        price = 0
        collection_method = self.collection_var.get()
        for thing in self.current_items:
            for item in self.menu:
                if item[0] == thing[0]:
                    price += int(item[1])*int(thing[1])
        if collection_method == "Delivery":
            price += 15
        self.orders.append(Order(name, item_names, amount, price, collection_method))
        self.current_items = [] # Reset list
        self.name_entry.delete(0, END)
        self.name_entry.focus()
        self.collection_var.set("Pick-Up")

    def display_to_create(self):
        self.menu_frame.grid(row=0, columnspan=2)
        self.create_order_frame.grid()
        self.display_order.grid_forget()
        self.rowcount1 = 0
        self.rowcount2 = 6
    
    def display_next(self):
        if self.index >= len(self.orders) - 1:
            self.index = 0
        else:
            self.index +=1
        for temp in self.temp_list:
            temp.destroy()
        self.temp_list.clear()
        self.rowcount2 = 5
        self.configure_display_labels()
    
    def display_previous(self):
        if self.index == 0:
            self.index = len(self.orders) - 1
        else:
            self.index -=1
        for temp in self.temp_list:
            temp.destroy()
        self.temp_list.clear()
        self.rowcount2 = 6
        self.configure_display_labels()

    def add_item(self):
        self.current_items.append([self.selected_option_var.get(), self.amount_entry.get()])
        self.selected_option_var.set("Select an item")
        self.amount_entry.delete(0, END)
        self.amount_entry.insert(0, 1)

    def view_orders(self):
        self.menu_frame.grid_forget()
        self.create_order_frame.grid_forget()
        self.display_order.grid()
        self.configure_display_labels()
    
    def configure_display_labels(self):
        self.name_display.configure(text="Name: " + str(self.orders[self.index].name))
        # Clear previous labels
        for temp in self.temp_list:
            temp.destroy()
        self.temp_list.clear()
        self.rowcount2 = 6
        print(self.index)

        self.total_price_display.configure(text="Total Price: " + str(self.orders[self.index].price))
        self.collection_display.configure(text=f"Collection by {self.orders[self.index].collection_method}")
        
        for i in range(len(self.orders[self.index].item_ordered)):
            label = Label(self.display_order, text=f"x{self.orders[self.index].amount[i-1]} {self.orders[self.index].item_ordered[i-1]}")
            label.grid(row=5 + i, column=1, sticky=W)
            self.temp_list.append(label)
            self.rowcount2 += 1

if __name__ == "__main__":
    root = Tk()
    start = Main(root)
    root.title("Shop")
    root.mainloop()
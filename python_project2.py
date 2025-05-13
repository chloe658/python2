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

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Main:
    def __init__(self, parent):

        #Menu
        self.menu = [["Pizza", 21], ["Burger", 16], ["Hotdog", 7], ["Salad", 8], ["Soda", 5]]
        rowcount=0
        self.orders = []


        #Variables
        self.name_var = StringVar()
        self.create_order_frame = Frame(parent)
        self.create_order_frame.grid()
        self.menu_frame = Frame(self.create_order_frame, relief="solid")
        self.menu_frame.grid(row=0, columnspan=2)
        self.display_order = Frame(parent)
        self.display_order.grid()
        
        for i in range(len(self.menu)):

            Label(self.menu_frame, text=self.menu[i][0]).grid(row=rowcount, column=0)
            Label(self.menu_frame, text=self.menu[i][1]).grid(row=rowcount, column=1)
            rowcount += 1
        
        self.name_label = Label(self.create_order_frame, text="Name: ").grid(row=rowcount, column=0)
        self.name_entry = Entry(self.create_order_frame, textvariable=self.name_var).grid(row=rowcount, column=1)
        
        self.amount_label = Label(self.create_order_frame, text="Amount: ").grid(row=rowcount+1, column=0)
        self.amount_entry = Spinbox(self.create_order_frame, from_=1, to=10)
        self.amount_entry.grid(row=rowcount+1, column=1)
        self.enter_button = Button(self.create_order_frame, text="SUBMIT", command=self.submit_order)
        self.enter_button.grid(row=rowcount+2, column=0, sticky=W)
        self.view_orders_btn = Button(self.create_order_frame, text="View Orders", command=self.view_orders, state="disabled")
        self.view_orders_btn.grid(row=rowcount+2, column=1, sticky=E)


    def submit_order(self):
        self.view_orders_btn.configure(state="normal")
        name = self.name_var.get()
        amount = self.amount_entry.get()
        self.orders.append(Order(name, amount))
        print("Submitted")
    
    def view_orders(self):
        self.menu_frame.grid_forget()
        self.create_order_frame.grid_forget()
        self.display_order.grid()
        print("sdfgdt")



if __name__ == "__main__":
    root = Tk()
    start = Main(root)
    root.title("Shop")
    root.mainloop()
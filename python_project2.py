"""An ordering system for a take-away food shop."""

from tkinter import *
from tkinter import messagebox


class Order:
    """Create order from user input."""

    def __init__(self, name, item_ordered, amount, price, collection_method):
        """Initiate widgets for Order class."""
        self.name = name
        self.item_ordered = item_ordered
        self.amount = amount
        self.price = price
        self.collection_method = collection_method


class Main:
    """Collect user inout and display order."""

    def __init__(self, parent):
        """Initiate widgets for Main class."""
        # Menu
        self.menu = [["Pizza", 21], ["Burger", 16], ["Hotdog", 7],
                     ["Salad", 8], ["Soda", 5]]
        self.menu_names = [item[0] for item in self.menu]
        self.rowcount1 = 1
        self.rowcount2 = 6
        self.orders = []
        self.current_items = []
        self.temp_list = []

        # Variables
        self.name_var = StringVar()
        self.selected_option_var = StringVar()
        self.amount_var = StringVar()
        self.selected_option_var.set("Select an item")
        self.collection_var = StringVar()
        self.collection_var.set("Pick-Up")
        self.index = 0
        wd = 15
        wd2 = 25

        # Frames
        self.create_order_frame = Frame(parent)
        self.create_order_frame.grid()
        self.menu_frame = Frame(self.create_order_frame,
                                relief="solid", borderwidth=3)
        self.menu_frame.grid(row=0, columnspan=2)
        self.display_order = Frame(parent)

        for i in range(len(self.menu)):

            Label(self.menu_frame, text=self.menu[i][0], width=10,
                  bg="light blue").grid(row=self.rowcount1, column=0)
            Label(self.menu_frame, text="$" + str(self.menu[i][1]), width=10,
                  bg="light blue").grid(row=self.rowcount1, column=1)
            self.rowcount1 += 1

        # CREATE ORDER WIDGETS
        self.option_label = Label(self.create_order_frame, text="Item: ",
                                  width=wd)
        self.option_label.grid(row=self.rowcount1, column=0)
        self.selected_option = OptionMenu(self.create_order_frame,
                                          self.selected_option_var,
                                          *self.menu_names)
        self.selected_option.grid(row=self.rowcount1, column=1)

        self.amount_label = Label(self.create_order_frame,
                                  text="Amount: ", width=wd)
        self.amount_label.grid(row=self.rowcount1+1, column=0)
        self.amount_entry = Entry(self.create_order_frame,
                                  textvariable=self.amount_var, width=wd)
        self.amount_entry.grid(row=self.rowcount1+1, column=1)

        self.add_item_btn = Button(self.create_order_frame, text="Add Item",
                                   command=self.add_item, width=wd)
        self.add_item_btn.grid(row=self.rowcount1+2,
                               columnspan=2, pady=(5, 20))

        self.name_label = Label(self.create_order_frame,
                                text="Name: ", width=wd)
        self.name_label.grid(row=self.rowcount1+3, column=0)
        self.name_entry = Entry(self.create_order_frame,
                                textvariable=self.name_var, width=wd)
        self.name_entry.grid(row=self.rowcount1+3, column=1)

        self.pickup = Radiobutton(self.create_order_frame, text="Pick-Up",
                                  value="Pick-Up",
                                  variable=self.collection_var, width=wd)
        self.pickup.grid(row=self.rowcount1+4, column=0)
        self.delivery = Radiobutton(self.create_order_frame,
                                    text="Delivery ($15 Fee)",
                                    value="Delivery",
                                    variable=self.collection_var, width=wd)
        self.delivery.grid(row=self.rowcount1+4, column=1)

        self.enter_button = Button(self.create_order_frame, text="SUBMIT",
                                   command=self.submit_order,
                                   state="disabled", width=wd)
        self.enter_button.grid(row=self.rowcount1+5, column=0,
                               sticky=W, pady=(20, 5))

        self.view_orders_btn = Button(self.create_order_frame,
                                      text="View Orders",
                                      command=self.view_orders,
                                      state="disabled", width=wd)
        self.view_orders_btn.grid(row=self.rowcount1+5, column=1,
                                  sticky=E, pady=(20, 5))

        # CREATE DISPLAY WIDGETS
        self.display_order_label = Label(self.display_order,
                                         text="Display Orders", width=wd)
        self.display_order_label.grid(row=0, column=0)
        self.add_new_btn = Button(self.display_order, text="Add New Order",
                                  command=self.display_to_create, width=wd)
        self.add_new_btn.grid(row=0, column=1)

        self.previous_order_btn = Button(
            self.display_order, text="Previous",
            command=self.display_previous, width=10)
        self.next_order_btn = Button(
            self.display_order, text="Next",
            command=self.display_next, width=10)
        self.previous_order_btn.grid(row=1, column=0, sticky=W, pady=(5, 20))
        self.next_order_btn.grid(row=1, column=1, sticky=E, pady=(5, 20))

        # Text will be added later
        self.name_display = Label(self.display_order, text="", width=wd2)
        self.name_display.grid(row=2, columnspan=2)
        self.total_price_display = Label(self.display_order,
                                         text="", width=wd2)
        self.total_price_display.grid(row=3, columnspan=2)
        self.collection_display = Label(self.display_order, text="", width=wd2)
        self.collection_display.grid(row=4, columnspan=2)
        self.item_display = Label(self.display_order, text="Items: ", width=wd)
        self.item_display.grid(row=5, column=0)

    def submit_order(self):
        """Save order as an instance of the Order class."""
        if self.name_var.get().strip() == "":
            messagebox.showerror("Error", "Please enter a name")
            self.name_entry.delete(0, END)
            self.name_entry.focus()
        elif len(self.current_items) == 0:
            messagebox.showerror("Error", "Please select an item")
        else:
            self.view_orders_btn.configure(state="normal")
            self.enter_button.configure(state="disabled")
            name = self.name_var.get().title()
            # Create list of item names for display
            item_names = [item[0] for item in self.current_items]
            amount = [item[1] for item in self.current_items]
            # Calculate total price
            price = 0
            collection_method = self.collection_var.get()
            for thing in self.current_items:
                for item in self.menu:
                    if item[0] == thing[0]:
                        price += int(item[1])*int(thing[1])
            if collection_method == "Delivery":
                price += 15
            self.orders.append(Order(
                name, item_names, amount, price, collection_method))
            self.current_items = []  # Reset list
            self.name_entry.delete(0, END)
            self.name_entry.focus()
            self.collection_var.set("Pick-Up")

    def display_to_create(self):
        """Change to create_order frame."""
        self.menu_frame.grid(row=0, columnspan=2)
        self.create_order_frame.grid()
        self.display_order.grid_forget()
        # Reset rowcounts
        self.rowcount1 = 0
        self.rowcount2 = 6

    def display_next(self):
        """Display next order."""
        if self.index >= len(self.orders) - 1:
            self.index = 0  # Loops around
        else:
            self.index += 1
        self.clear_display()

    def display_previous(self):
        """Display previous order."""
        if self.index == 0:
            self.index = len(self.orders) - 1  # Loops around
        else:
            self.index -= 1
        self.clear_display()

    def clear_display(self):
        """Destroy item labels."""
        for temp in self.temp_list:
            temp.destroy()
        self.temp_list.clear()
        self.rowcount2 = 6
        self.configure_display_labels()

    def add_item(self):
        """Save selected item to list and reset input widgets."""
        if self.selected_option_var.get() == "Select an item":
            messagebox.showerror("Error", "Please select an item")
        else:
            try:
                int(self.amount_var.get())
                if int(self.amount_var.get()) <= 0:
                    raise ValueError
                else:
                    var = [self.selected_option_var.get(),
                           self.amount_var.get()]
                    self.current_items.append(var)
                    self.selected_option_var.set("Select an item")
                    self.enter_button.configure(state="normal")
                    self.amount_entry.delete(0, END)
            except ValueError:
                messagebox.showerror("Error",
                                     "Please enter a positive, whole number")
                self.amount_entry.delete(0, END)
                self.amount_entry.focus()

    def view_orders(self):
        """Change to display_order frame."""
        self.menu_frame.grid_forget()
        self.create_order_frame.grid_forget()
        self.display_order.grid()
        self.configure_display_labels()

    def configure_display_labels(self):
        """Update labels using index number. Remove previous item labels."""
        item = self.orders[self.index]
        self.name_display.configure(
            text="Name: " + str(item.name))
        # Clear previous labels
        for temp in self.temp_list:
            temp.destroy()
        self.temp_list.clear()
        self.rowcount2 = 6
        self.total_price_display.configure(
            text="Total Price: $" + str(item.price))
        self.collection_display.configure(
            text=f"Collection by {item.collection_method}")

        for i in range(len(item.item_ordered)):
            label = Label(self.display_order,
                          text=f"x{item.amount[i]} {item.item_ordered[i]}",
                          width=15)
            label.grid(row=5 + i, column=1, sticky=W)
            self.temp_list.append(label)
            self.rowcount2 += 1


if __name__ == "__main__":
    root = Tk()
    start = Main(root)
    root.title("Shop")
    root.mainloop()

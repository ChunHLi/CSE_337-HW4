import shelve
from tkinter import *

data = shelve.open("database")


class Contact:

    def __init__(self):

        self.name = "";
        self.address = "";
        self.phone = ""
        self.personal = False


class MainScreen:

    def __init__(self, master):

        self.master = master
        self.frame = Frame(self.master)
        self.createEdit_button = Button(self.frame, text="CreateEdit Record", width=50, command=createEdit)
        self.search_button = Button(self.frame, text="Search Record", width=50, command=search)
        self.delete_button = Button(self.frame, text="Delete Record", width=50, command=delete)
        self.createEdit_button.pack()
        self.search_button.pack()
        self.delete_button.pack()
        self.frame.pack()


def createEdit():

    def save():

        entry = name_entry.get()
        if entry in data:
            data[entry].name = name_entry.get()
            data[entry].address = address_entry.get()
            data[entry].phone = phone_entry.get()
            data[entry].personal = (t.get() == 1)
            saved_label.config(text="Record Edited")
        else:
            new_entry = Contact()
            new_entry.name = name_entry.get()
            new_entry.address = address_entry.get()
            new_entry.phone = phone_entry.get()
            new_entry.personal = (t.get == 1)
            data[entry] = new_entry
            saved_label.config(text="Record Made")

    t = IntVar()
    window = Toplevel()
    window.title("CreateEdit")
    name_label = Label(window, text="Name")
    name_entry = Entry(window, width=80)
    phone_label = Label(window, text="Phone")
    phone_entry = Entry(window, width=80)
    address_label = Label(window, text="Address")
    address_entry = Entry(window, width=80)
    personal_button = Radiobutton(window, text="Personal", variable=t, value=0)
    business_button = Radiobutton(window, text="Business", variable=t, value=1)
    save_button = Button(window, text="Save Record", command=save)
    saved_label = Label(window, text=" ")
    name_label.grid(row=0, column=0)
    name_entry.grid(row=0, column=1)
    phone_label.grid(row=1, column=0)
    phone_entry.grid(row=1, column=1)
    address_label.grid(row=2, column=0)
    address_entry.grid(row=2, column=1)
    personal_button.grid(row=3, column=0)
    business_button.grid(row=3, column=1)
    save_button.grid(row=4, column=0)
    saved_label.grid(row=4, column=1)



def search():

    def searchHelper():

        entry = search_name_entry.get()
        if entry in data:
            search_found_label.config(text="Record Available")
            search_found_name.config(text="Name: " + data[entry].name)
            search_found_phone.config(text="Phone: " + data[entry].phone)
            search_found_address.config(text="Address: " + data[entry].address)
            if data[entry].personal:
                search_found_personal.config(text="Type: Personal")
            else:
                search_found_personal.config(text="Type: Business")

    window = Toplevel()
    window.title("Search")
    search_name_label = Label(window, text="Name")
    search_name_entry = Entry(window, width=80)
    search_search_button = Button(window, text="Search", command=searchHelper)
    search_found_label = Label(window, text="Record Unavailable")
    search_found_name = Label(window, text="Name: ")
    search_found_phone = Label(window, text="Phone: ")
    search_found_address = Label(window, text="Address: ")
    search_found_personal = Label(window, text="Type: ")
    search_name_label.grid(row=0, column=0)
    search_name_entry.grid(row=0, column=1)
    search_search_button.grid(row=1, column=0, columnspan=2)
    search_found_label.grid(row=2, column=1)
    search_found_name.grid(row=3, column=1)
    search_found_phone.grid(row=4, column=1)
    search_found_address.grid(row=5, column=1)
    search_found_personal.grid(row=6, column=1)


def delete():

    def deleteHelper():

        entry = delete_name_entry.get()
        if entry in data:
            del data[entry]
            delete_deleted_label.config(text="Record no longer exists")
        else:
            delete_deleted_label.config(text="Record never existed")

    window = Toplevel()
    window.title("Delete")
    delete_name_label = Label(window, text="Name: ")
    delete_name_entry = Entry(window, width=80)
    delete_delete_button = Button(window, text="Delete", command=deleteHelper)
    delete_deleted_label = Label(window, text=" ")
    delete_name_label.grid(row=0, column=0)
    delete_name_entry.grid(row=0, column=1)
    delete_delete_button.grid(row=1, column=0, columnspan=2)
    delete_deleted_label.grid(row=2, column=1)


if __name__ == "__main__":
    root = Tk()
    root.title("Telephone Database")
    app = MainScreen(root)
    root.mainloop()
    data.close()

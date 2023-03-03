from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- FIND PASSWORD ------------------------------- #


def search_password():

    webiste = website_entry.get()
    try:
        with open("data.json", mode="r") as file:
            # Reading old data
            data = json.load(file)  # data is a dictionary
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if webiste in data:
            email = data[webiste]["email"]
            password = data[webiste]["password"]
            messagebox.showinfo(title=webiste, message=f"Email: {email}\n"
                                                       f"Password: {password}")
        else:
            messagebox.showinfo(title="Error", message="No details for the website exists.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    #List Comprehension
    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    #join method
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
#JASON - JavaScriptObjectNotation


def save_password():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }

    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as file:
                # Reading old data
                data = json.load(file)  # data is a dictionary
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                # Saving updated data
                json.dump(new_data, file, indent=4)  # write
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", mode="w") as file:
                #Saving updated data
                json.dump(data, file, indent=4)  # write
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
password_image = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=password_image)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=33)
website_entry.grid(row=1, column=1)
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "avramescu.alexandra@gmail.com")
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

#Buttons
generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=44, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=15, command=search_password)
search_button.grid(row=1, column=2)



window.mainloop()


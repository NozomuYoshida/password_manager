from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list_letters = [choice(letters) for _ in range(randint(2, 4))]
    password_list_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list_numbers = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_list_letters + password_list_symbols + password_list_numbers

    shuffle(password_list)
    password = ''.join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }

    empty_data = {
        '': {
            '': '',
            '': ''
        }
    }
    is_empty = len(website) == 0 or len(email) == 0 or len(password) == 0
    if is_empty:
        messagebox.showwarning(title='Oops', message='Please do not leave any fields empty!')
    else:
        try:
            with open('data.json', 'r') as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open('data.json', 'w') as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_email.delete(0, END)
            entry_password.delete(0, END)


# ---------------------------- SEARCH WEBSITE ------------------------------- #

def find_website():
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError as error_message:
        messagebox.showinfo(title='There\'s no existing data file', message='No Data File Found')
    else:
        entered_website = entry_website.get()
        if entered_website in data.keys():
            website = entered_website
            password = data[entered_website]['password']
            messagebox.showinfo(title='There\'s existing password', message=f'website: {website}\npassword: {password}')
        else:
            messagebox.showinfo(title='There\'s no existing password', message='There\'s no existing password')
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('MyPass')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.gif')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

label_website = Label(text='Website:')
label_website.grid(row=1, column=0)
entry_website = Entry(width=25)
entry_website.grid(row=1, column=1)
button_search_website = Button(text='Search', width=10, command=find_website)
button_search_website.grid(row=1, column=2)


label_email = Label(text='Email/Username:')
label_email.grid(row=2, column=0)
entry_email = Entry(width=38)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(0, 'example@example.com')

label_password = Label(text='Password:')
label_password.grid(row=3, column=0)
entry_password = Entry(width=25)
entry_password.grid(row=3, column=1)
button_generate_password = Button(text='Generate Password', width=10, command=generate_password)
button_generate_password.grid(row=3, column=2)

button_add_password = Button(text='Add', width=36, command=save)
button_add_password.grid(row=4, column=1, columnspan=2)

window.mainloop()
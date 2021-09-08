from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
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
    
    is_empty = len(website) == 0 or len(email) == 0 or len(password) == 0
    if is_empty:
        messagebox.showwarning(title='Oops', message='Please do not leave any fields empty!')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {email}'
                                                      f'\nPassword: {password} \nIs it ok to save?')
        if is_ok:
            with open('data.txt', 'a') as file:
                file.write(f'{website} | {email} | {password}\n')
            entry_website.delete(0, END)
            entry_email.delete(0, END)
            entry_password.delete(0, END)
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
entry_website = Entry(width=38)
entry_website.grid(row=1, column=1, columnspan=2)


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
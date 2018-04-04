import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

#root.attributes('-fullscreen', True)
root.geometry('2000x2000')
root.title('AppCop 1.0')

button_frame = tk.Frame(root)
button_frame.pack(fill=tk.X, side=tk.TOP)

button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)
button_frame.columnconfigure(3, weight=1)

image = tk.PhotoImage(file="AppCop_logo.PNG")
label = tk.Label(image=image)
label.pack()

def f_HostnameIP():
    import AppCopUtil as f_machine_details
    host_machine_detail = ''
    host_machine_detail = f_machine_details.get_Host_IP()
    messagebox.showinfo("Logged in User Hostname & IP",host_machine_detail)
    
        
def f_PasswordGen():
    import AppCopUtil as f_auto_password
    auto_password_gen = ''
    auto_password_gen = f_auto_password.gen_Password()
    messagebox.showinfo("Auto Generated Password",auto_password_gen)

def f_CardValidate():    
    import AppCopUtil as f_card_validate
    Card_Details = ''
    Card_Number = ''
    # Create the Entry widget   PENDING WORK
    
##    Card_Number = input ('Enter Card Number to Validate >>>')
    Card_Details = f_card_validate.card_validate(Card_Number)
    messagebox.showinfo("Card Validation Check",Card_Details)

Ip_button = tk.Button(button_frame, text='Get Hostname & IP Address of Local Machine', command = f_HostnameIP)
Pass_button = tk.Button(button_frame, text='Automated Password Generator', command = f_PasswordGen)
Card_button = tk.Button(button_frame, text='Validate Your Card Number', command = f_CardValidate)
Exit_button = tk.Button(button_frame, text='Exit', command = exit)

Ip_button.grid(row=3, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
Pass_button.grid(row=3, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
Card_button.grid(row=3, column=2, sticky=tk.N+tk.S+tk.E+tk.W)
Exit_button.grid(row=3, column=3, sticky=tk.N+tk.S+tk.E+tk.W)

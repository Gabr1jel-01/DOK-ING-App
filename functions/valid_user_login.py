from main_code import *
from functions.log_in_button_action import *
from functions.successfull_login import *





def valid_user_login():
    
    username = username_entry_box2.get()
    password = password_entry_box2.get()
    
    if username !='' and password !='':
        cursor.execute('SELECT password FROM users WHERE username=?', [username])
        result = cursor.fetchone()
        if result:
            if bcrypt.checkpw(password.encode('utf-8'), result[0]):
                messagebox.showinfo('Success', 'Logged in successfully.')
                main_window2.destroy()
                successfull_login()
            else:
               messagebox.showerror('Error', 'Invalid password')
        else:
            messagebox.showerror('Error', 'Invalid username.')
    else:
        messagebox.showerror('Error', 'Enter all data.')
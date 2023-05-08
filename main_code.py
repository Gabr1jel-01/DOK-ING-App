import customtkinter as ctk
from app_constants import *
import bcrypt
import sqlite3
from tkinter import messagebox
from tkinter import *
from app_functions import *
 
 
  
#region MAIN WINDOW
ctk.set_appearance_mode('Dark')
main_window = ctk.CTk()
main_window.title('SmartKey')
main_window.geometry('600x500')
#endregion

#region APP TITLE
   
label_main_window = ctk.CTkLabel(main_window,
                                    text='SMART KEY APPLICATION by ALGEBRA',
                                    font=TITLE_FONT)
label_main_window.pack(padx=TITLE_PADX, pady=TITLE_PADY)
#endregion

#region USERNAME

username_title = ctk.CTkLabel(main_window,
                                text='Username',
                                font=SUBTITLE_FONT)
username_title.pack(padx=SUBTITLE_PADX, pady=SUBTITLE_PADY)

username_entry_box = ctk.CTkEntry(main_window,
                                width=200,
                                height=8)
username_entry_box.pack()
#endregion

#region PASSWORD

password_title = ctk.CTkLabel(main_window,
                                text='Password',
                                font=SUBTITLE_FONT)
password_title.pack(padx=SUBTITLE_PADX, pady=SUBTITLE_PADY)
password_entry_box = ctk.CTkEntry(main_window,
                                width=200,
                                height=8,
                                show='*')
password_entry_box.pack()

#endregion

#region SIGN UP BUTTON

sign_up_button = ctk.CTkButton(main_window,
                                 width=140,
                                 height=20,
                                 text='Sign Up',
                                 command= sign_up_button_action)
sign_up_button.pack(padx=0,pady=50)

#endregion

#region ALREADY ACC LABEL
   
already_acc_label = ctk.CTkLabel(main_window,
                                    text='Already have an account?',
                                    font=SUBTITLE_FONT)
already_acc_label.pack(padx=10, pady=2)
#endregion
    
#region LOG_IN Button
    
log_in_button = ctk.CTkButton(main_window,
                             width=140,
                                 height=20,
                                 text='Log In',
                                 command= lambda: [main_window.destroy(), log_in_button_action()])
log_in_button.pack(padx=15,pady=25)
#endregion
    
#region SQLITE3
    
sql_connection = sqlite3.connect('database.db')
cursor = sql_connection.cursor()
    
cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT NOT NULL,
            password TEXT NOT NULL)''')
    
    
#endregion
    
    
main_window.mainloop()
    





import customtkinter as ctk
from app_constants import *
import bcrypt
import sqlite3
from tkinter import messagebox
from tkinter import *


#region FUNKCIJE
def successfull_login():
    
    ctk.set_appearance_mode('Dark')
    main_window3 = ctk.CTk()
    main_window3.title('SmartKey')
    main_window3.geometry('600x500')
    
    title = Label(main_window3,
                  text='Smart House',
                  font=TITLE_FONT,
                  bg='grey')
    title.grid(row=0,column=0)
    
    
    
    
    
    
    
    
    main_window3.mainloop()
    
    pass

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

def sign_up_button_action():
        
    username = username_entry_box.get()
    password = password_entry_box.get()
        
    if username !='' and password != '':
        cursor.execute('SELECT username FROM users WHERE username = ?', [username])
        if cursor.fetchone() is not None:
                messagebox.showerror('Error', 'Username already exists.')
                result = cursor.fetchone()
                print(result)           
            
        else:
            encoded_password = password.encode('utf-8')
            hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
            #print(hashed_password)
            cursor.execute('INSERT INTO users VALUES (?,?)', [username, hashed_password])
            sql_connection.commit()
            messagebox.showinfo('Success', 'Account has been created!')
    else:
        messagebox.showerror('Error', 'Please enter both Username and Password')
    if cursor.fetchone() is not None:
        result = cursor.fetchone()
            
def log_in_button_action():
    
    global username_entry_box2
    global password_entry_box2
       
    #region MAIN WINDOW 2
    global main_window2
    main_window2 = ctk.CTk()
    main_window2.title('SmartKey')
    main_window2.geometry('600x500')
    ctk.set_appearance_mode('Dark')
        
    #endregion
        
    #region APP TITLE 2
    label_main_window2 = ctk.CTkLabel(main_window2,
                                text='SMART KEY APPLICATION by ALGEBRA',
                                font=TITLE_FONT)
    label_main_window2.pack(padx=TITLE_PADX, pady=TITLE_PADY)
    #endregion
        
    #region USERNAME 2

    username_title2 = ctk.CTkLabel(main_window2,
                            text='Username',
                            font=SUBTITLE_FONT)
    username_title2.pack(padx=SUBTITLE_PADX, pady=SUBTITLE_PADY)

    username_entry_box2 = ctk.CTkEntry(main_window2,
                            width=200,
                            height=8)
    username_entry_box2.pack()
    #endregion
        
    #region PASSWORD 2

    password_title2 = ctk.CTkLabel(main_window2,
                            text='Password',
                            font=SUBTITLE_FONT)
    password_title2.pack(padx=SUBTITLE_PADX, pady=SUBTITLE_PADY)

    password_entry_box2 = ctk.CTkEntry(main_window2,
                            width=200,
                            height=8,
                            show='*')
    password_entry_box2.pack()

    #endregion
    
    #region LOG_IN Button
    
    log_in_button = ctk.CTkButton(main_window2,
                                width=140,
                                    height=20,
                                    text='Log In',
                                    command=valid_user_login)
    log_in_button.pack(padx=15,pady=25)
    #endregion
    
    # BACK TO SIGN UP PAGE
    
    back_to_sign_up = ctk.CTkButton(main_window2,
                                    width=140,
                                    height=20,
                                    text='Back to sign up page',
                                    command= log_in_button_action)
    
    back_to_sign_up.pack(padx=20,pady=30)
    
    
    
    
    
    main_window2.mainloop()
#endregion

  
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
    





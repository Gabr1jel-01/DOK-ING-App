from main_code import *



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
from main_code import *
from functions.valid_user_login import *
from functions.back_to_sign_up_action import *


def log_in_button_action():
    
    global username_entry_box2
    global password_entry_box2
       
    #region MAIN WINDOW 2
    global main_window2
    main_window2 = ctk.CTk()
    main_window2.title('TERMINATOR 2 by DOK-ING')
    main_window2.geometry('800x600')
    main_window2.iconbitmap('DOK-ING-Logo.ico')
    ctk.set_appearance_mode('System')
        
    #endregion
        
    #region APP TITLE 2
    label_main_window2 = ctk.CTkLabel(main_window2,
                                text='TERMINATOR 2 by DOK-ING',
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
                                    command= back_to_sign_up_action)
    
    back_to_sign_up.pack(padx=20,pady=30)
    
    
    main_window2.mainloop()
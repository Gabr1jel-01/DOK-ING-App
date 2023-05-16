from main_code import *




def successfull_login():
    ctk.set_appearance_mode('System')
    main_window3 = ctk.CTk()
    main_window3.title('TERMINATOR 2 by DOK-ING')
    main_window3.geometry('800x600')
    main_window3.iconbitmap('DOK-ING-Logo.ico')
    
    bg = PhotoImage( file = "background.png")
    app_canvas = Canvas(main_window3, width=800 , height=600)
    app_canvas.pack(fill='both', expand=True)
    
    app_canvas.create_image(0,0, image=bg, anchor='nw')
    
    
    title = Label(main_window3,
                  text='TERMINATOR 2 by DOK-ING',
                  font=TITLE_FONT,
                  )
    title.pack(padx=0,pady=0)
    
    title_above_listbox = Label(main_window3,
                                text='Ispis podataka')
    
    list_box = Listbox(main_window3,
                       bg='white',
                       highlightcolor='#33FFFC',
                       width=40)
    
    list_box.pack(padx=10,pady=100, side=LEFT)
    
    
    main_window3.mainloop()
    
    pass
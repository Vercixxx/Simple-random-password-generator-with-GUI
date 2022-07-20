from tkinter import *
from tkinter import messagebox
import string
import random


def pass_gen(small_letters, big_letters, digitss, symbolss, lenn):
    """Function pass_gen generates password using random module, on given instrucions.

    Args:
        small_letters (bool): If true adds small letters to password
        big_letters (bool): If true adds big letters to password
        digitss (bool): If true adds digits (0-9) to password
        symbolss (bool): If true adds symbols to password
        len (int): Length of password

    Returns:
        String: Randomly generated password
    """
    small_letters_list = list(string.ascii_lowercase)
    big_letters_list = list(string.ascii_uppercase)
    digitss_list = list(string.digits)
    symbolss_list = list(string.punctuation)

    list_of_characters = []
    
    if small_letters:
        list_of_characters = list_of_characters + small_letters_list
    
    if big_letters:
        list_of_characters = list_of_characters + big_letters_list
            
    if digitss:
        list_of_characters = list_of_characters + digitss_list
            
    if symbolss:
        list_of_characters = list_of_characters + symbolss_list
        

    
    random.shuffle(list_of_characters)

    output = random.choices(list_of_characters, k = lenn)
    output = "".join(output)
    return output


def show_frame(frame):
    frame.tkraise()


def menu_top():
    
    def help_menu():
        messagebox.showinfo('Help', 'This program is made for creating randomly generated password with spcified properties. To create password u have to select desired collections, and specified length. Than just click generate, and password will be automaticly generated. ')
    
    def author():
        messagebox.showinfo('Author info', 'Author => Krzysztof Służałek\nLinkedin =>linkedin.com/in/krzysztof-sluzalek')
        
    
    #Menu on top
    my_menu = Menu(root)
    root.config(menu=my_menu)


    #===============Menu items===============
    
    #label "File"
    file_menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label= "Exit", command= root.quit)


    #label "More"
    more_menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label= "More", menu=more_menu)
    more_menu.add_command(label= "Help", command= help_menu)
    more_menu.add_command(label= "Author", command= author)


def show_welcome_frame():
    """
        Only shows Welcome frame first
    """
    show_frame(welcome_frame)

    

def generate_password():
    if small_letters.get() == False and big_letters.get() == False and digitss.get() == False and symbolss.get() == False:
        messagebox.showinfo('Error', 'Please select at least one option')
        
       
    else: 
        password = pass_gen(small_letters.get(),big_letters.get(),digitss.get(),symbolss.get(),password_len.get())

 
        #Result text
        outp_1 = Frame(main_frame)
        outp_1.grid(row=8, column=0, columnspan=2)

        Label(outp_1, text="Generated password: ", background= '#339933', font='Helvetica 13 bold').pack()


        #Result
        outp_2 = Frame(main_frame)
        outp_2.grid(row=9, column=0, columnspan=2)
        
        name = StringVar(outp_2, value=password)
        Entry(outp_2, textvariable=name, background= '#339933', bd=0, justify=CENTER, font='Helvetica 13 bold', width=75, cursor='arrow').pack()
        
        




root = Tk()
root.geometry("640x400")
root.title("Password generator")
root.iconbitmap('c:/Users/KrissTheKing/Desktop/Python/Password_generator_GUI/icon.ico')
root.resizable(False, False)


root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


welcome_frame = Frame(root)
main_frame = Frame(root, background= '#339933')

background_image = PhotoImage(file="c:/Users/KrissTheKing/Desktop/Python/Password_generator_GUI/background_image.png")
label_background_welcome = Label(welcome_frame, image=background_image)
label_background_welcome.place(x=0, y=0, relwidth=1, relheight=1)



for frame in (welcome_frame,main_frame):
    
    frame.grid(row= 0, column=0,sticky='nsew')




show_welcome_frame()
menu_top()




#===============Welcome frame===============

welcome_frame.columnconfigure(0, weight=1)

header_fram = Frame(welcome_frame)
header_fram.grid(row=0, column=0, pady=10, padx=10)
Label(header_fram, text="Hi! I am glad to welcome you in my first GUI program. \nThis program will generate password with specified properties.", background= '#339933', font= 'Helvetica 13 bold').pack()




button_start = Frame(welcome_frame)
button_start.grid(row=1, column=0, columnspan=2, pady=140)



Button(button_start, text= "Let's generate password!", command=lambda:show_frame(main_frame), background="#0DD000", activeforeground="#FFFFFF", activebackground="#222222", relief="ridge", bd="4", width ="40", height="5", font='Helvetica 11 bold').pack()







#===============Main frame===============


main_frame.columnconfigure(0, weight=1)


big_frame = LabelFrame(main_frame, text="Configure options below", font='Helvetica 14 bold', background= '#339933')
big_frame.grid(padx=10, pady=10)


#First checkbox (small letters)
option_1 = Frame(big_frame)
option_1.grid(row=0, column=0, sticky=W, padx=(2,10))

small_letters = BooleanVar()
small_letters_checkbox = Checkbutton(option_1, variable=small_letters, background= '#339933', font='Helvetica 13', onvalue=True, offvalue=False).pack()


option_1_1 = Frame(big_frame)
option_1_1.grid(row=0, column=1, sticky=W, padx=(0,500))
Label(option_1_1, text="Small letters", background= '#339933', font='Helvetica 12 bold').pack()




#Second checkbox (big letters)
option_2 = Frame(big_frame)
option_2.grid(row=1, column=0, sticky=W, padx=(2,10))

big_letters = BooleanVar()
big_letters_checkbox = Checkbutton(option_2, variable=big_letters,  background= '#339933', font='Helvetica 13', onvalue=True, offvalue=False).pack()

option_2_1 = Frame(big_frame)
option_2_1.grid(row=1, column=1, sticky=W)
Label(option_2_1, text="Big letters", background= '#339933', font='Helvetica 12 bold').pack()




#Third checkbox (digits)
option_3 = Frame(big_frame)
option_3.grid(row=3, column=0, sticky=W, padx=(2,10))

digitss = BooleanVar()
digitss_checkbox = Checkbutton(option_3, variable=digitss,  background= '#339933', font='Helvetica 13', onvalue=True, offvalue=False).pack()

option_3_1 = Frame(big_frame)
option_3_1.grid(row=3, column=1, sticky=W)
Label(option_3_1, text="Digits", background= '#339933', font='Helvetica 12 bold').pack()



#Fourth checkbox (symbols)
option_4 = Frame(big_frame)
option_4.grid(row=4, column=0, sticky=W, padx=(2,10))

symbolss = BooleanVar()
symbolss_checkbox = Checkbutton(option_4, variable=symbolss, background= '#339933', font='Helvetica 13', onvalue=True, offvalue=False).pack()

option_4_1 = Frame(big_frame)
option_4_1.grid(row=4, column=1, sticky=W)
Label(option_4_1, text="Symbols", background= '#339933', font='Helvetica 12 bold').pack()



#Password length
option_5 = Frame(big_frame)
option_5.grid(row=5, column=0, columnspan=2, padx=(2,10), sticky=W)
Label(option_5, text="Password length", background= '#339933', font='Helvetica 12 bold').pack()

option_5_1 = Frame(big_frame)
option_5_1.grid(row=6, column=0, columnspan=2, padx=(2,10), sticky=W)

password_len = IntVar()
pass_len = Scale(option_5_1, from_=8, to= 50, orient=HORIZONTAL, background= '#339933', variable=password_len, width=20, length=200, cursor='sb_h_double_arrow').pack()





button_generate = Frame(main_frame)
button_generate.grid(row=7, column=0, columnspan=2, pady=3)

Button(button_generate, text= "Generate", command=generate_password, background="#0DD000", activeforeground="#FFFFFF", activebackground="#222222", relief="ridge", bd="2", width=30, height=2).pack()






root.mainloop()
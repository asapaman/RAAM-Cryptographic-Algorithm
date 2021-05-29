from new_encrypt import *
from new_decryption import *
from incrypt_2 import *
# Python program to create
# a file explorer in Tkinter

# import all components
# from the tkinter library


from tkinter import *

# import filedialog module
from tkinter import filedialog

filename = ''
Algo_no=0
# Function for opening the
# file explorer window
def browseFiles():
    global filename
    filename = filedialog.askopenfilename(initialdir="/",title="Select an Image File",filetypes=(("image", ".jpeg"),("image", ".png"),("image", ".jpg"),("all files","*.*")))

    # Change label contents
    label_file_explorer.configure(text="File Opened: " + filename)
    print(filename)

# Create the root window
window = Tk()

# Set window title
window.title('Image Encryptor & Decryptor')

# Set window size
window.geometry("500x500")

# Set window background color
window.config(background="grey")

# Create a File Explorer label
label_file_explorer = Label(window, text="Encrypt and Decrypt Image File", width=100, height=4,fg="blue")

button_explore = Button(window, text="Browse Image", command=browseFiles)


#label_file_explorer.grid(column=1, row=1)
label_file_explorer.pack()

#button_explore.grid(column=1, row=2)
button_explore.pack()

def setRAAM():
    global Algo_no
    Algo_no = 1
    CheckVar2.set(0)

def setVig():
    global Algo_no
    Algo_no = 2
    CheckVar1.set(0)


#button_exit.grid(column=1, row=3)
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(window, text = "RAAM Algo", variable = CheckVar1, onvalue = 1, offvalue = 0, height=5, width = 20, command=setRAAM)
C2 = Checkbutton(window, text = "Vigenere", variable = CheckVar2, onvalue = 1, offvalue = 0, height=5, width = 20, command=setVig)
C1.pack()
C2.pack()



passw_var = StringVar()


# defining a function that will
# get the name and password and
# print them on the screen
#=======================================================================================================
def encfun():
    password = passw_var.get()
    print(filename)
    print("enc password = ", password)
    print("algo NO", Algo_no)
    if(filename=='' or password=='' or Algo_no==0):
        label_file_explorer.configure(text="error... please fill all the data correctly")
        return
    if Algo_no == 1:
        raam_enc(filename,password)
    elif Algo_no == 2:
        enc(filename, password)

    label_file_explorer.configure(text="Image Encrypted ")
    passw_var.set("")


def decfun():
    password = passw_var.get()
    print(filename)
    print("dec password = ", password)
    print("algo NO", Algo_no)
    if(filename=='' or password=='' or Algo_no==0):
        label_file_explorer.configure(text="error... please fill all the data correctly")
        return

    if Algo_no == 1:
        raam_dec(filename,password)
    elif Algo_no == 2:
        dec(filename, password)

    label_file_explorer.configure(text="Image Decrypted")
    passw_var.set("")
#============================================================================================================
# creating a label for password
passw_label = Label(window, text='Password',padx=20, font=('calibre', 10, 'bold'))
passw_label.pack()#grid(row=1, column=0)

# creating a entry for password
passw_entry = Entry(window, textvariable=passw_var, font=('calibre', 10, 'normal'))
passw_entry.pack()#grid(row=1, column=1)

# creating a button using the widget
# Button that will call the submit function
enc_btn = Button(window, text='encrypt',padx=20, command=encfun)
dec_btn = Button(window, text='decrypt',padx=20, command=decfun)
# placing the label and entry in
# the required position using grid method
enc_btn.pack()#grid(row=2, column=1)
dec_btn.pack(padx =50)#grid(row=2, column=1)

button_exit = Button(window, text="Exit",padx=25, command=exit)
button_exit.pack()

# Let the window wait for any events
window.mainloop()

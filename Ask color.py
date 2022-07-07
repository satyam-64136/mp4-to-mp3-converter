# Python program to create color chooser dialog box

# importing tkinter module
from tkinter import *

# importing the choosecolor package
from tkinter import colorchooser

# Function that will be invoked when the
# button will be clicked in the main window
def choose_color():

	# variable to store hexadecimal code of color
	color_code = colorchooser.askcolor(title ="Choose color")
	print(color_code)
def changeOnHover(button, colorOnHover, colorOnLeave):
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))
  
    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))

root = Tk()

root.resizable(False, False)
button = Button(root, text = "Select color",
				command = choose_color)
button.place(relx=0.5, rely=0.5, anchor=CENTER,height=100,width=100)
changeOnHover(button, "white", "#ff040b")
root.geometry("300x300")
root.mainloop()

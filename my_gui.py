from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from moviepy.editor import *
import os

window_root = Tk()
#creating a window
window_root.title("Video To Audio Converter.")
window_root.minsize(800,400)
window_root.maxsize(800,400)
canvas = Canvas(window_root,width=800,height=400)
canvas.grid(columnspan=3,rowspan=3)

#making logo
logo = Image.open("my_mp3_converter\\image.png")#image should be of 240 x 240 pixels
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0, sticky="nsew")

#Giving instructions
instructions = Label(window_root, text="Select a Video file on your computer to convert it in Mp3.", font="Raleway 20 bold")
instructions.grid(columnspan=3, column=0, row=1)

#opening and converting to mp3
def open_file():
    Browse_text.set("Loading...")
    file = askopenfile(parent=window_root, mode='rb', initialdir = '/',title = 'Select file',filetypes = (('mp4 files','*.mp4'),('all files','*.*'))) 
    z = os.path.realpath(file.name) 
    mp4_file = z
    mp3_file = "{}.mp3".format(mp4_file)
    videoClip = VideoFileClip(mp4_file)
    audioclip = videoClip.audio
    audioclip.write_audiofile(mp3_file)
    audioclip.close()
    videoClip.close()
  
    Browse_text.set("Click To Browse")

#Making browse button
def changeOnHover(button, colorOnHover, colorOnLeave):
    button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))
  
    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))

Browse_text = StringVar()
Browse_button = Button(window_root, textvariable=Browse_text,font="Raleway 15 bold", bg="#ff040b", fg="white", height=1, width=20,command=open_file)
Browse_text.set("Click To Browse")
Browse_button.grid(column=1, row=2)
changeOnHover(Browse_button, "#fe5050", "#ff040b")#Change the colour as per your needs.

window_root.mainloop()

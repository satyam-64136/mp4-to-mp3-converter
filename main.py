import moviepy.editor as me
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.ttk import Style

filename = ''

def convert():
    global filename
    filetypes = (("Audio files", "*.mp3;*.wav;*.ogg"), ("All files", "*.*"))
    try:
        video = me.VideoFileClip(filename)
        audio = video.audio
        file = asksaveasfilename(defaultextension=format.get(), filetypes=filetypes)
        if file:
            audio.write_audiofile(file)
            label5 = Label(root, text="✓ Converted!", font=("Arial", 16, "bold"), fg="#4CAF50", bg="#2E2E2E")
            label5.place(x=450, y=300)
    except Exception as e:
        label5 = Label(root, text=f"✗ Error: {str(e)}", font=("Arial", 16, "bold"), fg="#F44336", bg="#2E2E2E")
        label5.place(x=450, y=300)

def select():
    global filename
    filetypes = (
        ('Video files', '*.webm;*.mpg;*.mp2;*.mpeg;*.mpe;*.mpv;*.mp4;*.m4p;*.m4v;*.avi;*.wmv;*.mov;*.qt;*.flv;*.swf;*.avchd'),
        ('All files', '*.*')
    )
    filename = askopenfilename(filetypes=filetypes)
    if filename:
        label3.config(text="✓ Video Selected", fg="#4CAF50", bg="#2E2E2E")
        label4 = Label(root, text="Select Audio Format", font=("Arial", 16, "bold"), bg="#2E2E2E", fg="white")
        label4.place(x=125, y=250)
        options = [".mp3", ".ogg", ".wav"]
        format.set(".mp3")
        menu = OptionMenu(root, format, *options)
        menu.config(font=("Arial", 12), bg="#3E3E3E", fg="white", activebackground="#4E4E4E", activeforeground="white")
        menu.place(x=375, y=250)
        button3 = Button(root, text="EXPORT", bg='#3F51B5', fg="white", font=("Arial", 12, "bold"), command=convert, width=10, height=1)
        button3.place(x=250, y=300)

root = Tk()
root.configure(bg='#2E2E2E')
root.geometry("700x450")
root.minsize(600, 350)
root.maxsize(600, 350)
root.title("Video to Audio Converter")

style = Style()
style.configure("TButton", font=("Arial", 12), padding=5)

label1 = Label(root, text="EXTRACT AUDIO", font=("Arial", 24, "bold"), bg="#2E2E2E", fg="white")
label1.pack(pady=20)

label2 = Label(root, text="Select a Video File", font=("Arial", 16), bg="#2E2E2E", fg="white")
label2.place(x=200, y=100)

button1 = Button(root, text="BROWSE", bg='#3F51B5', fg="white", font=("Arial", 12, "bold"), command=select, width=10, height=1)
button1.place(x=250, y=200)

label3 = Label(root, font=("Arial", 16, "bold"), bg="#2E2E2E", fg="white")
label3.place(x=225, y=150)

format = StringVar()

root.mainloop()

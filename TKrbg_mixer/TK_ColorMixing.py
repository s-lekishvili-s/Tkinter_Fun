from tkinter import *
import tkinter as tk
 
root = tk.Tk()
root.title('Color mixer using tkinter')

frame = tk.Frame(root,bg='#FFFFFF',width = 300, height = 300,relief= SOLID)
 #ფერების RGB მოდელის გასამართად გამოყენებულია https://en.wikipedia.org/wiki/RGB_color_model#/media/File:AdditiveColor.svg და  https://www.csfieldguide.org.nz/en/interactives/rgb-mixer/
def Mix_Color():
    if (v1.get() == 1) & (v2.get() == 0) & (v3.get() == 0):
        frame.config(bg='#FF0000')
    elif (v1.get() == 0) & (v2.get() == 1) & (v3.get() == 0):
        frame.config(bg='#0000FF')
    elif (v1.get() == 0) & (v2.get() == 0) & (v3.get() == 1):
        frame.config(bg='#00FF00')
    elif (v1.get() == 1) & (v2.get() == 1) & (v3.get() == 0):
        frame.config(bg='#FF00FF')
    elif (v1.get() == 1) & (v2.get() == 1) & (v3.get() == 1):
        frame.config(bg='#FFFFFF')
    elif (v1.get() == 0) & (v2.get() == 1) & (v3.get() == 1):
        frame.config(bg='#00FFFF')
    elif (v1.get() == 1) & (v2.get() == 0) & (v3.get() == 1):
        frame.config(bg='#FFFF00')
    else:
        frame.config(bg='#000000')
 
v1 = tk.IntVar()
v2 = tk.IntVar()
v3 = tk.IntVar()
# 3 Checkbutton-ი
chkb1 = tk.Checkbutton(root,bg='red', text='Red',variable=v1, onvalue=1, offvalue=0, command=Mix_Color)
chkb1.pack()
chkb2 = tk.Checkbutton(root,bg= 'blue', text='Blue',variable=v2, onvalue=1, offvalue=0, command=Mix_Color)
chkb2.pack()
chkb3=tk.Checkbutton(root,bg='green', text='Green',variable=v3, onvalue=1, offvalue=0, command=Mix_Color)
chkb3.pack()
frame.pack()
 
root.mainloop()
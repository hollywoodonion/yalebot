from tkinter import *
from tkinter.ttk import *
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import tkinter as tk
import pygame
from PIL import Image, ImageTk
import webbrowser
from tkinter import messagebox
import time

##main based
toilet = Tk()

#based atribies
toilet.title("#1 most based app not on the appstore")
toilet.geometry('350x300')
lbl = Label(toilet, text="INTILIZING...", font="-weight bold", foreground="red")
lbl.grid(column=0, row=0, padx=0)


#based welcome
def welcome():
    msg_box = messagebox.askquestion("IMPORTANT LEGAL INFO", "Are you based?")    
    if msg_box == 'yes':
        lbl.configure(text="READY...", font="-weight bold", foreground="green")
    else:
        toilet.destroy()

welcome()

def OpenUrl():
    webbrowser.open_new('https://steamcommunity.com/id/9478325682/')
    play1()

#PIL image object
image = Image.open("yale.jpg")
photo = ImageTk.PhotoImage(image)
img_label = tk.Label(image=photo)
img_label.image = photo
img_label.grid(row=3, column=3)


##based toilet
pygame.init()
def play2():
    pygame.mixer.music.load("someone-broke-the-toilet.mp3") #Loading File Into Mixer
    pygame.mixer.music.play() #Playing It In The Whole Device
    ##time.sleep(1)
    ##pygame.mixer.music.load("based_intro.mp3") #Loading File Into Mixer
    ##pygame.mixer.music.play() #Playing It In The Whole Device
play2()

##based intro
pygame.init()
def play1():
    pygame.mixer.music.load("based_intro.mp3") #Loading File Into Mixer
    pygame.mixer.music.play() #Playing It In The Whole Device

play1()

btn = Button(toilet, text="YALE.EXE", command=play2)
btn.grid(column=0, row=1, padx=10)
btn2 = Button(toilet, text="YALE.COM", command=OpenUrl)
btn2.grid(column=0, row=2, padx=10)

##based
##more based
toilet.mainloop()
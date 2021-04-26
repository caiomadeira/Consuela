import tkinter as tk
from tkinter import *
from config import hex_colors
from PIL import ImageTk, Image

class SplashLoop(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.time = 2

        self.overrideredirect(True)

        self.splash_screen()
        self.splash_screen_frames()
        self.update()



    def splash_screen(self):

        self.w = self.winfo_reqwidth()
        self.h = self.winfo_reqheight()
        self.ws = self.winfo_screenwidth()
        self.hs = self.winfo_screenheight()
        self.x = (self.ws / 2) - (self.w / 2) - 200
        self.y = (self.hs / 2) - (self.h / 2) - 100

        self.title("Splash Screen  Test")
        #self.geometry("200x300")
        self.geometry("600x300"'+%d+%d' % (self.x, self.y))
        self.img = ImageTk.PhotoImage(Image.open("img/Splash_logo.png"))


    def splash_screen_frames(self):
        self.frame_splash = Frame(self)
        self.frame_splash.place(x=0, y=0, width=self.ws, height=self.hs)
        self.frame_splash.configure(background=hex_colors['COLOR_1'])
        self.panel = Label(self, image=self.img, bg=hex_colors['COLOR_1'])
        self.panel.pack(side="bottom", fill="both", expand="yes")
        self.label_credits = Label(self, text="Por Caio Madeira", bg=hex_colors['COLOR_1'],
                                   font=('helvetica', 7, 'bold'))
        self.label_credits.place(x=10, y=5, width=100, height=20)




"""

by Caio Madeira

see hexadecimal colors in: https://htmlcolorcodes.com/

bug splash screen and main solved: https://stackoverflow.com/questions/38676617/tkinter-show-splash-screen-and-hide-main-screen-until-init-has-finished


"""
import random
import time
from tkinter import *
from tkinter import ttk
import tkinter as tk

from functionalities import Functionalities
from reports import Reports_pdf
import socket
from PIL import ImageTk, Image
from config import hex_colors, custom_size
from splash_screen import SplashLoop
import ctypes

user32 = ctypes.windll.user32
screensize = f"{user32.GetSystemMetrics(0)}x{user32.GetSystemMetrics(1)}"

get_user_width = user32.GetSystemMetrics(0)
get_user_height = user32.GetSystemMetrics(1)

#splash_root = Tk()


class WindowLoop(Functionalities, Reports_pdf, tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.withdraw()
        splash = SplashLoop(self)
        #init_screen = Tk()
        #self.window = init_screen
        self.screen()
        self.screen_frames()
        self.widgets_frame_1()
        self.frame_2_list()
        self.create_tables()
        self.select_list()
        self.Menus()
        time.sleep(6)
        splash.destroy()

        ## show window again
        self.deiconify()

    def screen(self):
        w = self.winfo_reqwidth()
        print(w)
        h = self.winfo_reqheight()
        print(h)
        ws = self.winfo_screenwidth()
        print(ws)
        hs = self.winfo_screenheight()
        print(hs)
        x = (ws /2) - (w / 2) - 600
        y = (hs / 2) - (h / 2) - 300
        print(x,y)

        self.light_mode()
        self.PC_NAME = socket.gethostname()
        self.title(f"Consuela - Welcome {self.PC_NAME}")
        self.configure(background=self.BACKGROUND)
        self.geometry(f"{custom_size['init_width']}x{custom_size['init_height']}")
        self.geometry('+%d+%d' % (x, y))
        self.resizable(True, True)
        self.maxsize(width=get_user_width, height=get_user_height)
        self.minsize(width=custom_size['min_width'], height=custom_size['min_height'])
        self.iconbitmap('img/favicon.ico')
        self.img = ImageTk.PhotoImage(Image.open("img/consuela_logo_light.png"))

    def screen_frames(self):
        self.frame_1 = Frame(self)
        self.frame_1.place(relx=0.01, rely=0.01, relwidth=0.3, relheight=0.97)
        self.frame_1.configure(background=self.FRAME_1_COLOR)
        # ====================================================
        self.frame_2 = Frame(self, highlightbackground=hex_colors["BACKGROUND"], highlightthickness=1)
        self.frame_2.place(relx=0.350, rely=0.050, relwidth=0.63, relheight=0.850)
        self.frame_2.configure(background=self.FRAME_1_COLOR)

    def widgets_frame_1(self):
        # =========== BUTTON ================
        # entrar

        self.btn_enter = Button(self.frame_1, text="Salvar", fg=self.TEXT_BUTTON, bd=2, bg=self.BUTTON_COLOR,
                                font=('consolas', 12, 'bold'),
                                command=self.add_logins)
        self.btn_enter.place(relx=0.1, rely=0.830, relwidth=0.30, relheight=0.050)

        # limpar
        self.btn_clear = Button(self.frame_1, text="Limpar", bd=2, font=('consolas', 12, 'bold'),
                                command=self.clean_screen_login)
        self.btn_clear.place(relx=0.1, rely=0.900, relwidth=0.30, relheight=0.050)

        # apagar
        self.btn_erase = Button(self.frame_1, text="Apagar", bd=2, font=('consolas', 12, 'bold'),
                                command=self.delet_login)
        self.btn_erase.place(relx=0.5, rely=0.830, relwidth=0.30, relheight=0.050)

        # alterar
        self.btn_edit = Button(self.frame_1, text="Editar", bd=2, font=('consolas', 12, 'bold'),
                               command=self.edit_client)
        self.btn_edit.place(relx=0.1, rely=0.900, relwidth=0.30, relheight=0.050)

        # ========= LABELS  ============
        # self.panel = Label(self.frame_1, image=self.img)
        # self.panel.pack(side="bottom", fill="both", expand="yes")
        # self.panel.place(relx=0.25, rely=0.1, width=200, height=190)

        self.label_credits = Label(self.frame_1, text="Por Caio Madeira", bg=self.FRAME_1_COLOR,
                                   font=('helvetica', 7, 'bold'))
        self.label_credits.place(x=10, y=5, width=100, height=20)

        self.label_account = Label(self.frame_1, text="Conta:", bg=self.FRAME_1_COLOR, font=('consolas', 15, 'bold'))
        self.label_account.place(relx=0.01, rely=0.40, relwidth=0.45, relheight=0.05)

        self.label_user = Label(self.frame_1, text="Usuário/E-mail:", bg=self.FRAME_1_COLOR,
                                font=('consolas', 12, 'bold'))
        self.label_user.place(relx=0.10, rely=0.50, relwidth=0.45, relheight=0.05)

        self.label_pass = Label(self.frame_1, text="Senha:", bg=self.FRAME_1_COLOR, font=('consolas', 15, 'bold'))
        self.label_pass.place(relx=0.01, rely=0.60, relwidth=0.45, relheight=0.05)
        # ========= ENTRYS  ============

        self.entry_account = Entry(self.frame_1, font=('consolas', 12, 'bold'))
        self.entry_account.place(relx=0.15, rely=0.45, relwidth=0.60, relheight=0.05)

        self.entry_user = Entry(self.frame_1, font=('consolas', 12, 'bold'))
        self.entry_user.place(relx=0.15, rely=0.55, relwidth=0.60, relheight=0.05)

        self.entry_pass = Entry(self.frame_1, font=('consolas', 12, 'bold'))
        self.entry_pass.place(relx=0.15, rely=0.65, relwidth=0.60, relheight=0.05)

    def frame_2_list(self):
        self.list_logins = ttk.Treeview(self.frame_2, height=3, column=("col2", "col3", "col4"))
        self.list_logins.heading("#0", text="")
        self.list_logins.heading("#1", text="Conta")
        self.list_logins.heading("#2", text="Usuário")
        self.list_logins.heading("#3", text="Senha")

        self.list_logins.column("#0", width=1)
        self.list_logins.column("#1", width=100)
        self.list_logins.column("#2", width=150)
        self.list_logins.column("#3", width=150)

        self.list_logins.place(relx=0.02, rely=0.1, relwidth=0.96, relheight=0.850)

        # === BARRA DE ROLAGEM
        self.scroollList = Scrollbar(self.frame_2, orient='vertical')
        self.list_logins.configure(yscroll=self.scroollList.set)
        self.scroollList.place(relx=0.96, rely=0.1, relwidth=0.02, relheight=0.850)
        self.list_logins.bind("<Double-1>", self.OnDoubleClick)

        # ==== BOTAO BUSCAR

        self.btn_search = Button(self.frame_2, text="Buscar", bd=2, font=('consolas', 12, 'bold'),
                                 command=self.search_logins)
        self.btn_search.place(relx=0.01, rely=0.01, relwidth=0.1, relheight=0.050)

        self.entry_search = Entry(self.frame_2, font=('consolas', 12, 'bold'))
        self.entry_search.place(relx=0.3, rely=0.01, relwidth=0.60, relheight=0.05)

    def Menus(self):
        menu_bar = Menu(self)
        self.config(menu=menu_bar)
        menu_file_sair = Menu(menu_bar)
        # menu_file_limpar = Menu(menu_bar)
        menu_file_sobre = Menu(menu_bar)
        menu_file_reports = Menu(menu_bar)
        menu_file_dark_mode = Menu(menu_bar)

        def Quit(): self.destroy()

        menu_bar.add_cascade(label="Sobre", menu=menu_file_sobre)
        menu_bar.add_cascade(label="Exportar para...", menu=menu_file_reports)
        menu_bar.add_cascade(label="Opções", menu=menu_file_sair)
        menu_bar.add_cascade(label="Mais", menu=menu_file_dark_mode)

        menu_file_sair.add_command(label="Sair", command=Quit)
        # menu_file_limpar.add_command(label="Limpar a Tela", command=self.clean_screen_login)
        menu_file_reports.add_command(label="PDF", command=self.generateReport)
        menu_file_dark_mode.add_command(label="Modo Escuro", command=self.dark_mode)


if __name__ == '__main__':
    mainWindow = WindowLoop()
    mainWindow.mainloop()

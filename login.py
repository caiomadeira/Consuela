from tkinter import *
import tkinter as tk
from login_dao import LoginDAO
import socket
from PIL import ImageTk, Image
from config import hex_colors, custom_size
from app import WindowLoop
import ctypes, time
from splash_screen import SplashLoop

user32 = ctypes.windll.user32
screensize = f"{user32.GetSystemMetrics(0)}x{user32.GetSystemMetrics(1)}"

get_user_width = user32.GetSystemMetrics(0)
get_user_height = user32.GetSystemMetrics(1)


class LoginConsuela(LoginDAO, WindowLoop):

    def __init__(self):
        tk.Tk.__init__(self)
        self.withdraw()
        splash = SplashLoop(self)

        self.login_screen()
        self.login_screen_frames()
        self.login_widgets_frames()
        self.createTables()

        time.sleep(6)
        splash.destroy()

        ## show window again
        self.deiconify()


    def login_screen(self):
        w = self.winfo_reqwidth()
        print(w)
        h = self.winfo_reqheight()
        print(h)
        ws = self.winfo_screenwidth()
        print(ws)
        hs = self.winfo_screenheight()
        print(hs)
        x = (ws / 2) - (w / 2) - 600
        y = (hs / 2) - (h / 2) - 300
        print(x, y)
        # BUTTON SWITCH DARK OR LIGHT
        self.light_mode()
        self.PC_NAME = socket.gethostname()
        self.title("Consuela - Login")
        self.geometry(f"{custom_size['init_width']}x{custom_size['init_height']}")
        self.geometry('+%d+%d' % (x, y))
        self.resizable(True, True)
        self.maxsize(width=get_user_width, height=get_user_height)
        self.minsize(width=custom_size['min_width'], height=custom_size['min_height'])
        self.iconbitmap('img/favicon.ico')
        self.img = ImageTk.PhotoImage(Image.open("img/consuela_logo_light.png"))

    def login_screen_frames(self):
        self.frame_1 = Frame(self)
        self.frame_1.place(relx=0.01, rely=0.01, relwidth=0.3, relheight=0.97)
        self.frame_1.configure(background=self.FRAME_1_COLOR)
        # ====================================================
        self.frame_2 = Frame(self, highlightbackground=hex_colors["BACKGROUND"])
        self.frame_2.place(relx=0.350, rely=0.050, relwidth=0.63, relheight=0.850)


    def login_widgets_frames(self):
        # ========= BUTTONS  ============
        # ENTER
        self.btn_enter = Button(self.frame_1, text="Entrar", fg=self.TEXT_BUTTON, bd=2, bg=self.BUTTON_COLOR,
                                font=('consolas', 12, 'bold'), command=WindowLoop)
        self.btn_enter.place(relx=0.1, rely=0.830, relwidth=0.30, relheight=0.050)

        # REGISTER
        self.btn_edit = Button(self.frame_1, text="Cadastrar", fg=self.TEXT_BUTTON, bg=self.BUTTON_COLOR, bd=2,
                               font=('consolas', 12, 'bold'), command=self.register_consuela)
        self.btn_edit.place(relx=0.5, rely=0.830, relwidth=0.30, relheight=0.050)

        # ========= LABELS  ============

        # CONSUELA LOGO LOGIN SCREEN
        self.panel = Label(self.frame_1, image=self.img)
        self.panel.pack(side="bottom", fill="both", expand="yes")
        self.panel.place(relx=0.25, rely=0.1, width=197, height=190)
        # ------------------------------

        self.label_user = Label(self.frame_1, text="Usuário:", bg=self.FRAME_1_COLOR, fg=self.LABEL_COLOR_TEXT,
                                font=('consolas', 15, 'bold'))
        self.label_user.place(relx=0.04, rely=0.50, relwidth=0.45, relheight=0.05)

        self.label_pass = Label(self.frame_1, text="Senha:", bg=self.FRAME_1_COLOR, fg=self.LABEL_COLOR_TEXT,
                                font=('consolas', 15, 'bold'))
        self.label_pass.place(relx=0.01, rely=0.60, relwidth=0.45, relheight=0.05)
        # ========= ENTRYS  ============

        self.entry_user = Entry(self.frame_1, font=('consolas', 12, 'bold'))
        self.entry_user.place(relx=0.15, rely=0.55, relwidth=0.60, relheight=0.05)

        self.entry_pass = Entry(self.frame_1, font=('consolas', 12, 'bold'))
        self.entry_pass.place(relx=0.15, rely=0.65, relwidth=0.60, relheight=0.05)
        self.entry_pass.config(show="*")


    def register_consuela(self):



        # ========= BUTTONS  ============
        self.btn_register = Button(self.frame_1, text="Registrar", fg=self.TEXT_BUTTON, bd=2, bg=self.BUTTON_COLOR,
                                   font=('consolas', 12, 'bold'), command=self.createTables)
        self.btn_register.place(relx=0.1, rely=0.830, relwidth=0.30, relheight=0.050)

        # BACK TO LOGIN SCREEN
        self.btn_back_to_login = Button(self.frame_1, text="Voltar", fg=self.TEXT_BUTTON, bg=self.BUTTON_COLOR, bd=2,
                                        font=('consolas', 12, 'bold'))

        self.btn_back_to_login.place(relx=0.5, rely=0.830, relwidth=0.30, relheight=0.050)

        # ========= LABELS  ============

        self.label_name = Label(self.frame_1, text="Digite um nome:", bg=self.FRAME_1_COLOR, fg=self.LABEL_COLOR_TEXT,
                                font=('consolas', 15, 'bold'))
        self.label_name.place(relx=0.15, rely=0.40, relwidth=0.45, relheight=0.05)

        self.label_user = Label(self.frame_1, text="Digite um usuário:", bg=self.FRAME_1_COLOR, fg=self.LABEL_COLOR_TEXT,
                                font=('consolas', 15, 'bold'))
        self.label_user.place(relx=0.11, rely=0.50, relwidth=0.60, relheight=0.05)

        self.label_pass = Label(self.frame_1, text="Digite uma senha:", bg=self.FRAME_1_COLOR, fg=self.LABEL_COLOR_TEXT,
                                font=('consolas', 15, 'bold'))
        self.label_pass.place(relx=0.10, rely=0.60, relwidth=0.60, relheight=0.05)


        # ========= ENTRYS  ============
        self.entry_name = Entry(self.frame_1, font=('consolas', 12, 'bold'))
        self.entry_name.place(relx=0.15, rely=0.45, relwidth=0.60, relheight=0.05)

        self.entry_user = Entry(self.frame_1, font=('consolas', 12, 'bold'))
        self.entry_user.place(relx=0.15, rely=0.55, relwidth=0.60, relheight=0.05)

        self.entry_pass = Entry(self.frame_1, font=('consolas', 12, 'bold'))
        self.entry_pass.place(relx=0.15, rely=0.65, relwidth=0.60, relheight=0.05)


from config import hex_colors
import sqlite3

class LoginDAO():

    def light_mode(self):
        print("LIGHT MODE")
        self.BACKGROUND = hex_colors['BACKGROUND']
        self.BUTTON_COLOR = hex_colors['BUTTON_1']
        self.FRAME_1_COLOR = hex_colors['COLOR_1']
        self.TEXT_BUTTON = hex_colors['TEXT_BUTTON_LIGHT']
        self.LABEL_COLOR_TEXT = hex_colors['LABEL_TEXT_COLOR_LIGHT']

    def connect_db(self):
        print("CONECTANDO ao banco de dados de logins - login_consu.db")
        self.conn = sqlite3.connect("db/login_consu.db")
        self.cursor = self.conn.cursor()

    def disconnect_db(self):
        print("DESCONECTANDO ao banco de dados de logins - login_consu.db")
        self.conn.close()

    def createTables(self):
        self.connect_db()


        # CRIANDO TABELA
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users_consuela (
                cod INTEGER PRIMARY KEY,
                user_name CHAR(40) NOT NULL,
                user_consuela CHAR(40) NOT NULL,
                pass_consuela CHAR(40) NOT NULL
                 
            );
        """)
        self.conn.commit()
        self.disconnect_db()

    def add_user_consuela(self):
        self.username_consuela = self.entry_name.get()
        self.user_consuela = self.entry_user.get()
        self.password_consuela = self.entry_pass.get()
        self.connect_db()

        self.cursor.execute(""" INSERT INTO users_consuela (user_consuela, pass_consuela) 
            VALUES (?, ?)""", (self.user_consuela, self.password_consuela))
        self.conn.commit()
        self.disconnect_db()
        print("Usuario registrado com sucesso")

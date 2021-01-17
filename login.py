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


class LoginConsuela():

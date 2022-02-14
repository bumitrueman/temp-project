import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
from PIL import ImageTk


WIDTH = 500
HEIGHT = 300
APP_NAME = 'My App'
DIM = str(WIDTH) + str('x') + str(HEIGHT)

win = tk.Tk()
win.title(APP_NAME)
win.geometry(DIM)

img_captcha = ImageTk.PhotoImage(file='img/captcha.png')
img_reload = ImageTk.PhotoImage(file='img/reload.png')

PATH = r'driver\chromedriver97.exe'
URL = r'https://dpskolkata.net/'

DRIVER = webdriver.Chrome(PATH)
# DRIVER = webdriver.Chrome(PATH, chrome_options=options)
DRIVER.get(URL)

USERNAME = ''
PASSWORD = ''

SCREEN = tk.StringVar(win, 'Login')


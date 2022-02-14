from frame_main import *


win_login = tk.Frame(win)


def update_captcha():
    global img_captcha
    img = DRIVER.find_element(By.ID, "ContentPlaceHolder1_imgCaptcha")
    img.screenshot('img/captcha.png')
    img_captcha = ImageTk.PhotoImage(file='img/captcha.png')
    w_lg_img_captcha.config(image=img_captcha)


def login():
    username = DRIVER.find_element(By.ID, 'ContentPlaceHolder1_txtusername')
    username.clear()

    password = DRIVER.find_element(By.ID, 'ContentPlaceHolder1_txtpwd')
    password.clear()

    captcha = DRIVER.find_element(By.ID, 'ContentPlaceHolder1_txtCaptcha')
    captcha.clear()

    username.send_keys(w_lg_username.get())
    password.send_keys(w_lg_password.get())
    captcha.send_keys(w_lg_entry_captcha.get())

    DRIVER.find_element(By.ID, 'ContentPlaceHolder1_btnLogin').click()
    
    check_login()


def check_login():
    try:
        error = DRIVER.find_element(By.ID, 'ContentPlaceHolder1_lblerr').text
    except:
        error = ''

    if len(error) != 0:
        messagebox.showwarning("Error", error)
        update_captcha()
    else:
        SCREEN.set('Logged IN')
        DRIVER.get('https://dpskolkata.net/students/ClassSchedule.aspx')


w_lg_username = tk.StringVar(win_login, '')
w_lg_password = tk.StringVar(win_login, '')

w_lg_username.set(USERNAME)
w_lg_password.set(PASSWORD)

Y = 20
tk.Label(win_login, text='Username:', width=8, anchor='e').place(x=0, y=Y)
tk.Entry(win_login, textvariable=w_lg_username).place(x=70, y=20)

Y = 50
tk.Label(win_login, text='Password:', width=8, anchor='e').place(x=0, y=Y)
tk.Entry(win_login, textvariable=w_lg_password, show="*").place(x=70, y=Y)

Y = 80
w_lg_img_captcha = tk.Label(win_login, image=img_captcha)
w_lg_img_captcha.place(x=50, y=Y)
tk.Button(win_login, image=img_reload, command=update_captcha).place(x=170, y=Y, height=35)

Y = 125
tk.Label(win_login, text='Captcha:', width=8, anchor='e').place(x=0, y=Y)
w_lg_entry_captcha = tk.Entry(win_login)
w_lg_entry_captcha.place(x=70, y=Y)

Y = 155
tk.Button(win_login, text='Login', width=10, command=login).place(x=70, y=Y)

# w_lg_text_display = tk.Text(win_login, width=20, height=10).grid(row=0, column=2, rowspan=3)

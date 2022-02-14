from frame_main import *
from frame_login import *
from frame_recent import *


def update_frame(var=0, index=0, mode=0):    
    global win_login, win_recent

    if SCREEN.get() == 'Login':
        update_captcha()
        win_login.place(x=5, y=0, height=HEIGHT, width=200)
        win_recent.place(x=210, y=0, height=HEIGHT, width=290)
    else:
        win_login.place_forget()
        win_recent.place_forget()

    if SCREEN.get() == 'Logged IN':
        tk.Label(win, text='hey').pack()
    else:
        pass


update_frame()

SCREEN.trace("w", update_frame)

win.mainloop()

DRIVER.quit()

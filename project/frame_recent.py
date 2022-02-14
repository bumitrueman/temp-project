from frame_main import *

win_recent = tk.Frame(win)

string_sub = tk.StringVar(win_recent, "COMPUTER SCIENCE - (11-12)")
string_teacher = tk.StringVar(win_recent, "SUDARSHAN KUMAR MANNA")
string_time = tk.StringVar(win_recent, "07/02/2022 11:00 AM")
string_id = tk.StringVar(win_recent, "765 xxxx 6881")
string_pass = tk.StringVar(win_recent, "somepassword")

Y = 20
tk.Label(win_recent, text='Upcoming Class').place(x=0, y=Y)

Y = 50
#upcoming_class 
tk.Label(win_recent, text='Subject:').place(x=0, y=Y)
uc_sub = tk.Label(win_recent, textvariable=string_sub, anchor='w')
uc_sub.place(x=70, y=Y)

Y = 70
tk.Label(win_recent, text='Teacher:').place(x=0, y=Y)
uc_teacher = tk.Label(win_recent, textvariable=string_teacher, anchor='w')
uc_teacher.place(x=70, y=Y)

Y = 90
tk.Label(win_recent, text='Time:').place(x=0, y=Y)
uc_time = tk.Label(win_recent, textvariable=string_time, anchor='w')
uc_time.place(x=70, y=Y)

Y = 110
tk.Label(win_recent, text='Meeting ID:').place(x=0, y=Y)
uc_id = tk.Label(win_recent, textvariable=string_id, anchor='w')
uc_id.place(x=70, y=Y)

Y = 130
tk.Label(win_recent, text='Password:').place(x=0, y=Y)
uc_pass = tk.Label(win_recent, textvariable=string_pass, anchor='w')
uc_pass.place(x=70, y=Y)
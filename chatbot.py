from tkinter import *
import socket, pickle

s = socket.socket()
host = '127.0.0.1'
port = 9000
s.connect((host, port))

def Printname(event):
    username = entry1.get()
    password = entry2.get()
    print(username,password)
    s.send(pickle.dumps([username,password]))
    s.close()


# print(s.recv(1024))
# s.close()    
var = Tk()
name = Label(var, text = "name")
password = Label(var, text = "password")
entry1 = Entry(var)
entry2 = Entry(var, show="*")
name.grid(row=0, sticky = E)
password.grid(row=1, sticky = E)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
c = Checkbutton(var, text = "keep me logged in")
c.grid(row=2, columnspan=2)
top_frame = Frame(var)
top_frame.grid(row=3, columnspan=2)
button_1 = Button(top_frame, text = "Login", fg = "yellow", bg = "black")
button_1.bind("<Button-1>", Printname)
button_2 = Button(top_frame, text = "Reset")
button_1.pack(side = LEFT)
button_2.pack(side = LEFT)
var.mainloop()

# import tkinter as ck
# m= ck.Tk()
# m.geometry('600x400')
# m.title("counting seconds")
# # label1=ck.label(m,text="user name")
# # txt=ck.entry(m)
# # label1.grid(row=0,coloumn=0)
# button = ck.Button(m, text="stop")
# button.pack()

# m.mainloop()

from tkinter import *

gui = Tk(className='Python Examples - Button')
gui.geometry("500x200")

# create button
button = Button(gui, text='My Button', width=40, height=3, bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa')
# add button to gui window
button.pack()

gui.mainloop()

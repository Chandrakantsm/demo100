import tkinter as ck
m= ck.Tk()
m.geometry('600x400')
m.title("counting seconds")
# label1=ck.label(m,text="user name")
# txt=ck.entry(m)
# label1.grid(row=0,coloumn=0)
button = ck.Button(m, text="stop")
button.pack()

m.mainloop()

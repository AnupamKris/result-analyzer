


from tkinter import *
import sqlite3 as p
from prettytable import PrettyTable

win = Tk()
win.title("MySql Connector")
win.configure(background='#2D3140')


db = p.connect('my_db.db')
c = db.cursor()
t = Text(win,bg = '#2D3140',fg = 'white',width = 490,height = 50)
# t.grid(row=1,column = 1,rowspan = 9,columnspan = 13)
t.pack()
t.insert(END,'Welcome To SQL connector v 1.2')
e = Entry(win,width = 100,bg = '#2D3140',fg = 'white',border = 0,justify = CENTER)
# e.grid(row = 10, column = 1,columnspan = 12)
e.pack()

def ex(querry):
    if querry[0] == "#":
        exec(querry[1:])
    else:
        try:
            c.execute(querry)
        except:
            return 'You have an Error in the sql syntax'
        v = c.fetchall()
        try:
            return spacing(v)
        except:
            return (str(v)) 
        

def spacing(t):
    x = PrettyTable()
    x.field_names = [i[0] for i in c.description]
    for i in t:
        exec("x.add_row({})".format(i))   
    return(str(x))



def sub(x=0):
    global e
    global t
    f = e.get()
    t.insert(END,'\n>>>'+f)
    t.insert(END,'\n'+ex(f))
    t.yview(END)
    
    e.delete(0,END)
# b = Button(win,text = 'GO!',command = sub)
win.bind('<Return>',sub)
# b.grid(row=10,column=13)
win.mainloop()

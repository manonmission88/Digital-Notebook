
from tkinter import *
import tkinter as tk
import backend

def get_selected_row(event):
    global selected_row
    index = list.curselection()[0]
    selected_row = list.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_row[1])
    e2.delete(0,END)
    e2.insert(END,selected_row[2])
    e3.delete(0,END)
    e3.insert(END,selected_row[3])
    e4.delete(0,END)
    e4.insert(END,selected_row[4])
    e5.delete(0,END)
    e5.insert(END,selected_row[5])
    e6.delete(0,END)
    e6.insert(END,selected_row[6])

def delete_command():
    backend.delete(selected_row[0])

def view_command():
    list.delete(0,END)
    for row in backend.view():
        list.insert(END,row)

def search_command():
    list.delete(0,END)
    for row in backend.search(date_text.get(),professor_text.get(),course_text.get(),assignment_text.get(),deadline_text.get(),remarks_text.get()):
        list.insert(END,row)

def add_command():
    backend.insert(date_text.get(),professor_text.get(),course_text.get(),assignment_text.get(),deadline_text.get(),remarks_text.get())

    list.delete(0,END)
    list.insert(END,(date_text.get(),professor_text.get(),course_text.get(),assignment_text.get(),deadline_text.get(),remarks_text.get()))

win = Tk()

win.wm_title('DIGITAL NOTEBOOK -COLLEGE')
win.configure(background='light blue')
# win.iconphoto(False, tk.PhotoImage(file='/Users/manishnewray/Downloads/python--project/IconScout-1.0.3.png'))
win.geometry('790x400')
b1 = Button(win, text='Date',width=12,pady=5)
b1.grid(row=0,column=0)
b2 = Button(win, text='Professor',width=12,pady=5)
b2.grid(row=0,column=2)
b3 = Button(win, text='Course',width=12,pady=5)
b3.grid(row=1,column=0)
b4 = Button(win, text='Assignment',width=12,pady=5)
b4.grid(row=1,column=2)
b5 = Button(win, text='Deadline',width=12,pady=5)
b5.grid(row=2,column=0)
b6 = Button(win, text='Remarks',width=12,pady=5)
b6.grid(row=2,column=2)

date_text = StringVar()
e1 = Entry(win, textvariable=date_text)
e1.grid(row=0,column=1)

professor_text = StringVar()
e2 = Entry(win, textvariable=professor_text)
e2.grid(row=0,column=3)

course_text = StringVar()
e3 = Entry(win, textvariable=course_text)
e3.grid(row=1,column=1)

assignment_text = StringVar()
e4 = Entry(win, textvariable=assignment_text)
e4.grid(row=1,column=3)

deadline_text = StringVar()
e5 = Entry(win, textvariable=deadline_text)
e5.grid(row=2,column=1)

remarks_text = StringVar()
e6 = Entry(win, textvariable=remarks_text)
e6.grid(row=2,column=3)

#just above the text-box
info=Label(win,text='THINGS TO KEEP TRACK',bd=1,width=30)
info.grid(row=4,column=1)

list = Listbox(win,height=12,width=50)
list.grid(row=5,column=0,rowspan=10,columnspan=3)
# list.place(relx=0.4, rely=0.5, anchor='n')

sb = Scrollbar(win)
sb.grid(row=3,column=3,rowspan=9)

list.bind('<<ListboxSelect>>',get_selected_row)

b7 = Button(win,text='ADD',width=12,pady=5,command=add_command)
b7.grid(row=5,column=3)

b8 = Button(win,text='Search',width=12,pady=5,command=search_command)
b8.grid(row=6,column=3)

b9= Button(win,text='Delete date',width=12,pady=5,command=delete_command)
b9.grid(row=7,column=3)

b10 = Button(win,text='View all',width=12,pady=5,command=view_command)
b10.grid(row=8,column=3)

b11 = Button(win,text='Close',width=12,pady=5,command = win.destroy)
b11.grid(row=9,column=3)

win.mainloop()

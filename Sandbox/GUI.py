__author__ = 'Raphael'

# from tkinter import *
# import tkinter as tk
# import tkinter.font as tkfont
#
# master = Tk()
#
# font36 = tkfont.Font(size=24)
#
# frame1 = Frame(master, width=300, height=210)
# frame1.grid(row=0, column=0)
#
# frame2 = Frame(master, width=300, height=80)
# frame2.grid(row=1, column=0, sticky=tk.N+tk.E+tk.S+tk.W)
# frame2["bg"]="red"
#
# frame3 = Frame(master, width=80, height=290)
# frame3.grid(row=0, column=1, rowspan=2)
# frame3["bg"]="green"
#
# b1 = Button(frame1, text="Forward", font=font36)
# b1.grid(row=0, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
# # b1[font]
#
# b2 = Button(frame1, text="Left", font=font36)
# b2.grid(row=1, column=0, sticky=tk.N+tk.E+tk.S+tk.W)
#
# b3 = Button(frame1, text="Right", font=font36)
# b3.grid(row=1, column=2, sticky=tk.N+tk.E+tk.S+tk.W)
#
# b4 = Button(frame1, text="Backward", font=font36)
# b4.grid(row=2, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
#
# # frame1.grid_propagate(0)
# # frame2.grid_propagate(0)
# # frame3.grid_propagate(0)
#
# frame1.rowconfigure(0,minsize=70)
# frame1.rowconfigure(1,minsize=70)
# frame1.rowconfigure(2,minsize=70)
#
# frame1.columnconfigure(0,minsize=100)
# frame1.columnconfigure(1,minsize=100)
# frame1.columnconfigure(2,minsize=100)
#
# mainloop()

# import tkinter as tk
#
# root = tk.Tk()
# def myfunction(*event):
#     x=var.get()
#     y=entry1.get()
#     z=entry2.get()
#     print(len(x),":",len(y),":",len(z))
#     if len(y)>0 and len(x)>0 and len(z)>0:
#         button.config(state='normal')
#     else:
#         button.config(state='disabled')
# entry1=tk.Entry(root,width=15)
# entry1.grid(row=1,column=1)
# entry2=tk.Entry(root,width=15)
# entry2.grid(row=1,column=2)
#
# choices=('a','b','c')
# var=tk.StringVar(root)
# option=tk.OptionMenu(root,var,*choices)
# option.grid(row=1,column=3)
#
# button=tk.Button(root,text="submit")
# button.grid(row=1,column=4)
# button.config(state='disabled')
#
# root.bind_class("Entry","<FocusOut>",myfunction)
# var.trace('w', myfunction)
# root.mainloop()

from tkinter import *

def test():
    print(tiltscale.get(), panscale.get(), tiltscale.get()+panscale.get())

def reset():
    panscale.set(0)
    tiltscale.set(0)

def updatetilt(event):
    print("Tilt :", tiltscale.get())

def updatepan(event):
    print("Pan :", panscale.get())

def fctEventButton1(event):
    print("Button1 event")

def fctEventButtonPressed1(event):
    print("ButtonPressed1 event")

def fctEventButtonReleased1(event):
    print("ButtonReleased1 event")

master = Tk()

tiltscale = Scale(master, from_=90, to=-15, label="Tilt", sliderlength=20, length=150, command=updatetilt)
tiltscale.grid(row=0, column=0)

panscale = Scale(master, from_=-90, to=90, orient=HORIZONTAL, label="Pan", sliderlength=20, length=150)
panscale.grid(row=1, column=0)

panscale.bind("<ButtonRelease-1>", updatepan)

buttontest = Button(master, text="TEST", command=test)
buttontest.grid(row=2, column=0)

buttonreset = Button(master, text="RESET", command=reset)
buttonreset.grid(row=3, column=0)

buttonevent = Button(master, text="EVENT")
buttonevent.grid(row=4, column=0)

# buttonevent.bind("<Button-1>", fctEventButton1)
buttonevent.bind("<ButtonPress-1>", fctEventButtonPressed1)
buttonevent.bind("<ButtonRelease-1>", fctEventButtonReleased1)
master.mainloop()
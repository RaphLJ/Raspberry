__author__ = 'Raphael'

from tkinter import *
import tkinter as tk
import tkinter.font as tkfont

master = Tk()

font36 = tkfont.Font(size=24)

frame1 = Frame(master, width=300, height=210)
frame1.grid(row=0, column=0)

frame2 = Frame(master, width=300, height=80)
frame2.grid(row=1, column=0, sticky=tk.N+tk.E+tk.S+tk.W)
frame2["bg"]="red"

frame3 = Frame(master, width=80, height=290)
frame3.grid(row=0, column=1, rowspan=2)
frame3["bg"]="green"

b1 = Button(frame1, text="Forward", font=font36)
b1.grid(row=0, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
# b1[font]

b2 = Button(frame1, text="Left", font=font36)
b2.grid(row=1, column=0, sticky=tk.N+tk.E+tk.S+tk.W)

b3 = Button(frame1, text="Right", font=font36)
b3.grid(row=1, column=2, sticky=tk.N+tk.E+tk.S+tk.W)

b4 = Button(frame1, text="Backward", font=font36)
b4.grid(row=2, column=1, sticky=tk.N+tk.E+tk.S+tk.W)

# frame1.grid_propagate(0)
# frame2.grid_propagate(0)
# frame3.grid_propagate(0)

frame1.rowconfigure(0,minsize=70)
frame1.rowconfigure(1,minsize=70)
frame1.rowconfigure(2,minsize=70)

frame1.columnconfigure(0,minsize=100)
frame1.columnconfigure(1,minsize=100)
frame1.columnconfigure(2,minsize=100)

mainloop()
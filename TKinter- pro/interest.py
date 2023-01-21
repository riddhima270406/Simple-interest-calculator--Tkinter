from tkinter import *

window = Tk()

window.title("SIMPLE INTEREST")
window.geometry("500x500")
window.configure(bg="#2f302e")

title = Label(window, text="SIMPLE INTEREST \n CALCULATOR", font=('MS Sans Serif', 23), foreground="lightgreen", bg="#2f302e")
title.place(x=110, y=30)

principle_l = Label(window, text="Principle: ", font=('MS Sans Serif', 15), foreground="#bbbec3", bg='#2f302e')
principle_l.place(x=60, y=150)

principle = Entry(window, width=25, font=('MS Sans Serif', 15), foreground="#bbbec3", bg="#2f302e")
principle.place(x=155, y=150)

interest_l = Label(window, text="Interest Rate: ", font=('MS Sans Serif', 15), foreground="#bbbec3", bg='#2f302e')
interest_l.place(x=60, y=210)

interest = Entry(window, width=22, font=('MS Sans Serif', 15), foreground="#bbbec3", bg="#2f302e")
interest.place(x=190, y=210)

time_l = Label(window, text="Time: ", font=('MS Sans Serif', 15), foreground="#bbbec3", bg='#2f302e')
time_l.place(x=60, y=270)

time = Entry(window, width=28, font=('MS Sans Serif', 15), foreground="#bbbec3", bg="#2f302e")
time.place(x=125, y=270)

def cal():
    p = int(principle.get())
    i = int(interest.get())
    t = int(time.get())
    si = (p*i*t)/100
    result.destroy()
    output = Label(result_f, text= si, bg="#2f302e", font=('MS Sans Serif', 15), width=30)
    output.place(x=4, y=3)
    output.pack()

calculate = Button(window, text='CALCULATE', font=('MS Sans Serif', 13), foreground='green', bg='lightblue', command=cal)
calculate.place(x=200, y=340)

result_f = LabelFrame(window, text="RESULTS", bg='#2f302e', font=('MS Sans Serif', 10), foreground="orange")
result_f.pack(padx=20, pady=20)
result_f.place(x=60, y=390)

result = Label(result_f, text='', bg='#2f302e', font=('MS Sans Serif', 15), width=30)
result.place(x=4, y=3)
result.pack()

window.mainloop()
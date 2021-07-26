from tkinter import *

cal_window = Tk()
cal_window.geometry("700x700")
cal_window.title("Calculator")
cal_window.configure(bg="gray")
cal_window.anchor(CENTER)

entry1 = Entry(cal_window)
entry1.grid(columnspan=4, ipadx=130, ipady=20, padx=10, pady=30)

btn1 = Button(cal_window, width="10", height="3", text="7")
btn1.grid(row=1, column=0)

btn2 = Button(cal_window, width="10", height="3", text="8")
btn2.grid(row=1, column=1)

btn3 = Button(cal_window, width="10", height="3", text="9")
btn3.grid(row=1, column=2)

btnplus = Button(cal_window, width="10", height="3", text="+")
btnplus.grid(row=1, column=3)

btn4 = Button(cal_window, width="10", height="3", text="4")
btn4.grid(row=2, column=0, pady=10)

btn5 = Button(cal_window, width="10", height="3", text="5")
btn5.grid(row=2, column=1)

btn6 = Button(cal_window, width="10", height="3", text="6")
btn6.grid(row=2, column=2)

btnminus = Button(cal_window, width="10", height="3", text="-")
btnminus.grid(row=2, column=3)


btn1 = Button(cal_window, width="10", height="3", text="1")
btn1.grid(row=3, column=0, pady=10)

btn2 = Button(cal_window, width="10", height="3", text="2")
btn2.grid(row=3, column=1)

btn3 = Button(cal_window, width="10", height="3", text="3")
btn3.grid(row=3, column=2)

btninto = Button(cal_window, width="10", height="3", text="x")
btninto.grid(row=3, column=3)


btn0 = Button(cal_window, width="10", height="3", text="0")
btn0.grid(row=4, column=0, pady=10)

btnclear = Button(cal_window, width="10", height="3", text="Clear")
btnclear.grid(row=4, column=1)

btnequal = Button(cal_window, width="10", height="3", text="=")
btnequal.grid(row=4, column=2)

btninto = Button(cal_window, width="10", height="3", text="/")
btninto.grid(row=4, column=3)

cal_window.mainloop()

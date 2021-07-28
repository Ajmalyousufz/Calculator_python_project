from tkinter import *

cal_window = Tk()
cal_window.geometry("700x700")
cal_window.title("Calculator")
cal_window.configure(bg="gray")
cal_window.anchor(CENTER)

value = ""
temp = 0


def display(num):
    global temp
    global value
    global appval

    if temp == 1:

        value = ""
        value = value + str(num)
        equation.set(value)
        temp = 0

    else:

        value = value + str(num)
        equation.set(value)


def equalpress():
    global value
    global temp
    global appval
    temp = 1
    try:
        total = str(eval(value))
        equation.set(total)
        value = str(total)
    except:
        equation.set("Error")
        value = ""


def clear():
    global value
    value = ""
    entry1.delete(0, END)


def oper():
    global temp
    temp = 0

def backspace():
    global value
    entry1.delete(len(value)-1)
    value = entry1.get()


equation = StringVar()
entry1 = Entry(cal_window, textvariable=equation)
entry1.grid(columnspan=4, ipadx=130, ipady=20, padx=10, pady=30)

btn7 = Button(cal_window, command=lambda: display("7"), width="10", height="3", text="7")
btn7.grid(row=1, column=0, pady=10)

btn8 = Button(cal_window, command=lambda: display("8"), width="10", height="3", text="8")
btn8.grid(row=1, column=1)

btn9 = Button(cal_window, command=lambda: display("9"), width="10", height="3", text="9")
btn9.grid(row=1, column=2)

btnplus = Button(cal_window, command=lambda: [oper(), display(" + ")], width="10", height="3", text="+")
btnplus.grid(row=1, column=3)

btn4 = Button(cal_window, command=lambda: display("4"), width="10", height="3", text="4")
btn4.grid(row=2, column=0, pady=10)

btn5 = Button(cal_window, command=lambda: display("5"), width="10", height="3", text="5")
btn5.grid(row=2, column=1)

btn6 = Button(cal_window, command=lambda: display("6"), width="10", height="3", text="6")
btn6.grid(row=2, column=2)

btnminus = Button(cal_window, command=lambda: [oper(), display(" - ")], width="10", height="3", text="-")
btnminus.grid(row=2, column=3)

btn1 = Button(cal_window, command=lambda: display("1"), width="10", height="3", text="1")
btn1.grid(row=3, column=0, pady=10)

btn2 = Button(cal_window, command=lambda: display("2"), width="10", height="3", text="2")
btn2.grid(row=3, column=1)

btn3 = Button(cal_window, command=lambda: display("3"), width="10", height="3", text="3")
btn3.grid(row=3, column=2)

btninto = Button(cal_window, command=lambda: [oper(), display(" * ")], width="10", height="3", text="x")
btninto.grid(row=3, column=3)

btn0 = Button(cal_window, command=lambda: display("0"), width="10", height="3", text="0")
btn0.grid(row=4, column=0, pady=10)

btnclear = Button(cal_window, command=lambda: clear(), width="10", height="3", text="Clear")
btnclear.grid(row=4, column=1)

btnequal = Button(cal_window, command=lambda: equalpress(), width="10", height="3", text="=")
btnequal.grid(row=4, column=2)

btndiv = Button(cal_window, command=lambda: [oper(), display(" / ")], width="10", height="3", text="/")
btndiv.grid(row=4, column=3)

btnbs = Button(cal_window, command=lambda: [oper(),backspace()], width="10", height="3", text="<-")
btnbs.grid(row=5, column=0, pady=10)

cal_window.mainloop()

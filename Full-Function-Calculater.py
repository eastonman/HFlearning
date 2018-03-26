import tkinter
from tkinter import messagebox


def Plus_onClick():
    global Cal_Num_1
    global Cal_Num_2
    global Current_Num
    global Operator
    Cal_Num_1 = Current_Num
    Current_Num = 0
    Operator = '+'
    Main_Output_Window.config(text='')


def Minus_onClick():
    global Cal_Num_1
    global Cal_Num_2
    global Current_Num
    global Operator
    Cal_Num_1 = Current_Num
    Current_Num = 0
    Operator = '-'
    Main_Output_Window.config(text='')


def Multi_onClick():
    global Cal_Num_1
    global Cal_Num_2
    global Current_Num
    global Operator
    Cal_Num_1 = Current_Num
    Current_Num = 0
    Operator = 'x'
    Main_Output_Window.config(text='')


def Div_onClick():
    global Cal_Num_1
    global Cal_Num_2
    global Current_Num
    global Operator
    Cal_Num_1 = Current_Num
    Current_Num = 0
    Operator = '/'
    Main_Output_Window.config(text='')


def Num_Button_onClick(Num):
    global Current_Num
    Current_Num = Current_Num * 10 + Num
    Main_Output_Window.config(text=Current_Num)


def Equal_Button_onClick():
    global Operator
    global Cal_Num_1
    global Current_Num
    if Operator == '+':
        Main_Output_Window.config(text=str(Cal_Num_1 + Current_Num))
    if Operator == '-':
        Main_Output_Window.config(text=str(Cal_Num_1 - Current_Num))
    if Operator == 'x':
        Main_Output_Window.config(text=str(Cal_Num_1 * Current_Num))
    if Operator == '/':
        # Check If Second_Num IS ZERO
        if Current_Num == 0:
            messagebox.showinfo(message='Divided by zero!')
            return
        Main_Output_Window.config(text=str(Cal_Num_1 / Current_Num))


if __name__ == '__main__':
    # Initial Main_Activity
    Main_Activity = tkinter.Tk()
    Main_Activity.geometry("400x300")
    Main_Activity.title("按键计算器")

    # Global Varible Definition Begin
    Current_Num = 0
    Cal_Num_1 = 0
    Cal_Num_2 = 0
    Operator = ''
    # Definition END

    # Widget Definition Begin

    Main_Output_Window = tkinter.Label(Main_Activity, width=30)

    Num_Button_1 = tkinter.Button(
        Main_Activity, text="1", command=lambda: Num_Button_onClick(1))
    Num_Button_2 = tkinter.Button(
        Main_Activity, text="2", command=lambda: Num_Button_onClick(2))
    Num_Button_3 = tkinter.Button(
        Main_Activity, text="3", command=lambda: Num_Button_onClick(3))
    Num_Button_4 = tkinter.Button(
        Main_Activity, text="4", command=lambda: Num_Button_onClick(4))
    Num_Button_5 = tkinter.Button(
        Main_Activity, text="5", command=lambda: Num_Button_onClick(5))
    Num_Button_6 = tkinter.Button(
        Main_Activity, text="6", command=lambda: Num_Button_onClick(6))
    Num_Button_7 = tkinter.Button(
        Main_Activity, text="7", command=lambda: Num_Button_onClick(7))
    Num_Button_8 = tkinter.Button(
        Main_Activity, text="8", command=lambda: Num_Button_onClick(8))
    Num_Button_9 = tkinter.Button(
        Main_Activity, text="9", command=lambda: Num_Button_onClick(9))
    Num_Button_0 = tkinter.Button(
        Main_Activity, text="0", command=lambda: Num_Button_onClick(0))

    Plus_Button = tkinter.Button(
        Main_Activity, text="+", command=Plus_onClick)
    Minus_Button = tkinter.Button(
        Main_Activity, text="-", command=Minus_onClick)
    Multi_Button = tkinter.Button(
        Main_Activity, text="x", command=Multi_onClick)
    Div_Button = tkinter.Button(
        Main_Activity, text="/", command=Div_onClick)
    Equal_Button = tkinter.Button(
        Main_Activity, text="=", command=Equal_Button_onClick)

    Output_TextBox = tkinter.Text(Main_Activity)
    # Definition END

    # Pack Widget Into Main_Activity Using Grid
    Main_Output_Window.grid(row=1, columnspan=4)
    Num_Button_1.grid(row=2, column=0)
    Num_Button_2.grid(row=2, column=1)
    Num_Button_3.grid(row=2, column=2)
    Num_Button_4.grid(row=3, column=0)
    Num_Button_5.grid(row=3, column=1)
    Num_Button_6.grid(row=3, column=2)
    Num_Button_7.grid(row=4, column=0)
    Num_Button_8.grid(row=4, column=1)
    Num_Button_9.grid(row=4, column=2)
    Num_Button_0.grid(row=5, column=0)

    Plus_Button.grid(row=2, column=3)
    Minus_Button.grid(row=3, column=3)
    Multi_Button.grid(row=4, column=3)
    Div_Button.grid(row=5, column=3)
    Equal_Button.grid(row=6, column=3)

    # Plus_Button.pack()
    # Minus_Button.pack()
    # Multi_Button.pack()
    # Div_Button.pack()
    # Output_TextBox.pack()
    # Pack END

    # Main Loop Start
    Main_Activity.mainloop()

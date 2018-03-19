import tkinter
from math import sqrt as sqrt
from tkinter import messagebox

def calDistance():
    sqrt()

if __name__ == '__main__':
    # Initial Main_Activity
    Main_Activity = tkinter.Tk()
    Main_Activity.geometry('400x500')
    Main_Activity.title('平面中任意两点之间的距离')

    # Define Widget
    First_X_Entry = tkinter.Entry(Main_Activity)
    First_Y_Entry = tkinter.Entry(Main_Activity)
    Second_X_Entry = tkinter.Entry(Main_Activity)
    Second_Y_Entry = tkinter.Entry(Main_Activity)
    Cal_Process_Button = tkinter.Button(Main_Activity,text='',command=calDistance)
    Distance_Output_TextBox = tkinter.Text(Main_Activity)
    # Define Widget END


    # Pack Widget Into Main_Activity
    First_X_Entry.pack()
    First_Y_Entry.pack()
    Second_X_Entry.pack()
    Second_Y_Entry.pack()
    # Pack END

    # Main Loop Start
    Main_Activity.mainloop()
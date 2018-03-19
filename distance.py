import tkinter
import math
from tkinter import messagebox


def calDistance():
    if  not ((First_X_Entry.get().isnumeric()) and (First_Y_Entry.get().isnumeric()) and (Second_X_Entry.get().isnumeric()) and (Second_Y_Entry.get().isnumeric())):
        messagebox.showinfo(message='输入非法！！！！！')
        return

    First_X = float(First_X_Entry.get())
    First_Y = float(First_Y_Entry.get())
    Second_X = float(Second_X_Entry.get())
    Second_Y = float(Second_Y_Entry.get())

    Distance_Output_TextBox.delete(0.0,'end')
    Distance_Output_TextBox.insert('end',math.sqrt((First_X - Second_X) * (First_X - Second_X) + (First_Y - Second_Y) * (First_Y - Second_Y)))
    #Distance_Output_TextBox.insert('end',math.sqrt(int(12)))


if __name__ == '__main__':
    # Initial Main_Activity
    Main_Activity = tkinter.Tk()
    Main_Activity.geometry('500x600')
    Main_Activity.title('平面中任意两点之间的距离')

    # Define Widget
    First_X_Entry = tkinter.Entry(Main_Activity, width=25)
    First_X_Entry_Label = tkinter.Label(Main_Activity,text='X1')
    First_Y_Entry = tkinter.Entry(Main_Activity, width=25)
    First_Y_Entry_Label = tkinter.Label(Main_Activity, text='Y1')
    Second_X_Entry = tkinter.Entry(Main_Activity, width=25)
    Second_X_Entry_Label = tkinter.Label(Main_Activity, text='X2')
    Second_Y_Entry = tkinter.Entry(Main_Activity ,width=25)
    Second_Y_Entry_Label = tkinter.Label(Main_Activity, text='Y2')
    Cal_Process_Button = tkinter.Button(Main_Activity, text='两点之间的距离是', command=calDistance)
    Distance_Output_TextBox = tkinter.Text(Main_Activity, width=20,height= 5)
    # Define Widget END


    # Pack Widget Into Main_Activity
    First_X_Entry_Label.grid(row=0 ,column=0)
    First_X_Entry.grid(row=0, column=1)
    First_Y_Entry_Label.grid(row=0, column=2)
    First_Y_Entry.grid(row=0, column=3)
    Second_X_Entry_Label.grid(row=1, column=0)
    Second_X_Entry.grid(row=1, column=1)
    Second_Y_Entry_Label.grid(row=1, column=2)
    Second_Y_Entry.grid(row=1, column=3)
    Cal_Process_Button.grid(row=2, column=0)
    Distance_Output_TextBox.grid(row=2, column=1)
    # Pack END

    # Main Loop Start
    Main_Activity.mainloop()

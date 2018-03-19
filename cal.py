import tkinter
from tkinter import messagebox


def process_op1():
    first_num = int(first_num_entry.get())
    second_num = int(second_num_entry.get())
    # if ( operation == '+' ):
    # print(str(first_num+second_num))
    output_textbox.delete(0.0, 'end')
    output_textbox.insert('end', str(first_num + second_num))


def process_op2():
    first_num = int(first_num_entry.get())
    second_num = int(second_num_entry.get())
    # if ( operation == '+' ):
    # print(str(first_num+second_num))
    output_textbox.delete(0.0, 'end')
    output_textbox.insert('end', str(first_num - second_num))


def process_op3():
    first_num = int(first_num_entry.get())
    second_num = int(second_num_entry.get())
    # if ( operation == '+' ):
    # print(str(first_num+second_num))
    output_textbox.delete(0.0, 'end')
    output_textbox.insert('end', str(first_num * second_num))


def process_op4():
    first_num = int(first_num_entry.get())
    second_num = int(second_num_entry.get())
    # if ( operation == '+' ):
    # print(str(first_num+second_num))
    if second_num == 0:
        messagebox.showinfo(message='divided by zero!')
        return
    output_textbox.delete(0.0, 'end')
    output_textbox.insert('end', str(first_num / second_num))


if __name__ == '__main__':
    main_activity = tkinter.Tk()
    main_activity.geometry("400x300")
    main_activity.title("简易计算器")

    # define

    first_num_entry = tkinter.Entry(main_activity)
    second_num_entry = tkinter.Entry(main_activity)
    plus_button = tkinter.Button(main_activity, text="+", command=process_op1)
    minus_button = tkinter.Button(main_activity, text="-", command=process_op2)
    multi_button = tkinter.Button(main_activity, text="x", command=process_op3)
    div_button = tkinter.Button(main_activity, text="/", command=process_op4)

    output_textbox = tkinter.Text(main_activity)
    # process_button = tkinter.Button(main_activity, text="output", command=process_op)
    # define end




    # add to main activity
    first_num_entry.pack()
    second_num_entry.pack()
    plus_button.pack()
    minus_button.pack()
    multi_button.pack()
    div_button.pack()
    # process_button.pack()
    output_textbox.pack()

    main_activity.mainloop()

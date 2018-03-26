import tkinter


def pass_text():
    texttopass = enter_textbox.get()
    assert isinstance(texttopass, object)
    output_textbox.delete(0.0,'end')
    output_textbox.insert('end', texttopass)


if __name__ == '__main__':

    main_activity = tkinter.Tk()
    main_activity.geometry("400x300")
    main_activity.title("内容传送小程序")
    #head define end

    #define things
    enter_textbox = tkinter.Entry(main_activity)
    output_textbox = tkinter.Text(main_activity,height=4)
    command_button = tkinter.Button(main_activity,text="开始传送",command=pass_text)
    #define end

    #output_textbox.insert('insert','test')
    enter_textbox.pack()
    command_button.pack()
    output_textbox.pack()
    main_activity.mainloop()

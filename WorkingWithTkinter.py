import tkinter
root = tkinter.Tk()
widgt1 = tkinter.Label(text = 'Hello')
widgt1.pack()
widgt2 = tkinter.Button(text = "Click to quit", command = quit)
widgt2.pack()
root.mainloop()

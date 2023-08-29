import tkinter
def Stress():
    L = []
    global l
    while l:
        L.append("LOLHVJB VBYGVYJTYCY HCV VHJVV V H ")
def Stop():
        l = False
#__main__
l = True
root = tkinter.Tk
w1 = tkinter.Label(text = 'RAM Stress can be started by pressing the button below.')
w1.pack()
w2 = tkinter.Button(text = 'Start Stressing',command = Stress)
w2.pack()
w3 = tkinter.Button(text = 'Stop Stressing',command = Stop)
w3.pack()
root.mainloop()

import tkinter as gui
win_x = 800
win_y = 600
def main():
    mainwin = gui.Tk()
    mainwin.geometry(str(win_x)+'x'+str(win_y))
    widget1 = gui.Button(main, text = "PRESS", command = main)
    widget1.place(win_x/2,win_y/2)
    widget1.pack()
    mainwin.mainloop()
main()

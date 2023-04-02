from tkinter import *
from test import select_file
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

window = Tk()
window.title("Steganography System")
window.geometry("900x600")
window.resizable(False, False)
frame = Frame(window, bg='Ivory', relief=RIDGE)
frame.place(x=0, y=0, width=900, height=600)

c1frame = Label(frame, bg='#5882A5', text="Steganography", font=("arial", 20, "bold"), fg="white")
c1frame.place(x=0, y=0, width=900, height=100)

frame1 = Frame(frame, bg='gold')
frame1.place(x=0, y=100, width=400, height=500)
Label(frame1, text="Upload Image", font=("arial", 20, "bold"), background="gold").place(x=50, y=10, width=200,height=40)


Label(frame1, text="Pic", background="white").place(x=10, y=50, width=350, height=250)
open_img_btn = Button(frame1, text="Open image", bg="black", fg="white", command=select_file).place(x=20, y=340, width=150, height=50)
save_img_btn = Button(frame1, text="Save Image", bg="black", fg="white", command=select_file).place(x=230, y=340, width=150, height=50)

def hidedata_box():
    frame2 = Frame(frame, bg='ivory')
    frame2.place(x=400, y=100, width=500, height=480)
    Button(frame2, text="Hide Data", font=("arial", 20, "bold"), background="ivory", command=hidedata_box).place(x=50, y=10, width=200,
                                                                                           height=40)
    Button(frame2, text="Show Data", font=("arial", 20, "bold"), background="ivory", command=showdata_box).place(x=250, y=10,
                                                                                                        width=200,
                                                                                                        height=40)

    Label(frame2, text="Input Type :", background="ivory").place(x=0, y=60, width=200, height=40)
    Entry(frame2).place(x=150, y=70, width=200, height=20)

    Label(frame2, text="Pic", background="grey").place(x=30, y=100, width=450, height=200)

    Label(frame2, text="Password", background="ivory").place(x=30, y=310, width=100, height=40)
    Entry(frame2).place(x=30, y=350, width=100, height=20)
    Label(frame2, text="Confirm password", background="ivory").place(x=200, y=310, width=100, height=40)
    Entry(frame2).place(x=200, y=350, width=100, height=20)
    Label(frame2, text="Hide Data", background="ivory").place(x=350, y=310, width=100, height=40)
    Entry(frame2).place(x=350, y=350, width=100, height=20)
    Button(frame2, text="Upload", font=("arial", 14, "bold"), background="black", foreground="white").place(x=100,
                                                                                                            y=400,
                                                                                                            width=200,
                                                                                                            height=40)


def showdata_box():
    frame3 = Frame(frame, bg='#838abd')
    Button(frame3, text="Hide Data", font=("arial", 20, "bold"), background="ivory", command=hidedata_box).place(x=50, y=10, width=200,
                                                                                           height=40)
    Button(frame3, text="Show Data", font=("arial", 20, "bold"), background="ivory", command=showdata_box).place(x=250, y=10,
                                                                                                        width=200,
                                                                                                        height=40)

    frame3.place(x=400, y=100, width=500, height=530)
    Label(frame3, text="Enter Key", background="#838abd").place(x=30, y=50, width=100, height=40)
    Entry(frame3).place(x=30, y=90, width=100, height=20)
    Button(frame3, text="Show Data", bg="black", fg="white").place(x=200, y=80, width=100, height=30)
    Label(frame3, text="Pic", background="white").place(x=30, y=130, width=450, height=300)

hidedata_box()



if __name__ == "__main__":
    window.mainloop()

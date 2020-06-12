from tkinter import *
import subprocess, os
from PIL import ImageTk
import PIL.Image
cwd = os.getcwd()
cwda = cwd + "\\data\\"

root = Tk()
root.geometry("476x290")
root.resizable(False, False)
root.iconbitmap(cwd + "\\images\\spade.ico")
root.title("Skin Shop")

tier0 = False
tier1 = False
tier2 = False
tier3 = False
tier0b = False
tier1b = False
tier2b = False
tier3b = False


def main(arg):
    global tier0, tier1, tier2, tier3, tier0b, tier1b, tier2b, tier3b
    if arg == "0":
        with open(cwda + "eqski.txt", "r+")as file:
            tempo = file.read()
            file.truncate()
            file.seek(0)
            file.write("1" + tempo[1:])
    elif arg == "1":
        if tier1:
            with open(cwda + "eqski.txt", "r+")as file:
                tempo = file.read()
                file.truncate()
                file.seek(0)
                file.write("2" + tempo[1:])
        else:
            with open(cwda + "bjdata.txt", "r+")as file:
                tempo = file.read()
                if int(tempo) >= 1000:
                    file.truncate()
                    file.seek(0)
                    file.write(str(int(tempo) - 1000))
                    with open(cwda + "skidata.txt", "r+")as file2:
                        tempo = file2.read()
                        tempo = int(tempo) + 100
                        file2.truncate()
                        file2.seek(0)
                        file2.write(str(tempo))
    elif arg == "2":
        if tier2:
            with open(cwda + "eqski.txt", "r+")as file:
                tempo = file.read()
                file.truncate()
                file.seek(0)
                file.write("3" + tempo[1:])
        else:
            with open(cwda + "bjdata.txt", "r+")as file:
                tempo = file.read()
                if int(tempo) >= 5000:
                    file.truncate()
                    file.seek(0)
                    file.write(str(int(tempo) - 5000))
                    with open(cwda + "skidata.txt", "r+")as file2:
                        tempo = file2.read()
                        tempo = int(tempo) + 10
                        file2.truncate()
                        file2.seek(0)
                        file2.write(str(tempo))
    elif arg == "3":
        if tier3:
            with open(cwda + "eqski.txt", "r+")as file:
                tempo = file.read()
                file.truncate()
                file.seek(0)
                file.write("4" + tempo[1:])
        else:
            with open(cwda + "bjdata.txt", "r+")as file:
                tempo = file.read()
                if int(tempo) >= 10000:
                    file.truncate()
                    file.seek(0)
                    file.write(str(int(tempo) - 10000))
                    with open(cwda + "skidata.txt", "r+")as file2:
                        tempo = file2.read()
                        tempo = int(tempo) + 1
                        file2.truncate()
                        file2.seek(0)
                        file2.write(str(tempo))
    elif arg == "0b":
        with open(cwda + "eqski.txt", "r+")as file:
            tempo = file.read()
            file.truncate()
            file.seek(0)
            file.write(tempo[0:] + "1")
    elif arg == "1b":
        if tier1b:
            with open(cwda + "eqski.txt", "r+")as file:
                tempo = file.read()
                file.truncate()
                file.seek(0)
                file.write(tempo[0:1] + "2")
        else:
            with open(cwda + "bjdata.txt", "r+")as file:
                tempo = file.read()
                if int(tempo) >= 1000:
                    file.truncate()
                    file.seek(0)
                    file.write(str(int(tempo) - 1000))
                    with open(cwda + "skidata_.txt", "r+")as file2:
                        tempo = file2.read()
                        tempo = int(tempo) + 100
                        file2.truncate()
                        file2.seek(0)
                        file2.write(str(tempo))
    elif arg == "2b":
        if tier2b:
            with open(cwda + "eqski.txt", "r+")as file:
                tempo = file.read()
                file.truncate()
                file.seek(0)
                file.write(tempo[0:1] + "3")
        else:
            with open(cwda + "bjdata.txt", "r+")as file:
                tempo = file.read()
                if int(tempo) >= 5000:
                    file.truncate()
                    file.seek(0)
                    file.write(str(int(tempo) - 5000))
                    with open(cwda + "skidata_.txt", "r+")as file2:
                        tempo = file2.read()
                        tempo = int(tempo) + 10
                        file2.truncate()
                        file2.seek(0)
                        file2.write(str(tempo))
    elif arg == "3b":
        if tier3b:
            with open(cwda + "eqski.txt", "r+")as file:
                tempo = file.read()
                file.truncate()
                file.seek(0)
                file.write(tempo[0:1] + "4")
        else:
            with open(cwda + "bjdata.txt", "r+")as file:
                tempo = file.read()
                if int(tempo) >= 10000:
                    file.truncate()
                    file.seek(0)
                    file.write(str(int(tempo) - 10000))
                    with open(cwda + "skidata_.txt", "r+")as file2:
                        tempo = file2.read()
                        tempo = int(tempo) + 1
                        file2.truncate()
                        file2.seek(0)
                        file2.write(str(tempo))
    root.destroy()
    subprocess.call(cwd + "\\Black_Jack.exe")


class varin(object):

    def __init__(self, get):
        self.get = temporarly


cd = {}

load = PIL.Image.open(cwd + "\\images\\PNG\\gray_back.png")
load2 = load.resize((115, 176))
temporarly = PIL.ImageTk.PhotoImage(load2)
cd["T0"] = varin(temporarly)
load = PIL.Image.open(cwd + "\\images\\PNG\\t1.png")
load2 = load.resize((115, 176))
temporarly = PIL.ImageTk.PhotoImage(load2)
cd["T1"] = varin(temporarly)
load = PIL.Image.open(cwd + "\\images\\PNG\\t2.png")
load2 = load.resize((115, 176))
temporarly = PIL.ImageTk.PhotoImage(load2)
cd["T2"] = varin(temporarly)
load = PIL.Image.open(cwd + "\\images\\PNG\\t3.png")
load2 = load.resize((115, 176))
temporarly = PIL.ImageTk.PhotoImage(load2)
cd["T3"] = varin(temporarly)

tii0 = cd["T0"].get
tii1 = cd["T1"].get
tii2 = cd["T2"].get
tii3 = cd["T3"].get

ti0 = Label(root, image=tii0)
ti0.image = tii0
ti1 = Label(root, image=tii1)
ti1.image = tii1
ti2 = Label(root, image=tii2)
ti2.image = tii2
ti3 = Label(root, image=tii3)
ti3.image = tii3

ti0.grid()
ti1.grid(row=0, column=1)
ti2.grid(row=0, column=2)
ti3.grid(row=0, column=3)

b0 = Button(root, text="ERR", width=10, command=lambda: main("0"))
b1 = Button(root, text="ERR", width=10, command=lambda: main("1"))
b2 = Button(root, text="ERR", width=10, command=lambda: main("2"))
b3 = Button(root, text="ERR", width=10, command=lambda: main("3"))

b0.grid(row=1)
b1.grid(row=1, column=1)
b2.grid(row=1, column=2)
b3.grid(row=1, column=3)

placeholder = Label(root)
placeholder.grid(row=2, columnspan=3)

c1 = Label(root, text="Black Jack!", fg="white", bg="green", width=10)
c2 = Label(root, text="Black Jack!", fg="black", width=10)
c3 = Label(root, text="Black Jack!", fg="white", bg="blue", width=10)
c4 = Label(root, text="Black Jack!", fg="white", bg="#8257fe", width=10)

c1.grid(row=3, column=0)
c2.grid(row=3, column=1)
c3.grid(row=3, column=2)
c4.grid(row=3, column=3)

b0b = Button(root, text="ERR", width=10, command=lambda: main("0b"))
b1b = Button(root, text="ERR", width=10, command=lambda: main("1b"))
b2b = Button(root, text="ERR", width=10, command=lambda: main("2b"))
b3b = Button(root, text="ERR", width=10, command=lambda: main("3b"))

b0b.grid(row=4)
b1b.grid(row=4, column=1)
b2b.grid(row=4, column=2)
b3b.grid(row=4, column=3)


with open(cwda + "skidata.txt", "r")as file:
    d = file.read()
    temp = d[0:1]
    if temp == "1":
        tier0 = True
        b0.config(text="OWNED")
    temp = d[1:2]
    if temp == "1":
        tier1 = True
        b1.config(text="OWNED")
    else:
        b1.config(text="$1000")
    temp = d[2:3]
    if temp == "1":
        tier2 = True
        b2.config(text="OWNED")
    else:
        b2.config(text="$5000")
    temp = d[3:4]
    if temp == "1":
        tier3 = True
        b3.config(text="OWNED")
    else:
        b3.config(text="$10000")

with open(cwda + "skidata_.txt", "r")as file:
    d = file.read()
    temp = d[0:1]
    if temp == "1":
        tier0b = True
        b0b.config(text="OWNED")
    temp = d[1:2]
    if temp == "1":
        tier1b = True
        b1b.config(text="OWNED")
    else:
        b1b.config(text="$1000")
    temp = d[2:3]
    if temp == "1":
        tier2b = True
        b2b.config(text="OWNED")
    else:
        b2b.config(text="$5000")
    temp = d[3:4]
    if temp == "1":
        tier3b = True
        b3b.config(text="OWNED")
    else:
        b3b.config(text="$10000")


root.mainloop()
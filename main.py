from tkinter import *
import os, random, time, threading
from PIL import ImageTk
import PIL.Image

cwd = os.getcwd()

#money
with open(cwd + "\\data\\bjdata.txt", "r")as file:
    money = file.read()
    money = int(money)

#moments
moment = "start"

#global vars
betvar = 0
val = 0
dval = 0
cantt = 0
dcantt = 0
ress = None

co = ["H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13", "S1", "S2", "S3", "S4",
          "S5", "S6", "S7", "S8", "S9", "S10", "S11", "S12", "S13", "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8",
          "D9", "D10", "D11", "D12", "D13", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12",
          "C13"]


def mainfunc():
    global moment
    if moment == "start":
        cards()
    elif moment == "bet":
        while moment == "bet":
            return 0
    elif moment == "play":
            game()
    elif moment == "done":
        moneyg()


def betopti(opt):
    global moment, betvar, money
    if moment == "bet":
        if opt == "+10":
            betvar += 10
        elif opt == "+50":
            betvar += 50
        elif opt == "+100":
            betvar += 100
        elif opt == "-10":
            betvar -= 10
            if betvar < 0:
                betvar = 0
        elif opt == "d":
            comment.config(text="Let's begin then!")
            money -= betvar
            if money < 0:
                comment.config(text="Can't bet that much!")
                money += betvar
                cash.config(text="$" + str(money))
            elif betvar == 0:
                comment.config(text="You must bet to play!")
                return 0
            else:
                cash.config(text="$" + str(money))
                moment = "play"
                mainfunc()
        beta.config(text="$" + str(betvar))
    else:
        comment.config(text="Can't bet now!")


def game():
    global moment, cd, card1i, card2i, card3i, card4i, card5i, val, dval, dc1i, dc2i, dc3i, dc4i, cantt, dcantt, back
    global ress, co
    val = 0
    dval = 0
    tem = random.choice(co)
    n = tem[1:]
    n = int(n)
    if 11 > n > 1:
        val += n
    elif n >= 11:
        val += 10
    elif n == 1:
        val += 11
    card1i = cd[tem].get
    co.remove(tem)
    card1.config(image=card1i)
    card1.image = card1i
    card1.place(x=903, y=650)
    time.sleep(1)
    root.update()
    tem = random.choice(co)
    n = tem[1:]
    n = int(n)
    if 11 > n > 1:
        dval += n
    elif n >= 11:
        dval += 10
    elif n == 1:
        dval += 11
    dc1i = cd[tem].get
    co.remove(tem)
    dc1.config(image=back)
    dc1.image = back
    dc1.place(x=640, y=75)
    time.sleep(1)
    root.update()
    tem = random.choice(co)
    n = tem[1:]
    n = int(n)
    if 11 > n > 1:
        val += n
    elif n >= 11:
        val += 10
    elif n == 1 and val + 11 <= 21:
        val += 11
    else:
        val += 1
    card2i = cd[tem].get
    co.remove(tem)
    card2.config(image=card2i)
    card2.image = card2i
    card2.place(x=960, y=562)
    time.sleep(1)
    root.update()
    tem = random.choice(co)
    n = tem[1:]
    n = int(n)
    if 11 > n > 1:
        dval += n
    elif n >= 11:
        dval += 10
    elif n == 1:
        dval += 11
    elif n == 1 and dval + 11 <= 21:
        dval += 11
    else:
        dval += 1
    dc2i = cd[tem].get
    co.remove(tem)
    dc2.config(image=dc2i)
    dc2.image = dc2i
    dc2.place(x=800, y=75)
    time.sleep(1)
    root.update()
    cantt = 2
    dcantt = 2
    if val == 21:
        if card1i == cd["H11"].get or cd["S11"].get or cd["D11"].get or cd["C11"].get:
            if card2i == cd["S1"].get or cd["C1"].get or cd["D1"].get or cd["H1"].get:
                ress = "winb"
                comment.config(text="You have got Black Jack!")
                moneyg()
        elif card2i == cd["H11"].get or cd["S11"].get or cd["D11"].get or cd["C11"].get:
            if card1i == cd["S1"].get or cd["C1"].get or cd["D1"].get or cd["H1"].get:
                ress = "winb"
                comment.config(text="You have got Black Jack!")
                moneyg()
        else:
            ai()
    else:
        moment = "play2"
        comment.config(text="Stay or Hit??")
        return 0


def opti(f):
    global moment, cantt, dcantt, co, val, card3i, card4i, card5i, ress
    if moment == "play2":
        if f == "h":
            if cantt != 5:
                if cantt == 2:
                    tem = random.choice(co)
                    n = tem[1:]
                    n = int(n)
                    if 11 > n > 1:
                        val += n
                    elif n >= 11:
                        val += 10
                    elif n == 1 and val + 11 <= 21:
                        val += 11
                    else:
                        val += 1
                    card3i = cd[tem].get
                    co.remove(tem)
                    card3.config(image=card3i)
                    card3.image = card3i
                    card3.place(x=1017, y=474)
                    time.sleep(1)
                    root.update()
                    cantt += 1
                    if val > 20:
                        if val == 21:
                            ai()
                        comment.config(text="Aww, you got busted...")
                        time.sleep(1)
                        root.update()
                        ress = "loss"
                        moneyg()
                elif cantt == 3:
                    tem = random.choice(co)
                    n = tem[1:]
                    n = int(n)
                    if 11 > n > 1:
                        val += n
                    elif n >= 11:
                        val += 10
                    elif n == 1 and val + 11 <= 21:
                        val += 11
                    else:
                        val += 1
                    card4i = cd[tem].get
                    co.remove(tem)
                    card4.config(image=card4i)
                    card4.image = card4i
                    card4.place(x=1074, y=386)
                    time.sleep(1)
                    root.update()
                    cantt += 1
                    if val > 20:
                        if val == 21:
                            ai()
                        comment.config(text="Aww, you got busted...")
                        time.sleep(1)
                        root.update()
                        ress = "loss"
                        moneyg()
                elif cantt == 4:
                    tem = random.choice(co)
                    n = tem[1:]
                    n = int(n)
                    if 11 > n > 1:
                        val += n
                    elif n >= 11:
                        val += 10
                    elif n == 1 and val + 11 <= 21:
                        val += 11
                    else:
                        val += 1
                    card5i = cd[tem].get
                    co.remove(tem)
                    card5.config(image=card5i)
                    card5.image = card5i
                    card5.place(x=1137, y=298)
                    time.sleep(1)
                    root.update()
                    cantt += 1
                    if val > 20:
                        if val == 21:
                            ai()
                        comment.config(text="Aww, you got busted...")
                        time.sleep(1)
                        root.update()
                        ress = "loss"
                        moneyg()
            else:
                ai()
        elif f == "s":
            time.sleep(1)
            root.update()
            ai()
    else:
        comment.config(text="You can't make those choices now...")


def ai():
    global moment, cantt, dcantt, co, val, dc1i, dc3i, dc4i, ress, dval
    comment.config(text="Let's see what dealer's got!")
    dc1.config(image=dc1i)
    time.sleep(1)
    root.update()
    if dval == 21:
        if dc1i == cd["H11"].get or cd["S11"].get or cd["D11"].get or cd["C11"].get:
            if dc2i == cd["S1"].get or cd["C1"].get or cd["D1"].get or cd["H1"].get:
                ress = "loss"
                comment.config(text="Dealer have got Black Jack!")
                moneyg()
        elif dc2i == cd["H11"].get or cd["S11"].get or cd["D11"].get or cd["C11"].get:
            if dc1i == cd["S1"].get or cd["C1"].get or cd["D1"].get or cd["H1"].get:
                ress = "loss"
                comment.config(text="Dealer have got Black Jack!")
                moneyg()
    if val > dval:
        if dval < 17:
            if dcantt != 4:
                time.sleep(1)
                root.update()
                if dcantt == 2:
                    tem = random.choice(co)
                    n = tem[1:]
                    n = int(n)
                    if 11 > n > 1:
                        dval += n
                    elif n >= 11:
                        dval += 10
                    elif n == 1 and dval + 11 <= 21:
                        dval += 11
                    else:
                        dval += 1
                    dc3i = cd[tem].get
                    co.remove(tem)
                    dc3.config(image=dc3i)
                    dc3.image = dc3i
                    dc3.place(x=960, y=75)
                    time.sleep(1)
                    root.update()
                    dcantt += 1
                    if dval > 20:
                        if dval == 21:
                            ai()
                        comment.config(text="Dealer's busted!")
                        ress = "win"
                        moneyg()
                    else:
                        ai()
                elif dcantt == 3:
                    tem = random.choice(co)
                    n = tem[1:]
                    n = int(n)
                    if 11 > n > 1:
                        dval += n
                    elif n >= 11:
                        dval += 10
                    elif n == 1 and dval + 11 <= 21:
                        dval += 11
                    else:
                        dval += 1
                    dc4i = cd[tem].get
                    co.remove(tem)
                    dc4.config(image=dc4i)
                    dc4.image = dc4i
                    dc4.place(x=1120, y=75)
                    time.sleep(1)
                    root.update()
                    dcantt += 1
                    if dval > 20:
                        if dval == 21:
                            pass
                        comment.config(text="Dealer's busted!")
                        ress = "win"
                        moneyg()
                    else:
                        ai()
            else:
                comment.config(text="You won!")
                ress = "win"
                moneyg()
        else:
            comment.config(text="You won!")
            ress = "win"
            moneyg()
    elif dval == val:
        comment.config(text="Draw...")
        ress = "draw"
        moneyg()
    else:
        comment.config(text="You lost!")
        ress = "loss"
        moneyg()


def moneyg():
    global moment, betvar, ress, money
    if ress == "winb":
        money += (betvar * 3)
    elif ress == "win":
        money += (betvar * 2)
    elif ress == "draw":
        money += betvar
    elif ress == "loss":
        money = money
    time.sleep(1)
    root.update()
    #RESET
    cash.config(text="$" + str(money))
    with open(cwd + "\\data\\bjdata.txt", "w")as filel:
        filel.truncate()
        filel.seek(0)
        filel.write(str(money))
    moment = "start"
    card1.place_forget()
    card2.place_forget()
    card3.place_forget()
    card4.place_forget()
    card5.place_forget()
    dc1.place_forget()
    dc2.place_forget()
    dc3.place_forget()
    dc4.place_forget()
    betvar = 0
    beta.config(text="$" + str(betvar))
    mainfunc()


def cards():
    global moment, co
    co = ["H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13", "S1", "S2", "S3", "S4",
          "S5", "S6", "S7", "S8", "S9", "S10", "S11", "S12", "S13", "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8",
          "D9", "D10", "D11", "D12", "D13", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12",
          "C13"]
    moment = "bet"
    mainfunc()


#database creator
class varin(object):

    def __init__(self, get):
        self.get = temporarly


root = Tk()

#window
root.title("Black Jack")
root.state('zoomed')
root.resizable(False, False)
root.iconbitmap(cwd + "\\images\\spade.ico")

#databases and render assets
temporarly = 0
numc = 1
numd = 1
numh = 1
nums = 1
c = 1
d = 1
h = 1
s = 1
cd = {}


#render
def render():
    global c, d, h, s, numc, numd, numh, nums, cd, temporarly
    temporarly = 0
    numc = 1
    numd = 1
    numh = 1
    nums = 1
    c = 1
    d = 1
    h = 1
    s = 1
    cd.clear()
    for i in range(53):
        if c != 14:
            load = PIL.Image.open(cwd + "\\images\\PNG\\" + str(numc) + "C.png")
            load2 = load.resize((115, 176))
            temporarly = PIL.ImageTk.PhotoImage(load2)
            cd["C" + str(numc)] = varin(temporarly)
            c += 1
            numc = int(numc)
            numc = numc + 1
        elif d != 14:
            load = PIL.Image.open(cwd + "\\images\\PNG\\" + str(numd) + "D.png")
            load2 = load.resize((115, 176))
            temporarly = PIL.ImageTk.PhotoImage(load2)
            cd["D" + str(numd)] = varin(temporarly)
            d += 1
            numd = int(numd)
            numd = numd + 1
        elif h != 14:
            load = PIL.Image.open(cwd + "\\images\\PNG\\" + str(numh) + "H.png")
            load2 = load.resize((115, 176))
            temporarly = PIL.ImageTk.PhotoImage(load2)
            cd["H" + str(numh)] = varin(temporarly)
            h += 1
            numh = int(numh)
            numh = numh + 1
        elif s != 14:
            load = PIL.Image.open(cwd + "\\images\\PNG\\" + str(nums) + "S.png")
            load2 = load.resize((115, 176))
            temporarly = PIL.ImageTk.PhotoImage(load2)
            cd["S" + str(nums)] = varin(temporarly)
            s += 1
            nums = int(nums)
            nums = nums + 1
        elif s == 14:
            load = PIL.Image.open(cwd + "\\images\\PNG\\gray_back.png")
            load2 = load.resize((115, 176))
            temporarly = PIL.ImageTk.PhotoImage(load2)
            cd["BACK"] = varin(temporarly)
            load = PIL.Image.open(cwd + "\\images\\chip.png")
            load2 = load.resize((115, 115))
            temporarly = PIL.ImageTk.PhotoImage(load2)
            cd["CHIP"] = varin(temporarly)


render()

chip = cd["CHIP"].get
back = cd["BACK"].get
card1i = cd["BACK"].get
card2i = cd["BACK"].get
card3i = cd["BACK"].get
card4i = cd["BACK"].get
card5i = cd["BACK"].get
dc1i = cd["BACK"].get
dc2i = cd["BACK"].get
dc3i = cd["BACK"].get
dc4i = cd["BACK"].get
#display pictures

#all screen widgets
cash = Label(root, text="$" + str(money), width=10, font=("Helvetica", 36))
img = Label(root, image=chip)
img.image = chip
deck = Button(root, image=back, command=lambda: opti("h"))
stay = Button(root, text="STAY", font=("Helvetica", 16), width=10, command=lambda: opti("s"))
deck.place(x=183, y=300)
img.place(x=183, y=700)
cash.place(x=95, y=850)
stay.place(x=178, y=500)

card1 = Label(root, image=card1i)
card2 = Label(root, image=card2i)
card3 = Label(root, image=card3i)
card4 = Label(root, image=card4i)
card5 = Label(root, image=card5i)
card1.image = card1i
card2.image = card2i
card3.image = card3i
card4.image = card4i
card5.image = card5i
card1.place(x=903, y=650)
card2.place(x=960, y=562)
card3.place(x=1017, y=474)
card4.place(x=1074, y=386)
card5.place(x=1137, y=298)
card1.place_forget()
card2.place_forget()
card3.place_forget()
card4.place_forget()
card5.place_forget()

dc1 = Label(root, image=dc1i)
dc2 = Label(root, image=dc2i)
dc3 = Label(root, image=dc3i)
dc4 = Label(root, image=dc4i)
dc1.image = dc1i
dc2.image = dc2i
dc3.image = dc3i
dc4.image = dc4i
dc1.place(x=640, y=75)
dc2.place(x=800, y=75)
dc3.place(x=960, y=75)
dc4.place(x=1120, y=75)
dc1.place_forget()
dc2.place_forget()
dc3.place_forget()
dc4.place_forget()

beta = Label(root, text="$0", font=("Helvetica", 16), width=10)
bet = Button(root, image=chip, command=lambda: betopti("d"))
bet.image = chip
bet.place(x=903, y=850)
beta.place(x=900, y=980)

comment = Label(root, text="Welcome, please place a bet to play!", font=("Helvetica", 16), width=100)
comment.place(x=900, y=1015)

betop1 = Button(root, text="+100", font=("Helvetica", 16), width=5, command=lambda: betopti("+100"))
betop2 = Button(root, text="+50", font=("Helvetica", 16), width=5, command=lambda: betopti("+50"))
betop3 = Button(root, text="+10", font=("Helvetica", 16), width=5, command=lambda: betopti("+10"))
betop4 = Button(root, text="-10", font=("Helvetica", 16), width=5, command=lambda: betopti("-10"))
betop1.place(x=700, y=980)
betop3.place(x=560, y=980)
betop2.place(x=630, y=980)
betop4.place(x=490, y=980)
betops = Label(root, text="Bet Options", font=("Helvetica", 16), width=20)
betops.place(x=508, y=930)

xe = threading.Thread(target=mainfunc)
xe.start()

root.mainloop()
import tkinter as tk
import turtle as tu
from random import randint

# -------------------------------------------------------------------------------------2nd window


def victoryr(winner):

    vicr = tk.Tk()
    vicr.title('Order Fight!')
    vicr.geometry('1200x600')

    canvas1 = tk.Canvas(vicr)
    canvas1.place(relx=0, rely=0, relwidth=1, relheight=1)

    image = tk.PhotoImage(file="pic/picG.png")
    labe2 = tk.Label(canvas1, image=image)
    labe2.place(relx=0, rely=0, relwidth=1, relheight=1)

    if winner == spee1:
        labe3 = tk.Label(canvas1, text=(spee1 + ' Wins!!!!!'), font=("Courier", 20), bg='chocolate')
        labe3.place(relx=0.35, rely=0.1, relwidth=0.3, relheight=0.1)

        labe4 = tk.Label(canvas1, text=(spee2 + ',You \'ve to open!'), font=("Courier", 20), bg='chocolate')
        labe4.place(relx=0.45, rely=0.3, relwidth=0.3, relheight=0.1)
    else:
        labe3 = tk.Label(canvas1, text=(spee2 + ' Wins!!!!!'), font=("Courier", 20), bg='chocolate')
        labe3.place(relx=0.35, rely=0.1, relwidth=0.3, relheight=0.1)

        labe4 = tk.Label(canvas1, text=(spee1 + ',You \'ve to open!'), font=("Courier", 20), bg='chocolate')
        labe4.place(relx=0.45, rely=0.3, relwidth=0.3, relheight=0.1)

    vicr.mainloop()


def turtles():
    global spee1
    global spee2
    spe1 = rentry.get()
    spe2 = bentry.get()
    spee1 = spe1
    spee2 = spe2
    maine.destroy()
    dist1 = 0
    dist2 = 0

    tur0 = tu.Turtle()
    tur0.speed(20)

    tur0.penup()
    tur0.goto(-300, 200)

    for step in range(31):
        tur0.write(step, align='center')
        tur0.right(90)
        tur0.forward(20)
        tur0.pendown()
        tur0.forward(200)
        tur0.penup()
        tur0.backward(220)
        tur0.left(90)
        tur0.forward(20)

    # ------------------------------------------------------------------------------------tur1

    tur1 = tu.Turtle()
    tur1.color('red')
    tur1.shape('turtle')
    tur1.speed(1)

    tur1.penup()
    tur1.goto(-300, 100)
    tur1.pendown()

    # ----------------------------------------------------------------------------------------tur2

    tur2 = tu.Turtle()
    tur2.color('blue')
    tur2.shape('turtle')
    tur2.speed(1)

    tur2.penup()
    tur2.goto(-300, 70)
    tur2.pendown()

    # -----------------------------------------------------------------------------------------run
    for turn in range(180):
        rad1 = randint(1, 5)
        dist1 += rad1
        tur1.forward(rad1)

        rad2 = randint(1, 5)
        dist2 += rad2
        tur2.forward(rad2)

    if dist1 > dist2:
        tu.bye()
        victoryr(spee1)
    else:
        tu.bye()
        victoryr(spee2)


def main():
    global maine
    global rentry
    global bentry

    maine = tk.Tk()
    maine.title('Order Fight!')
    maine.geometry('1200x600')

    canvas1 = tk.Canvas(maine)
    canvas1.place(relx=0, rely=0, relwidth=1, relheight=1)

    image = tk.PhotoImage(file="pic/picG.png")
    label = tk.Label(canvas1, image=image)
    label.place(relx=0, rely=0, relwidth=1, relheight=1)

    label = tk.Label(canvas1, text='Select Your Turtle!!!', font=("Courier", 20), bg='chocolate')
    label.place(relx=0.35, rely=0.1, relwidth=0.3, relheight=0.1)

    label2 = tk.Label(canvas1, text='Red Turtle:', font=("Courier", 15), bg='chocolate')
    label2.place(relx=0.05, rely=0.2, relwidth=0.2, relheight=0.1)

    rentry = tk.Entry(canvas1, font=("Courier", 25), bg='peru')
    rentry.place(relx=0.25, rely=0.2, relwidth=0.2, relheight=0.1)

    label3 = tk.Label(canvas1, text='Blue Turtle', font=("Courier", 15), bg='chocolate')
    label3.place(relx=0.55, rely=0.2, relwidth=0.2, relheight=0.1)

    bentry = tk.Entry(canvas1, font=("Courier", 25), bg='peru')
    bentry.place(relx=0.75, rely=0.2, relwidth=0.2, relheight=0.1)

    button = tk.Button(canvas1, text='Run!', font=("Courier", 30), bg='chocolate', command=turtles)
    button.place(relx=0.82, rely=0.80, relwidth=0.15, relheight=0.15)

    maine.mainloop()


# -------------------------------------------------------------------------------------1st window


def kill():
    errors.destroy()


def error():
    global errors

    errors = tk.Tk()
    errors.geometry('200x100')
    errors.title('error')

    labeler = tk.Label(errors, text='Error')
    labeler.place(relx=0, rely=0, relwidth=1, relheight=0.4)

    buttoner = tk.Button(errors, text="ok", command=kill)
    buttoner.place(relx=0.45, rely=0.7, relwidth=0.2, relheight=0.2)


def con(*args):
    peo = entry.get()
    if peo == '1':
        pass
    elif peo == '2':
        window1.destroy()
        main()
    else:
        error()


def win1():
    global window1
    global entry

    window1 = tk.Tk()
    window1.geometry('1200x600')
    window1.title('Order Fight!')

    canvas = tk.Canvas(window1)
    canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

    image = tk.PhotoImage(file="pic/picG.png")
    label = tk.Label(canvas, image=image)
    label.place(relx=0, rely=0, relwidth=1, relheight=1)

    label = tk.Label(canvas, text='Welcome to Order Fight', font=("Courier", 20), bg='chocolate')
    label.place(relx=0.35, rely=0.1, relwidth=0.3, relheight=0.1)

    label2 = tk.Label(canvas, text='Order for?', font=("Courier", 15), bg='chocolate')
    label2.place(relx=0.35, rely=0.2, relwidth=0.2, relheight=0.1)

    entry = tk.Entry(canvas, font=("Courier", 25), bg='peru')
    entry.bind("<Return>", con)
    entry.place(relx=0.55, rely=0.2, relwidth=0.1, relheight=0.1)

    window1.mainloop()


win1()

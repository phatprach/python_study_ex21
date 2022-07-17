# TK document : https://tkdocs.com/tutorial/widgets.html

from tkinter import *

main_win = Tk()

def left_click(event):
    h = float(text_box_h.get())
    w = float(text_box_w.get())
    # print(w/((h/100)**2))
    r = w/((h/100)**2)
    if r > 30:
        label_r.configure(text = "your BMI is %.2f, Very fat" % r)
    elif r >= 25 and r <= 29.9:
        label_r.configure(text = "your BMI is %.2f, Fat" % r)
    elif r >= 23 and r <= 24.9:
        label_r.configure(text = "your BMI is %.2f, Over weight" % r)
    elif r >= 18.5 and r <= 22.9:
        label_r.configure(text = "your BMI is %.2f, Balance body" % r)
    elif r < 18.5:
        label_r.configure(text = "your BMI is %.2f, Too thin" % r)

label_h = Label(main_win, text = "Height (cm) : ").grid(row=0, column=0)
text_box_h = Entry(main_win)
text_box_h.grid(row=0, column=1)

label_w = Label(main_win, text = "Weight (kg) : ").grid(row=1, column=0)
text_box_w = Entry(main_win)
text_box_w.grid(row=1, column=1)

button = Button(main_win, text = "Calculate BMI")
button.bind("<Button-1>", left_click)
button.grid(row=2, column=0)

label_r = Label(main_win, text = "result")
label_r.grid(row=2, column=1)

main_win.mainloop()
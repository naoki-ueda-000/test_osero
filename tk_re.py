
from tkinter import *

# ボタンイベント関数
def btn_1():
    pass
def btn_2():
    pass
def btn_3():
    pass
def btn_4():
    pass
def btn_5():
    pass
def btn_6():
    pass

# メインウィンドウの設定
root = Tk()
root.title("Tk window")
root.geometry()

# Frameを設定
frame_1 = Frame(root, bd=4, relief=GROOVE)
frame_2 = Frame(root, bd=4, relief=GROOVE)
frame_3 = Frame(root, bd=4, relief=GROOVE)

# ボタンwidgetを設定
button_1 = Button(frame_1, text='Button1-a', command=btn_1)
button_2 = Button(frame_1, text='Button2-bb', command=btn_2)
button_3 = Button(frame_1, text='Button3-ccc', command=btn_3)
button_4 = Button(frame_2, text='Button4-dddd', command=btn_4)
button_5 = Button(frame_2, text='Button5-eeeee', command=btn_5)
button_6 = Button(frame_3, text='Button6-ffffff', command=btn_6)

# widgetの配置を設定
frame_1.grid(row=0, column=0, columnspan=2, sticky=W + E)
frame_2.grid(row=1, column=0)
frame_3.grid(row=1, column=1, sticky=N + S)
button_1.pack(fill=X)
button_2.pack(fill=X)
button_3.pack(fill=X)
button_4.pack(fill=X)
button_5.pack(fill=X)
button_6.pack(fill=X)

root.mainloop()

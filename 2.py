from tkinter import *
import random
import webbrowser

data1 = ['醬油','味噌','豚骨','蔥']
going = True
run = False
def lottery_roll(var1):
  global going
  show = random.choice(data1)
  var1.set(show)
  if going:
    window.after(50,lottery_roll,var1)
  else:
    going = True
    return

def ramen(var1):
  global run
  if run:
    return
  run = True
  lottery_roll(var1)
  
def stop():
  global going,run
  if run:
    going = False
    run = False

def window2():
    window2 = Tk()
    window2.geometry("300x200")
    label = Label(window2, text = "goodbye" ,font = ("Snap ITC",25))
    label.pack()
    window2.mainloop()
    

window = Tk()
window.geometry('600x400')
window.title('拉麵大師')
window["bg"] = "#FFFFBB"
var1 = StringVar(value='拉麵大師')
show_label1 = Label(window,textvariable=var1,width=17,height=3,bg='#BFEFFF',font='楷體 -40 bold')
show_label1.place(x=100,y=20)

button1 = Button(window,text='隨機品項',height=4,width=8,command=lambda: ramen(var1),font=8)
button1.place(x=70,y=175)
button2 = Button(window,text='隨機店家',height=4,width=8,command=lambda: store(var1),font=8)
button2.place(x=70,y=290)
button3 = Button(window,text="台灣拉麵地圖",height=4,width=8,font=1,command=lambda:webbrowser.open("https://www.google.com/maps/d/viewer?mid=1WCW-1ocsYYbQjBVOOgx5dZEyvmE&hl=en_US&ll=25.062800461952587%2C121.51292114152841&z=12&fbclid=IwAR3d-Gq3hAycEtM-hVnD1UHDTo9GrSyKk5iVtbbWPC07Cef2MMv9Ee41ihY"))
button3.place(x=460,y=290)
button4 = Button(window,text='隨機湯頭',height=4,width=8,font=("Solid Edge ISO CE",15))
button4.place(x=200,y=175)
button5 = Button(window,text='隨機小菜',height=4,width=8,font=8)
button5.place(x=200,y=290)
button6 = Button(window,text='',height=4,width=8,font=8)
button6.place(x=330,y=175)
button7 = Button(window,text='',height=4,width=8,font=8)
button7.place(x=330,y=290)

#button8 = Button(window,text='停止',height=4,width=8,font=4,command=lambda: stop())
#button8.place(x=460,y=175)
#button9 = Button(windowl, text = "OK",font = ("Solid Edge ISO CE",15), command = window2)
#button9["fg"] = "gray"



window.mainloop()

from tkinter import *
from PIL import ImageTk,Image
from tkinter.ttk import*
import random
a=Tk()
a.title("Oggy Shoes")

#bg
c3=ImageTk.PhotoImage(Image.open("bg2.png"))
ltt3=Label(a,image=c3)
ltt3.place(x=5,y=0)
c4=ImageTk.PhotoImage(Image.open("bg2.png"))
ltt4=Label(a,image=c4)
ltt4.place(x=5,y=632)


#invisible label group
il1=Label(a,text="",font=("Copperplate Gothic Bold",25))
il1.place(x=1180,y=10)

il2=Label(a,text="",font=("Copperplate Gothic Bold",25))
il2.place(x=1100,y=200)

vl1=Label(a,text="15% OFF ",font=("Harlow Solid Italic",28))
vl1.place(x=900,y=450)
vl2=Label(a,text="for purchases above 7000/-",font=("Harlow Solid Italic",28))
vl2.place(x=950,y=500)




#function
def item1():
    var1=int(click1.get())
    var2=int(click2.get())
    var3=int(click3.get())
    var4=int(click4.get())
    var5=int(click5.get())
    var6=int(click6.get())
    t=var1+var2+var3+var4+var5+var6
    il1.configure(text=""+str(t))
    m1=var1*2799
    m2=var2*1499
    m3=var3*2799
    m4=var4*1799
    m5=var5*2299
    m6=var6*1899
    m=m1+m2+m3+m4+m5+m6
    if(m>=7000):
        messagebox.showinfo("Discount!","Congratulations!!!\nYou have just received 15% discount")
        il2.configure(text=""+str(m)+'/-')
        m=m-(m*15/100)     
        il3=Label(a,text=""+str(m)+'/-',font=("Copperplate Gothic Bold",25))
        il3.place(x=1100,y=290)
        def checkout():
            messagebox.showinfo("Checkout","Your Payment has been received.\nThanks for shopping with Oggy.")
        cb=Button(a,text="PAY",command=checkout)
        cb.place(x=1000,y=370)
        
        
    else:
        il2.configure(text=""+str(m)+'/-')
        il3=Label(a,text=""+str(m)+'/-',font=("Copperplate Gothic Bold",25))
        il3.place(x=1100,y=290)
        def checkout():
            messagebox.showinfo("Checkout","Your Payment has been received.\nThanks for shopping with Oggy.")
            
        cb=Button(a,text="PAY",command=checkout)
        cb.place(x=1000,y=370)
        

def e_egg():
    v9=random.randint(100000,999999)
    messagebox.showinfo("Easter Egg!!","#OgGyStOrE\n\nUpload the below code in Facebook tagging us and get a pair of shoes for free!!\n\nCode:"+str(v9))
jb1=Button(a,text='Click',command=e_egg) 
jb1.place(x=1290,y=680)  





#img placing
c11=ImageTk.PhotoImage(Image.open("cu1.png"))
ltt11=Label(a,image=c11)
ltt11.place(x=1130,y=640)

c7=ImageTk.PhotoImage(Image.open("og1.png"))
ltt7=Label(a,image=c7)
ltt7.place(x=950,y=100)


c9=ImageTk.PhotoImage(Image.open("ad.png"))
ltt9=Label(a,image=c9)
ltt9.place(x=950,y=280)

c1=ImageTk.PhotoImage(Image.open("cart.png"))
ltt1=Label(a,image=c1)
ltt1.place(x=1250,y=0)

c2=ImageTk.PhotoImage(Image.open("total.png"))
ltt2=Label(a,image=c2)
ltt2.place(x=1000,y=200)

img1=ImageTk.PhotoImage(Image.open("sh1.png"))
lt1=Label(a,image=img1)
lt1.place(x=0,y=0)

img2=ImageTk.PhotoImage(Image.open("sh2.png"))
lt2=Label(a,image=img2)
lt2.place(x=300,y=0)

img3=ImageTk.PhotoImage(Image.open("sh3.png"))
lt3=Label(a,image=img3)
lt3.place(x=600,y=0)

img4=ImageTk.PhotoImage(Image.open("sh4.png"))
lt4=Label(a,image=img4)
lt4.place(x=0,y=350)

img5=ImageTk.PhotoImage(Image.open("sh5.png"))
lt5=Label(a,image=img5)
lt5.place(x=300,y=350)

img6=ImageTk.PhotoImage(Image.open("sh6.png"))
lt6=Label(a,image=img6)
lt6.place(x=600,y=350)

#textplacing
l1=Label(a,text="1699/-",font=("High Tower Text",15))
l1.place(x=90,y=230)

options1=["0","1","2","3","4","5"]
click1=StringVar()
click1.set("Qty")
drop1=OptionMenu(a,click1,*options1)
drop1.place(x=50,y=280)

b1=Button(a,text="Add to Cart",command=item1)
b1.place(x=50,y=310)

l2=Label(a,text="2399/-",font=("High Tower Text",15))
l2.place(x=410,y=230)

options2=["0","1","2","3","4","5"]
click2=StringVar()
click2.set("Qty")
drop2=OptionMenu(a,click2,*options2)
drop2.place(x=370,y=280)

b2=Button(a,text="Add to Cart",command=item1)
b2.place(x=370,y=310)


l3=Label(a,text="2799/-",font=("High Tower Text",15))
l3.place(x=730,y=230)


options3=["0","1","2","3","4","5"]
click3=StringVar()
click3.set("Qty")
drop3=OptionMenu(a,click3,*options3)
drop3.place(x=690,y=280)

b3=Button(a,text="Add to Cart",command=item1)
b3.place(x=690,y=310)


l4=Label(a,text="1799/-",font=("High Tower Text",15))
l4.place(x=90,y=560)
options4=["0","1","2","3","4","5"]
click4=StringVar()
click4.set("Qty")
drop4=OptionMenu(a,click4,*options4)
drop4.place(x=50,y=615)
b4=Button(a,text="Add to Cart",command=item1)
b4.place(x=50,y=650)


l5=Label(a,text="2299/-",font=("High Tower Text",15))
l5.place(x=410,y=560)
options5=["0","1","2","3","4","5"]
click5=StringVar()
click5.set("Qty")
drop5=OptionMenu(a,click5,*options5)
drop5.place(x=370,y=615)
b5=Button(a,text="Add to Cart",command=item1)
b5.place(x=370,y=650)


l6=Label(a,text="1899/-",font=("High Tower Text",15))
l6.place(x=730,y=560)
options6=["0","1","2","3","4","5"]
click6=StringVar()
click6.set("Qty")
drop6=OptionMenu(a,click6,*options6)
drop6.place(x=690,y=615)
b6=Button(a,text="Add to Cart",command=item1)
b6.place(x=690,y=650)



a.mainloop()

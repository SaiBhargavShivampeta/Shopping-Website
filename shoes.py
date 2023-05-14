from tkinter import *
from PIL import ImageTk,Image
window = Tk()
window.title("OGGY LOGIN PAGE")
c3=ImageTk.PhotoImage(Image.open("bg2.png"))
ltt3=Label(window,image=c3)
ltt3.place(x=5,y=0)
c4=ImageTk.PhotoImage(Image.open("bg2.png"))
ltt4=Label(window,image=c4)
ltt4.place(x=5,y=632)


#labels

l2=Label(window,text="Login Page",bg="light yellow",fg="black",font=("Copperplate Gothic Bold",30))
l2.place(x=700,y=60,anchor="center")
l3=Label(window,text="Username",bg="light yellow",font=("Elephant",20))
l3.place(x=600,y=200,anchor="center")
l3=Label(window,text="Password",bg="light yellow",font=("Elephant",20))
l3.place(x=600,y=280,anchor="center")
e1=Entry(window,width=10,bg="light yellow",font=("Elephant",20))
e1.place(x=800,y=200,anchor="center")
e2=Entry(window,width=10,bg="light yellow",font=("Elephant",20),show="*")
e2.place(x=800,y=280,anchor="center")




def click():
    pwd=e2.get()
    if pwd=="oggy":
        import s_main
    else:
        messagebox.showinfo("ALERT","Invalid Password !!!")

b1=Button(window,text="LOGIN",bg="light yellow",font=("Elephant",15),command=click)
b1.place(x=700,y=400,anchor="center")


window.mainloop()
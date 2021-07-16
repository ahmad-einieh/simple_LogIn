from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

class Login_System:
    def __init__(self,root):
        self.root = root
        self.root.title("login system")
        self.root.geometry("1350x700+0+0")

        # all image
        self.bg_icon=ImageTk.PhotoImage(file="bg1.png")
        self.user_icon=PhotoImage(file="icons8-user-male-24.png")
        self.pass_icon = PhotoImage(file="icons8-user-locked-32.png")
        self.logo_icon = PhotoImage(file="login-icon-3057.gif")
        #
        self.user=StringVar()
        self.password = StringVar()

        #

        bg_label = Label(self.root, image=self.bg_icon).pack()

        title = Label(self.root,text="Login System",
                      font=("times new roman",40,"bold"),
                      bg="yellow",fg="red",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        login_fram = Frame(self.root,bg="white")
        login_fram.place(x=400,y=150)
        logo_label = Label(login_fram,image=self.logo_icon,bd=0)
        logo_label.grid(row=0,columnspan=2,pady=20)
        lableuser=Label(login_fram,text="username",
                        image=self.user_icon,compound=LEFT,
                        font=("times new roman",20,"bold"),bg="white")
        lableuser.grid(row=1,column=0,padx=1,pady=1)
        textuser=Entry(login_fram,bd=5,textvariable=self.user,relief=GROOVE,font=(" ",15))
        textuser.grid(row=1,column=1,padx=20)

        lablepass = Label(login_fram, text="password",
                          image=self.pass_icon, compound=LEFT,
                          font=("times new roman", 20, "bold"), bg="white")
        lablepass.grid(row=2, column=0, padx=1, pady=1)

        textpass = Entry(login_fram, bd=5,textvariable=self.password,show="*", relief=GROOVE, font=(" ", 15))
        textpass.grid(row=2, column=1, padx=20)

        butlogin= Button(login_fram,text="login",width=15,command=self.login,font=("times new roman",14,"bold"),bg="yellow",fg="red")
        butlogin.grid(row=3, column=1, pady=10)

    def login(self):
        if self.user.get() == "" or self.password.get() == "":
            messagebox.showerror("error"," all field is required")
        elif self.user.get() == "ahmad" and self.password.get() == "ahmad":
            messagebox.showinfo("successful",f"welcome {self.user.get()}")
        else:
            messagebox.showerror("error","wrong username or password")


root = Tk()
obj = Login_System(root)
root.mainloop()

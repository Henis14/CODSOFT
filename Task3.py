from tkinter import *
import string 
import random

def generator():
    small_alphabets=string.ascii_lowercase 
    capital_alphabets=string.ascii_uppercase 
    numbers=string.digits 
    special_charecters=string.punctuation

    all=small_alphabets+capital_alphabets+numbers+special_charecters
    password_length=int(lengthbox.get())

    if choice.get()==1:
        passfield.insert(0,random.sample(small_alphabets,password_length))

    if choice.get()==2:
        passfield.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))

    if choice.get()==3:
        passfield.insert(0,random.sample(all,password_length))

    # password=random.sample(all, password_length) 
    # passfield.insert(0,password)

root=Tk()
root.config(bg='#a1887f')
choice=IntVar()
Font=('arial',15,'bold')
password=Label(root,text='Password Generator',font=('times new roman',20,'bold'),bg='#4e342e',fg='white')
password.grid(pady=10)

weakrb=Radiobutton(root,text="WEAK",value=1,variable=choice,font=Font)
weakrb.grid(pady=5)

mediumrb=Radiobutton(root,text="MEDIUM",value=2,variable=choice,font=Font)
mediumrb.grid(pady=5)

strongrb=Radiobutton(root,text="STRONG",value=3,variable=choice,font=Font)
strongrb.grid(pady=5)

lengthlabel=Label(root,text='Password length',font=Font,bg='#a1887f',fg='#4e342e')
lengthlabel.grid(pady=5)

lengthbox=Spinbox(root,from_=6,to_=18,width=10,font=Font)
lengthbox.grid(pady=5)

generatebutton=Button(root,text='Generate',font=Font,bg='#4e342e',fg='white',command=generator)
generatebutton.grid(pady=5)

passfield=Entry(root,width=25,bd=2,font=Font)
passfield.grid()

root.mainloop()
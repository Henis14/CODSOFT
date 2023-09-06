from tkinter import *
from tkinter import ttk

class task1:
    def __init__(self,root):
        self.root=root
        self.root.title("To-do List")
        self.root.geometry('550x550+300+150')
        self.label=Label(self.root,text='MY TO DO LIST',
                         font="cursive, 30 italic bold",width=10,bd=15,bg='#e4a199',fg='black')
        self.label.pack(side='top',fill=BOTH)


        self.label2=Label(self.root,text='Add from here',
                         font='cursive,20',width=10,bd=10,bg='black',fg='#e4a199')
        self.label2.place(x=40,y=90)


        self.label3=Label(self.root,text='Things to do',
                         font='cursive,20',width=10,bd=10,bg='black',fg='#e4a199')
        self.label3.place(x=320,y=90)


        self.main_text=Listbox(self.root,height=15,bd=5,width=26,font="cursive,25")
        self.main_text.place(x=240,y=170)


        self.text=Text(self.root,bd=5,height=2,width=13,font="ariel, 20 bold")
        self.text.place(x=10,y=170)



        def add():
            content=self.text.get(1.0,END)
            self.main_text.insert(END,content)
            result = open("tasks.txt","a")
            print(result.read())
            #with open('tasks.txt','a') as file:
            result.write(content)
            result.seek(0)
            result.close()
            self.text.delete(1.0,END)

        def delete():
            delete_= self.main_text.curselection()
            look=self.main_text.get(delete_)
            with open('tasks.txt','r+') as f:
                new_f=f.readlines()
                f.seek(0)
                for line in new_f:
                    item=str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete_)


            result = open("tasks.txt","r")
            print(result.read())
        # with open("tasks.txt","r") as file:
            read=result.readlines()
            for i in read():
                ready=i.split()
                self.main_text.insert(END,ready)
            result.close()


        self.button=Button(self.root,text="Insert",font="sarif, 20 bold",
                           width=6,bd=5,bg='black',fg='#e4a199',command=add)
        self.button.place(x=50,y=280)

        self.button1=Button(self.root,text="Remove",font="sarif, 20 bold",
                           width=6,bd=5,bg='black',fg='#e4a199',command=delete)
        self.button1.place(x=50,y=360)


def main():
    root=Tk()
    ui=task1(root)
    root.mainloop()

if __name__ == "__main__":
    main()

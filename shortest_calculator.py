from tkinter import *

root = Tk()
root.title('Shortest Calaulator')

root.minsize(270,600)
root.maxsize(270,600)

def qns(which_num_to_add):
	qn.set((qn.get())+which_num_to_add)

def answer():
	qn.set(eval((qn.get())))

def create(frame_name,command_name):
	Button(frame_name,
	text=""+command_name,
	bg="white",
	fg="black",
	borderwidth=0,
	pady=19,
	padx=29,
	font="impact 20 bold",
	command=lambda:(qns(''+command_name))).pack(side=LEFT)

def clear():
	qn.set((qn.get()[0:-1]))

def next(text,command_name,frame_name):
	Button(frame_name,
	text=""+text,
	bg="white",
	fg="black",
	borderwidth=0,
	pady=19,
	padx=29,
	font="impact 20 bold",
	command=command_name).pack(side=LEFT)

def ultra():
	qn.set('')

qn = StringVar()
qn.set('')

l1 = Label(textvariable=qn,bg="black",fg="white",font="comicsansms 35 bold",state=DISABLED)
l1.pack()


f1 = Frame(borderwidth=10,bg="black")
f2 = Frame(borderwidth=10,bg="black")
f3 = Frame(borderwidth=10,bg="black")
f4 = Frame(borderwidth=10,bg="black")
f5 = Frame(borderwidth=10,bg="black")
f6 = Frame(borderwidth=10,bg="black")

create(f1,'1')
create(f1,'2')
create(f1,'3')

create(f2,'4')
create(f2,'5')
create(f2,'6')

create(f3,'7')
create(f3,'8')
create(f3,'9')

create(f4,'0')
create(f4,'*')
create(f4,'-')

create(f5,'/')

Button(f5,
	text="=",
	bg="white",
	fg="black",
	borderwidth=0,
	pady=19,
	padx=29,
	font="impact 20 bold",
	command=answer).pack(side=LEFT)

next('CC',clear,f5)
next('C',ultra,f6)


f1.pack(anchor="w")
f2.pack(anchor="w")
f3.pack(anchor="w")
f4.pack(anchor="w")
f5.pack(anchor="w")
f6.pack(anchor="w")

root.config(bg="black")
root.mainloop()

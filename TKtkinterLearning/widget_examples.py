from tkinter import *

window = Tk()
window.title("Tkinter Python")
window.minsize(600,600)
window.config(padx=50,pady=50)


label = Label(text="my label")
label.config(bg="black")
label.config(fg="white")
label.config(padx=10,pady=10)
label.pack()

def button_clicked():

    print(text.get("1.1", END))

button = Button(text="Button",command=button_clicked)
button.pack()

entry = Entry(width=20)
entry.pack()

text = Text(width=30,height=15)
text.focus()
text.pack()

# scale
def scale_selected(value):
    print(value)

my_scale = Scale(from_=0,to=50, command=scale_selected)
my_scale.pack()

# spinbox
def spinbox_selected():
    print(my_spinbox.get())

my_spinbox = Spinbox(from_=0, to=60, command=spinbox_selected)
my_spinbox.pack()

# checkbox
def check_button_selected():
    print(check_state.get())

check_state = IntVar()
my_checkbutton = Checkbutton(text="check", variable=check_state, command=check_button_selected)
my_checkbutton.pack()


# radio button

def radio_button_selected():
    print(radio_check_state.get())

radio_check_state = IntVar()
my_radiobutton = Radiobutton(text="1. option", value=10, variable=radio_check_state, command=radio_button_selected)
my_radiobutton.pack()
my_radiobutton2 = Radiobutton(text="2. option", value=20, variable=radio_check_state, command=radio_button_selected)
my_radiobutton2.pack()


# listbox
def listbox_selected(event):
    print(my_listbox.get(my_listbox.curselection()))


my_listbox = Listbox()
name_list = ["elif", "mustafa", "çil"]
for i in range(len(name_list)):
    my_listbox.insert(i,name_list[i])

my_listbox.bind('<<ListboxSelect>>', listbox_selected)
my_listbox.pack()

window.mainloop()
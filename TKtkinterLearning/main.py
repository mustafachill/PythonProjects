import tkinter

def click_button():
    user_input = my_entry.get()
    print(user_input)

# window
window = tkinter.Tk()
window.title("Python Tkinter")
window.minsize(500,500)

# label
my_label = tkinter.Label(text="this is a label", bg="black", fg="pink")
my_label.config(fg="blue", font=('Arial', 30, "italic"))
my_label.grid(row=1, column=0)
my_label.config(fg="red")

# button
my_button = tkinter.Button(text="this is a button", command=click_button)
#my_button.pack()
my_button.grid(row=1, column=1)
# entry
my_entry = tkinter.Entry(width=50)
#my_entry.place(x=42,y=300)



#
#
# MAINLOOP
window.mainloop()
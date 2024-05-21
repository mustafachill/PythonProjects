from tkinter import *

window = Tk()
window.minsize(600,400)
window.title("BMI CALCULATOR")
window.config(padx=30,pady=30)
person_BMI_info = 0
# for creating label
def create_label(text):
    label = Label(text=text, fg="black", font=('Arial',20))
    label.pack()
    return label

# for creating entrance
def create_entrance():
    entry = Entry()
    entry.pack()
    return entry

# for creating button
def create_button(command):
    button = Button(text="Send info", command=command)
    button.pack()

# for getting users input and print
def get_users_info(entry1, entry2):
    info_bw = 0
    info_hg = 0
    global person_BMI_info
    try:info_bw = int(entry1.get())
    except: print_result_variable.config(text="Please enter your body weight")

    try:info_hg = int(entry2.get())
    except: print_personal_result.config(text="Please enter your body height")
    person_BMI_info = calculate_BMI(info_bw,info_hg)
    print_result(person_BMI_info)

# calculating BMI
def calculate_BMI(info_bw,info_hg):
    value = 0
    try: value = int(info_bw) / (int(info_hg) / 100) ** 2
    except: pass
    return value

def print_result(person_BMI_info):
    global print_result_variable
    if person_BMI_info > 0:
        print_result_variable.config(text=f"Your BMI Score is {person_BMI_info}")
        if person_BMI_info <= 18.4:
            print_personal_result.config(text="You are underweight")
        elif person_BMI_info >= 18.5 and person_BMI_info <= 24.9:
            print_personal_result.config(text="You are good")
        elif person_BMI_info >= 25.0 and person_BMI_info <= 39.9:
            print_personal_result.config(text="You should lose some weight")
        elif person_BMI_info >= 40:
            print_personal_result.config(text="You are an obese")


''' UI/UX PART '''
# height part
create_label("Please enter your height:")
entry_for_height = create_entrance()

# bodyweight part
create_label("Please enter your bodyweight:")
entry_for_bodyweight = create_entrance()

# sent info and print info part
create_button(lambda: get_users_info(entry_for_bodyweight, entry_for_height))
print_result_variable = create_label("")
print_personal_result = create_label("")
mainloop()
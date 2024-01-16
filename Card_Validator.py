# This is a new comment 
# this is first version 
from tkinter import *
def validate(card_number):
    card_list = list(card_number)
    # get the odd number index sum
    odd_sum = 0
    even_list = []
    for (index, val) in enumerate(card_list):
        if not index % 2 == 0:
            odd_sum += int(val)
        else:
            # double the even the numbers
            even_list.append(2 * int(val))
    double_string = ""
    for x in even_list:
        double_string += str(x)
    even_list = list(double_string)
    even_sum = 0
    for x in even_list:
        even_sum += int(x)
    sum = even_sum + odd_sum
    if sum % 10 == 0:
        result.config(text="Valid Credit Card")
    else:
        result.config(text="Invalid Credit Card")





root = Tk()
root.geometry("400x400")
label = Label(root, text="Card Number : ")
label.grid(row=0,column=0)
card_entry = Entry(root)
card_entry.grid(row=0,column=1)
button = Button(root,text="Validate", command= lambda:validate(card_entry.get()))
button.grid(row=1,column=1)
result = Label(root, fg= "red", font=("Arial", 20))
result.grid(row=2,column=1)
root.mainloop()
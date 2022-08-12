from tkinter import *

windows = Tk()
windows.title(string='Mile To Kilometers')
# windows.minsize(width=300, height=150)
windows.config(padx=30,pady=25)
# labels
#label 1
label = Label(text='miles')
label.grid(column=2,row=0)
label.config(padx=5,pady=5)
#label 2
label_2 = Label(text="is equal to")
label_2.grid(column=0,row=1)
#label 3
label_3 = Label(text="Km")
label_3.grid(column=2,row=1)
label_3.config(padx=5,pady=5)
#label 4
result_label = Label(text="0")
result_label.grid(column=1,row=1)
# entry
entry = Entry(width=10)
entry.grid(column=1,row=0)
# button
button = Button(text="Calculate",command=converter)
button.grid(column=1,row=3)


def converter():
    miles = entry.get()
    kilometers = round(int(miles) * 1.60934,1)
    result_label.config(text=f"{kilometers}")

windows.mainloop()
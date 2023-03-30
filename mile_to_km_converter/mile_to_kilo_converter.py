from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=10, pady=20)


def miles_to_km():
    miles = float(miles_input.get())
    kilometers = round(miles * 1.609)
    km.config(text=kilometers)


is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

miles_input = Entry(width=10)
print(miles_input.get())
miles_input.grid(column=1, row=0)

km = Label(text="")
km.grid(column=1, row=1)

calculate_button = Button(text="Click Me", command=miles_to_km)
calculate_button.grid(column=1, row=2)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)











window.mainloop()
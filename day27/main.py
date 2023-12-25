import tkinter

window = tkinter.Tk()
window.title("GUI Program")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

def button_clicked():
    get_input = float(input.get())
    km = round(get_input * 1.609, 1)
    kilometer_result.config(text=f"{km}")


miles = tkinter.Label(text="Miles")
miles.grid(row=0, column=2)

km = tkinter.Label(text="Km")
km.grid(row=1, column=2)

is_equal_to = tkinter.Label(text="is equal to")
is_equal_to.grid(row=1, column=0)

kilometer_result = tkinter.Label(text="0")
kilometer_result.grid(row=1, column=1)

button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)


input = tkinter.Entry()
input.grid(row=0, column=1)


window.mainloop()
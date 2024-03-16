import tkinter as tk


def get_text(text, on=False):
    if on:
        # enable text widget for editing
        result_text.config(state="normal")
        # clear previous content
        result_text.delete("1.0", tk.END)
        # insert new text
        result_text.insert(tk.END, text)
        # disable text widget again to make it read only
        result_text.config(state="disabled")


def start():
    # retrieve text from the entry field
    text = length_entry.get()
    # retrieve the state of the checkbox
    on = checkbox_var.get()
    # call get_text function to display text
    get_text(text, on)


# create the main window
root = tk.Tk()
root.title("Example")

# set initial size
root.geometry("400x300")

# widgets

# label for entry field
length_label = tk.Label(root, text="Enter number")
length_label.pack()

# entry field for user input
length_entry = tk.Entry(root)
length_entry.pack()

# button
button = tk.Button(root, text="Getx Text", command=start)
button.pack()

# checkbox
checkbox_var = tk.BooleanVar(value=True)
checkbox = tk.Checkbutton(root, text="Include special_chars", variable=checkbox_var)
checkbox.pack()

# text widget
result_text = tk.Text(root, wrap="word", height=5, state="disabled")
result_text.pack()

# run the application
root.mainloop()
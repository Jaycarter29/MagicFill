import tkinter as tk
from tkinter import messagebox

def setup_ui():
    def save_data():
        user_data = entry_name.get()
        if user_data:
            messagebox.showinfo('Success', f'Data saved: {user_data}')
            # Logic to save data can be added here
        else:
            messagebox.showwarning('Input Error', 'Please enter a name.')

    def clear_data():
        entry_name.delete(0, tk.END)

    root = tk.Tk()
    root.title('MagicFill - Manage User Data')

    label_name = tk.Label(root, text='Name:')
    label_name.grid(row=0, column=0)

    entry_name = tk.Entry(root)
    entry_name.grid(row=0, column=1)

    button_save = tk.Button(root, text='Save', command=save_data)
    button_save.grid(row=1, column=0)

    button_clear = tk.Button(root, text='Clear', command=clear_data)
    button_clear.grid(row=1, column=1)

    root.mainloop()
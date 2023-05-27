import tkinter as tk
import subprocess
from tkinter import ttk
from tkinter import messagebox


def show_windows():
    def on_continue():
        selected_option = radio_var.get()
        if selected_option == 1:
            root.destroy()
            subprocess.run(['python3', 'average_window.py'])
        elif selected_option == 2:
            root.destroy()
            subprocess.run(['python3', 'manual_search_window.py'])
        elif selected_option == 3:
            root.destroy()
            subprocess.run(['python3', 'two_v_two_window.py'])
        else:
            messagebox.showerror("Error", "Please select an option")

    def on_radio_button_click():
        continue_button.config(state=tk.NORMAL)

    root = tk.Tk()
    root.title("1st Window")

    main_frame = ttk.Frame(root, padding=20)
    main_frame.pack(expand=True, fill=tk.BOTH)

    prompt = ttk.Label(
        main_frame, text="What are you interested to know about the coworkers:")
    prompt.pack()

    radio_var = tk.IntVar()
    radio_frame = ttk.Frame(main_frame)
    radio_frame.pack(fill=tk.X, pady=(20, 10))
    radio1 = ttk.Radiobutton(radio_frame, text="Overall work hours average tab?",
                             variable=radio_var, value=1, command=on_radio_button_click)
    radio1.grid(row=0, column=0, sticky=tk.W)
    radio2 = ttk.Radiobutton(radio_frame, text="Manual average search for a colleague?",
                             variable=radio_var, value=2, command=on_radio_button_click)
    radio2.grid(row=1, column=0, sticky=tk.W)
    radio3 = ttk.Radiobutton(radio_frame, text="2v2 comparison?",
                             variable=radio_var, value=3, command=on_radio_button_click)
    radio3.grid(row=2, column=0, sticky=tk.W)

    button_frame = ttk.Frame(main_frame)
    button_frame.pack(side=tk.BOTTOM, anchor=tk.SE, pady=(20, 0))
    continue_button = ttk.Button(
        button_frame, text="Continue", state=tk.DISABLED, command=on_continue)
    continue_button.grid(row=0, column=0)
    cancel_button = ttk.Button(
        button_frame, text="Cancel", command=root.destroy)
    cancel_button.grid(row=0, column=1)

    root.mainloop()


if __name__ == "__main__":
    show_windows()

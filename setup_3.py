import tkinter as tk
from tkinter import filedialog, ttk
import subprocess
import os

def center_window(root, width=500, height=300):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

def browse_folder():
    global projectPath
    projectPath = filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, projectPath)

def run_composer_install():
    try:
        progress_var.set(0)
        cmd = "composer install"
        subprocess.run(cmd, cwd=projectPath, shell=True)
        status_label.config(text="Command completed!", fg="green")
        for i in range(100):
            progress_var.set(i)
            root.update_idletasks()
        progress_var.set(100)
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}", fg="red")

root = tk.Tk()
root.title("Laravel Composer Installer")
center_window(root)

# Main title
tk.Label(root, text="Laravel Composer Installer", font=("Arial", 16, "bold")).pack(pady=10)

# Project path input
path_frame = tk.Frame(root)
path_frame.pack(pady=10, fill=tk.X, padx=50)

DEFAULT_PATH = os.path.expanduser("C:/laragon/www/okul")
projectPath = DEFAULT_PATH

path_entry = tk.Entry(path_frame, width=35, font=("Arial", 12))
path_entry.insert(0, DEFAULT_PATH)
path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

browse_btn = tk.Button(path_frame, text="Browse", command=browse_folder)
browse_btn.pack(side=tk.RIGHT)

# Composer Install button
btn_install = tk.Button(root, text="Composer Install", command=run_composer_install, font=("Arial", 14), bg="green", fg="white", width=20)
btn_install.pack(pady=10)

# Status label
status_label = tk.Label(root, text="", font=("Arial", 12))
status_label.pack(pady=10)

# Progress bar
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate", variable=progress_var)
progress_bar.pack(pady=10)

# Footer Frame
footer_frame = tk.Frame(root)
footer_frame.pack(pady=20)

tk.Label(footer_frame, text="Created with ", font=("Arial", 12, "bold"), fg="#4477CE").pack(side=tk.LEFT)
tk.Label(footer_frame, text="❤️", font=("Arial", 12, "bold"), fg="red").pack(side=tk.LEFT)
tk.Label(footer_frame, text=" by AccessPoint IT", font=("Arial", 12, "bold"), fg="#4477CE").pack(side=tk.LEFT)

root.mainloop()
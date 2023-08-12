import tkinter as tk
from tkinter import filedialog, ttk
import customtkinter as ctk
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
        # Initiate the progress bar in indeterminate mode
        progress_bar.configure(mode="indeterminate")
        progress_bar.start(10) # Start the progress bar animation
        status_label.config(text="Running Composer Install...", fg="blue")
        cmd = "composer install"
        subprocess.run(cmd, cwd=projectPath, shell=True)
        status_label.config(text="Command completed!", fg="green")

        # Set the progress bar to complete after command is done
        progress_bar.stop() # Stop the indeterminate animation
        progress_bar.configure(mode="determinate")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}", fg="red")
        # Stop the progress bar if an error occurs
        progress_bar.stop()
        progress_bar.configure(mode="determinate")

root = ctk.CTk()
root.title("Laravel Composer Installer")
center_window(root)

# Main title
ctk.CTkLabel(root, text="Laravel Composer Installer", font=("Arial", 16, "bold")).pack(pady=10)

# Project path input
path_frame = ctk.CTkFrame(root)
path_frame.pack(pady=10, fill=tk.X, padx=50)

DEFAULT_PATH = os.path.expanduser("C:/laragon/www/okul")
projectPath = DEFAULT_PATH

path_entry = ctk.CTkEntry(path_frame, width=35, font=("Arial", 12))
path_entry.insert(0, DEFAULT_PATH)
path_entry.pack(side=ctk.LEFT, fill=ctk.X, expand=True, padx=(0, 10))

browse_btn = ctk.CTkButton(path_frame, text="Browse", command=browse_folder)
browse_btn.pack(side=ctk.RIGHT)

# Composer Install button
btn_install = ctk.CTkButton(root, text="Composer Install", command=run_composer_install, font=("Arial", 14), width=200)
btn_install.pack(pady=10)

# Status label
status_label = ctk.CTkLabel(root, text="", font=("Arial", 12))
status_label.pack(pady=10)

# Progress bar
progress_bar = ctk.CTkProgressBar(root, width=400)
progress_bar.pack(pady=10)

# Footer Frame
footer_frame = ctk.CTkFrame(root)
footer_frame.pack(pady=20)

ctk.CTkLabel(footer_frame, text="Created by AccessPoint IT", font=("Arial", 20)).pack(side=tk.LEFT)

root.mainloop()
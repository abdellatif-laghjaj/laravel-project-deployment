import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from PIL import Image, ImageTk
import os
import subprocess

software_setups = {
    "Laragon": "laragon.exe",
    "Composer": "composer-v2.5.8.exe",
    "Node.js": "node-v18.16.1.msi"
}

def center_window(root, width=500, height=400):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

def all_setups_exist():
    for software, setup in software_setups.items():
        if not os.path.exists(os.path.join(folderPath, setup)):
            return software  # return the software name that's missing its setup file
    return True  # all setups exist

def install_softwares():
    missing_software = all_setups_exist()
    if missing_software != True:
        messagebox.showerror("Error", f"The setup for {missing_software} is missing!")
        return

    try:
        for software, setup in software_setups.items():
            status_label.config(text=f"Installing {software} ...")
            if software == "Laragon":
                install_laragon()
            elif software == "Composer":
                install_composer()
            elif software == "Node.js":
                install_node()
            progress_var.set((list(software_setups.keys()).index(software) + 1) / len(software_setups) * 100)
            root.update_idletasks()
        complete_installation()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during installation: {str(e)}")


def install_laragon():
    setupLaragon = os.path.join(folderPath, "laragon.exe")
    subprocess.run([setupLaragon], shell=True)
    os.environ['PATH'] += ";C:\\laragon\\bin\\php\\php-8.1.10-Win32-vs16-x64"
    subprocess.run(['setx', 'path', f"%path%;C:\\laragon\\bin\\php\\php-8.1.10-Win32-vs16-x64", '/M'], shell=True)


def install_composer():
    setupComposer = os.path.join(folderPath, "composer-v2.5.8.exe")
    subprocess.run([setupComposer], shell=True)


def install_node():
    setupNode = os.path.join(folderPath, "node-v18.16.1.msi")
    subprocess.run([setupNode], shell=True)


def complete_installation():
    status_label.config(text="Installation completed!")
    messagebox.showinfo("Info", "Setup is done, please click on OK to restart your PC!")
    os.system('shutdown /r /t 1')


def browse_folder():
    global folderPath
    folderPath = filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, folderPath)


def main():
    global path_entry, folderPath, status_label, progress_var, root

    root = tk.Tk()
    root.title("Software Installer")
    center_window(root)

    tk.Label(root, text="Tools Installation", font=("Arial", 16, "bold")).pack(pady=10)

    tk.Label(root, text="Please specify the folder containing installers:", font=("Arial", 12)).pack(pady=20)

    path_frame = tk.Frame(root)
    path_frame.pack(pady=10)

    path_entry = tk.Entry(path_frame, width=35, font=("Arial", 12))
    path_entry.pack(side=tk.LEFT, padx=(0, 10))

    browse_btn = tk.Button(path_frame, text="Browse", command=browse_folder, font=("Arial", 12), height=1)
    browse_btn.pack(side=tk.RIGHT)

    btn_install = tk.Button(root, text="Install Softwares", command=install_softwares, font=("Arial", 12), bg="green", fg="white")
    btn_install.pack(pady=20)

    status_label = tk.Label(root, text="", font=("Arial", 12))
    status_label.pack(pady=20)

    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate", variable=progress_var)
    progress_bar.pack(pady=20)

    # Footer
    footer_label = tk.Label(root, text="Created with ", font=("Arial", 12, "bold"), fg="#4477CE")
    footer_label.pack(pady=20, side=tk.LEFT)

    heart_label = tk.Label(root, text="❤️", font=("Arial", 12, "bold"), fg="red")
    heart_label.pack(pady=20, side=tk.LEFT)

    company_label = tk.Label(root, text=" by AccessPoint IT", font=("Arial", 12, "bold"), fg="#4477CE")
    company_label.pack(pady=20, side=tk.LEFT)

    root.mainloop()

if __name__ == "__main__":
    main()
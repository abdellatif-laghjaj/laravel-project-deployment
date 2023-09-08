import os
import subprocess
from typing import Self
import customtkinter as ctk
from tkinter import filedialog, messagebox

software_setups = {
    "Laragon": "laragon.exe",
    "VC_Redist": "VC_redist.x64.exe",
    "Composer": "composer-v2.5.8.exe",
    "Node.js": "node-v18.16.1.msi"
}

def center_window(root, width=500, height=460):
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
            status_label.configure(text=f"Installing {software} ...")
            if software == "Laragon":
                install_laragon()
            elif software == "VC_Redist":
                install_vc_redist()
            elif software == "Composer":
                install_composer()
            elif software == "Node.js":
                install_node()
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

def install_vc_redist():
    setupVCRedist = os.path.join(folderPath, "VC_redist.x64.exe")
    subprocess.run([setupVCRedist], shell=True)

def install_node():
    setupNode = os.path.join(folderPath, "node-v18.16.1.msi")
    subprocess.run([setupNode], shell=True)

def complete_installation():
    status_label.configure(text="Installation completed!")
    messagebox.showinfo("Info", "Setup is done, please click on OK to restart your PC!")
    os.system('shutdown /r /t 1')

def browse_folder():
    global folderPath
    folderPath = filedialog.askdirectory()
    path_entry.delete(0, "end")
    path_entry.insert(0, folderPath)

def main():
    global path_entry, folderPath, status_label, root

    root = ctk.CTk()
    root.title("Software Installer")
    root.geometry("500x460")

    center_window(root)

    ctk.CTkLabel(root, text="Tools Installation", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)

    ctk.CTkLabel(root, text="Please specify the folder containing installers:", font=ctk.CTkFont(size=12)).pack(pady=20)

    path_frame = ctk.CTkFrame(root)
    path_frame.pack(pady=10)

    path_entry = ctk.CTkEntry(path_frame, width=260, font=ctk.CTkFont(size=12))
    path_entry.pack(side="left", padx=(0, 10))

    browse_btn = ctk.CTkButton(path_frame, text="Browse", command=browse_folder)
    browse_btn.pack(side="right")

    btn_install = ctk.CTkButton(root, text="Install Softwares", command=install_softwares)
    btn_install.pack(pady=20)

    status_label = ctk.CTkLabel(root, text="", font=ctk.CTkFont(size=12))
    status_label.pack(pady=20)

    progress_bar = ctk.CTkProgressBar(root, width=400, height=20)
    progress_bar.pack(pady=20)

    footer_frame = ctk.CTkFrame(root)
    footer_frame.pack(pady=20)

    ctk.CTkLabel(footer_frame, text="Created by AccessPoint IT", font=ctk.CTkFont(size=12, weight="bold")).pack(side="left")

    root.mainloop()

if __name__ == "__main__":
    main()
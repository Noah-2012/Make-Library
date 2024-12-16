import tkinter as tk
from tkinter import messagebox
import subprocess

def build_project(target):
    try:
        # Run the make command with the selected target
        subprocess.run(["make", target], check=True)
        messagebox.showinfo("Build erfolgreich", "Build wurde erfolgreich abgeschlossen!")
    except subprocess.CalledProcessError:
        messagebox.showerror("Fehler", "Build fehlgeschlagen!")

def clean_project():
    try:
        # Run the make clean command to remove build artifacts
        subprocess.run(["make", "clean"], check=True)
        messagebox.showinfo("Clean erfolgreich", "Build-Artefakte wurden erfolgreich entfernt!")
    except subprocess.CalledProcessError:
        messagebox.showerror("Fehler", "Clean-Vorgang fehlgeschlagen!")

def showdr_project():
    try:
        # Run the make showdr command
        subprocess.run(["make", "showdr"], check=True)
        messagebox.showinfo("Showdr erfolgreich", "Showdr-Vorgang wurde erfolgreich abgeschlossen!")
    except subprocess.CalledProcessError:
        messagebox.showerror("Fehler", "Showdr-Vorgang fehlgeschlagen!")

def display_project():
    try:
        # Run the make display command
        subprocess.run(["make", "display"], check=True)
        messagebox.showinfo("Display erfolgreich", "Display-Vorgang wurde erfolgreich abgeschlossen!")
    except subprocess.CalledProcessError:
        messagebox.showerror("Fehler", "Display-Vorgang fehlgeschlagen!")

def create_gui():
    root = tk.Tk()
    root.title("Make Library Build Tool")

    # Dropdown für Auswahl des Targets (z.B. Debug, Release)
    target_label = tk.Label(root, text="Wähle Build-Target:")
    target_label.pack(padx=10, pady=5)

    target_var = tk.StringVar(value="release")
    target_dropdown = tk.OptionMenu(root, target_var, "debug", "release")
    target_dropdown.pack(padx=10, pady=5)

    # Button zum Starten des Builds
    build_button = tk.Button(root, text="Build starten", command=lambda: build_project(target_var.get()))
    build_button.pack(padx=10, pady=10)

    # Button zum Cleanen des Builds
    clean_button = tk.Button(root, text="Build bereinigen", command=clean_project)
    clean_button.pack(padx=10, pady=10)

    # Button zum Showdr-Vorgang
    showdr_button = tk.Button(root, text="Showdr ausführen", command=showdr_project)
    showdr_button.pack(padx=10, pady=10)

    # Button zum Display-Vorgang
    display_button = tk.Button(root, text="Display ausführen", command=display_project)
    display_button.pack(padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()

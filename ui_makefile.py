import tkinter as tk
from tkinter import messagebox, colorchooser, scrolledtext, Toplevel, Menu, simpledialog
import subprocess
import os
import shutil
import time

# Globale Variablen
button_colors = {"build": "#4CAF50", "clean": "#FF5722", "execute": "#2196F3"}
output_window = None
output_text = None
dark_mode = False
language = "de"
password = "1973"  # Das Passwort für experimentelle Funktionen
clock_label = None  # Für die Uhr
clock_visible = False  # Steuert, ob die Uhr angezeigt wird

# Funktion zum Ausführen des Befehls
def run_make_command(target):
    global output_text
    try:
        # Starte den Befehl ohne Umleitung
        process = subprocess.Popen(
            ["make", target],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )

        # Zeige Live-Ausgabe im Fenster
        for line in process.stdout:
            print(line.strip())  # Ausgabe in der Konsole
            if output_text:
                output_text.insert(tk.END, line)
                output_text.see(tk.END)
        
        process.wait()  # Warten, bis der Prozess abgeschlossen ist

        # Überprüfe Erfolg oder Fehler
        if process.returncode == 0:
            messagebox.showinfo("Erfolg", f"'{target}' wurde erfolgreich ausgeführt!")
        else:
            messagebox.showerror("Fehler", f"'{target}' ist fehlgeschlagen!")

    except Exception as e:
        messagebox.showerror("Fehler", f"Ein unerwarteter Fehler ist aufgetreten: {str(e)}")

# Farben der Buttons ändern
def change_button_colors():
    color = colorchooser.askcolor(title="Wähle die Farbe für die Knöpfe")[1]
    if color:
        for key in button_colors:
            button_colors[key] = color
        update_button_colors()

def update_button_colors():
    build_button.config(bg=button_colors["build"])
    clean_button.config(bg=button_colors["clean"])
    execute_button.config(bg=button_colors["execute"])

# Dunkelmodus umschalten
def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    update_ui_colors()

def update_ui_colors():
    if dark_mode:
        root.configure(bg="#333")
        for widget in root.winfo_children():
            widget.configure(bg="#333", fg="#fff")
        build_button.config(bg="#4CAF50", fg="#fff")
        clean_button.config(bg="#FF5722", fg="#fff")
        execute_button.config(bg="#2196F3", fg="#fff")
    else:
        root.configure(bg="#f0f0f0")
        for widget in root.winfo_children():
            widget.configure(bg="#f0f0f0", fg="#000")
        build_button.config(bg=button_colors["build"], fg="white")
        clean_button.config(bg=button_colors["clean"], fg="white")
        execute_button.config(bg=button_colors["execute"], fg="white")

# Projektinformationen anzeigen
def show_project_info():
    messagebox.showinfo("Projektinformationen", "Make Library Build Tool\nVersion 1.0\nEntwickler: Noah-2012")

# Automatische Build-Überwachung
def enable_auto_build():
    messagebox.showinfo("Automatische Build-Überwachung", "Diese Funktion wird noch entwickelt.\nBleiben Sie dran!")

# Mehrsprachigkeit umschalten
def switch_language():
    global language
    language = "en" if language == "de" else "de"
    messagebox.showinfo("Sprache geändert", "Sprache geändert! Bitte starten Sie das Programm neu.")

# Backup-Funktion für Makefile
def backup_makefile():
    try:
        src = "Makefile"
        dst = f"Makefile_backup_{int(time.time())}"
        shutil.copy(src, dst)
        messagebox.showinfo("Backup erfolgreich", f"Makefile wurde als {dst} gesichert!")
    except FileNotFoundError:
        messagebox.showerror("Fehler", "Makefile nicht gefunden!")

# Passwortabfrage für experimentelle Funktionen
def ask_password_for_experimental():
    password_input = simpledialog.askstring("Passwort eingeben", "Gib das Passwort ein:")
    if password_input == password:
        experimental_functions()
    else:
        messagebox.showerror("Fehler", "Falsches Passwort!")

# Experimentelle Funktionen
def experimental_functions():
    messagebox.showinfo("Experimentelle Funktionen", "Diese Funktionen sind derzeit in Entwicklung und nicht vollständig verfügbar.")
    show_clock()

# Uhr anzeigen
def show_clock():
    global clock_label, clock_visible, root
    if clock_visible:
        return
    clock_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0", fg="black")
    clock_label.pack(side="bottom", pady=10)  # Uhr wird am unteren Rand des Fensters angezeigt
    update_clock()
    clock_visible = True
    # Fensterhöhe um 30 Pixel erhöhen, wenn die Uhr angezeigt wird
    current_geometry = root.geometry().split("+")[0]
    width, height = map(int, current_geometry.split("x"))
    root.geometry(f"{width}x{height + 30}")  # 30 Pixel hinzufügen

# Uhrzeit aktualisieren
def update_clock():
    current_time = time.strftime("%H:%M:%S")
    if clock_label:
        clock_label.config(text=current_time)
    root.after(1000, update_clock)  # Aktualisiere alle 1000ms (1 Sekunde)

# Terminal-Ausgabefenster einblenden
def open_output_window():
    global output_window, output_text
    if output_window is not None:
        output_window.deiconify()
        return
    output_window = Toplevel()
    output_window.title("Terminal Output")
    output_window.geometry("600x400")
    output_text = scrolledtext.ScrolledText(output_window, wrap=tk.WORD)
    output_text.pack(expand=True, fill="both")

# GUI erstellen
def create_gui():
    global build_button, clean_button, execute_button, root

    root = tk.Tk()
    root.title("Make Library Build Tool")
    root.configure(bg="#f0f0f0")

    # Menüleiste erstellen
    menubar = Menu(root)
    root.config(menu=menubar)

    view_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Ansicht", menu=view_menu)
    view_menu.add_command(label="Knopffarben ändern", command=change_button_colors)
    view_menu.add_command(label="Terminal Output anzeigen", command=open_output_window)
    view_menu.add_command(label="Dunkelmodus umschalten", command=toggle_dark_mode)

    edit_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Bearbeiten", menu=edit_menu)
    edit_menu.add_command(label="Sprache wechseln", command=switch_language)
    edit_menu.add_command(label="Projektinformationen", command=show_project_info)
    edit_menu.add_command(label="Auto Build Überwachung", command=enable_auto_build)
    edit_menu.add_command(label="Makefile sichern", command=backup_makefile)
    edit_menu.add_command(label="Experimentelle Funktionen", command=ask_password_for_experimental)

    # Überschrift
    tk.Label(root, text="Make Library Build Tool", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

    # Build-Frame
    build_frame = tk.LabelFrame(root, text="Build-Einstellungen", font=("Arial", 10, "bold"), bg="#f9f9f9", padx=10, pady=10)
    build_frame.pack(padx=10, pady=10, fill="both")

    target_var = tk.StringVar(value="release")
    tk.Label(build_frame, text="Wähle Build-Target:", bg="#f9f9f9").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    tk.OptionMenu(build_frame, target_var, "debug", "release").grid(row=0, column=1, padx=5, pady=5)

    build_button = tk.Button(build_frame, text="Build starten", bg=button_colors["build"], fg="white", width=15,
                             command=lambda: run_make_command(target_var.get()))
    build_button.grid(row=1, column=0, columnspan=2, pady=10)

    # Clean-Frame
    clean_frame = tk.LabelFrame(root, text="Build bereinigen", font=("Arial", 10, "bold"), bg="#f9f9f9", padx=10, pady=10)
    clean_frame.pack(padx=10, pady=10, fill="both")
    clean_button = tk.Button(clean_frame, text="Clean ausführen", bg=button_colors["clean"], fg="white", width=15,
                             command=lambda: run_make_command("clean"))
    clean_button.pack(pady=5)

    # Zusatz-Targets
    extra_frame = tk.LabelFrame(root, text="Zusätzliche Targets", font=("Arial", 10, "bold"), bg="#f9f9f9", padx=10, pady=10)
    extra_frame.pack(padx=10, pady=10, fill="both")
    extra_var = tk.StringVar(value="showdr")
    tk.Label(extra_frame, text="Wähle Target:", bg="#f9f9f9").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    tk.OptionMenu(extra_frame, extra_var, "showdr", "display").grid(row=0, column=1, padx=5, pady=5)
    execute_button = tk.Button(extra_frame, text="Befehl ausführen", bg=button_colors["execute"], fg="white", width=15,
                               command=lambda: run_make_command(extra_var.get()))
    execute_button.grid(row=1, column=0, columnspan=2, pady=10)

    update_button_colors()
    root.mainloop()

if __name__ == "__main__":
    create_gui()

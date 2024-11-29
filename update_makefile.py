import os

# Pfad zum Haupt-Makefile
makefile_path = "Makefile"

# Pfad zum Projektordner
projects_dir = "projects"

def get_subdirs(path):
    """Gibt eine Liste der Unterordner zurück."""
    return [f.path for f in os.scandir(path) if f.is_dir()]

def update_makefile():
    """Aktualisiert die SUBDIRS im Haupt-Makefile."""
    if not os.path.exists(makefile_path):
        print(f"Fehler: {makefile_path} nicht gefunden!")
        return

    # Aktuelle Projekte im Ordner "projects/"
    current_subdirs = get_subdirs(projects_dir)
    current_subdirs = [os.path.relpath(d, start=".") for d in current_subdirs]  # relative Pfade

    # Alte Makefile-Inhalte einlesen
    with open(makefile_path, "r") as file:
        lines = file.readlines()

    # SUBDIRS finden und aktualisieren
    new_lines = []
    subdirs_updated = False
    for line in lines:
        if line.startswith("SUBDIRS"):
            subdirs_line = f"SUBDIRS = {' '.join(current_subdirs)}\n"
            new_lines.append(subdirs_line)
            subdirs_updated = True
        else:
            new_lines.append(line)

    if not subdirs_updated:
        print("SUBDIRS nicht im Makefile gefunden. Bitte füge eine Zeile mit 'SUBDIRS =' hinzu.")
        return

    # Änderungen speichern
    with open(makefile_path, "w") as file:
        file.writelines(new_lines)

    print(f"Makefile aktualisiert: SUBDIRS = {' '.join(current_subdirs)}")

if __name__ == "__main__":
    if os.path.exists(projects_dir):
        update_makefile()
    else:
        print(f"Fehler: Der Ordner '{projects_dir}' existiert nicht!")


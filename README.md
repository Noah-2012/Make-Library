# Makefile-Projekte

---

## WARNUNG: Eigentlich für Linux aber unter Windows geht es auch. 

---

## Übersicht
Dieses Repository enthält eine Sammlung von Projekten, die mit `make` verwaltet werden. Jedes Projekt hat ein eigenes Makefile, das speziell auf die Anforderungen des jeweiligen Projekts zugeschnitten ist. Zusätzlich gibt es ein Haupt-Makefile, mit dem alle Projekte zentral verwaltet werden können.

---

## Voraussetzungen

Bevor du die Projekte bauen kannst, stelle sicher, dass folgende Tools installiert sind:

### Allgemeine Voraussetzungen
- **GNU Make**: Zum Verwalten der Build-Prozesse.
  - Installation (Debian/Ubuntu):  
    ```bash
    sudo apt update && sudo apt install make
    ```
- **xxd**: Für die Erstellung von Hex-Dumps.
  - Installation (Debian/Ubuntu):  
    ```bash
    sudo apt update && sudo apt install xxd
    ```

### Projektspezifische Voraussetzungen

#### Für das Assembly-Projekt:
- **NASM**: Ein Assembler für x86-Architekturen.
  - Installation (Debian/Ubuntu):  
    ```bash
    sudo apt update && sudo apt install nasm
    ```

---


### Haupt Makefile:
- Das Haupt Makefile verwaltet alle unter Projekte.
  - Du musst den Ordner mit dem Haupt Makefile im Terminal öffnen.
    - Mit diesem Befehl werden alle Unterprojekte gebaut:
    ```bash
    make
    ```
    - Mit diesem Befehl werden alle gereinigt:
    ```bash
    make clean
    ```
    - Und mit diesem kann man ein bestimmtes Unterprojekt bauen:
    ```bash
    make -C projects/<project_name>
    ```
---

### WARNUNG: DevKitARM, DevKitPPC!
- Ihr müsst euch DevKitPro herunterladen und die Ordner DevKitARM und DevKitPPC mit in das DevKitPro Verzeichniss mit rein schieben!

---

### Update Pythonprogramm(update_makefile.py):
- Die python Datei sorgt nur dafür das neue Ordner im projects Ordner im Makefile eingefügt werden.
  - Bei Linux kann man Pakete nicht über pip installieren. Wäre ja auch viel zu leicht.
  - Du musst sicher stellen das Python auf deinem System installiert ist.
  - Damit du jetzt os instalieren kannst(Was benötigt ist um das Python Script auszuführen) musst du folgende Befehle eingeben:
  ```bash
  python3 -m venv myenv
  ```
  - Das erstellt eine virtuelle Umgebung. Um diese zu aktivieren, diesen Code:
  ```bash
  source myenv/bin/activate
  ```
  - Nun hast du deine virtuelle Umgebung.
  - Jetzt müssen wir os installieren:
  ```bash
  pip install os
  ```
  - Nach der Installation schliessen wir unsere virtuelle umgebung wieder.
  - Wenn während der Installation irgendwas mit Ja/Nein kommt, mach einfach ja.
  - Um die Umgebung jetzt zu schliessen, dieser Code:
  ```bash
  deactivate
  ```
  - Die python Datei im Ordner mit dem Makefile ausführen.

├── debug/                  # Haupt-Debug-Logs
├── Makefile                # Haupt-Makefile
└── update_makefile.py      # Python-Skript zum Aktualisieren des Haupt-Makefiles


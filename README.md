# Makefile-Projekte

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

## Ordnerstruktur

```plaintext
make/
├── projects/
│   ├── Assembly(Linux)/   # Assembly-Projekt
│   │   ├── asm/            # Assembly-Quellcode
│   │   ├── build/          # Kompilierte Dateien
│   │   ├── debug/          # Debug-Logs
│   │   ├── exe/            # Ausführbare Dateien
│   │   ├── bin/            # Bin-Dateien
│   │   ├── Makefile        # Makefile für Assembly-Projekt
├── Makefile                # Haupt-Makefile

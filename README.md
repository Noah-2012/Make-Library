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

#### Für das C-Projekt:
- **GCC**: Ein Compiler für C-Programme.
  - Installation (Debian/Ubuntu):  
    ```bash
    sudo apt update && sudo apt install gcc
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

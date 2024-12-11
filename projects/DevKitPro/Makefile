# Haupt- Makefile für DevKitPro Projekte

# Setze hier die DevKitPro-Pfade auf den Ordner, in dem DevKitPro installiert ist
DEVKITARM ?= projects/DevKitPro/devkitARM      # devkitARM befindet sich im devkitpro Ordner
DEVKITPPC ?= projects/DevKitPro/devkitPPC      # devkitPPC befindet sich im devkitpro Ordner

.PHONY: all clean set-devkitpro-vars

# Bereinige alle Projekte
clean:
	@echo "Bereinige alle devkitpro Projekte..."
	$(MAKE) -C 3ds clean
	$(MAKE) -C gamecube clean
	$(MAKE) -C gba clean
	$(MAKE) -C gp32 clean
	$(MAKE) -C nds clean
	$(MAKE) -C wii clean

# Baue alle Projekte
all:
	@echo "Baue alle devkitpro Projekte..."
	$(MAKE) -C 3ds
	$(MAKE) -C gamecube
	$(MAKE) -C gba
	$(MAKE) -C gp32
	$(MAKE) -C nds
	$(MAKE) -C wii

# Setze Umgebungsvariablen für devkitpro
set-devkitpro-vars:
	@echo "Setze Umgebungsvariablen für devkitpro"
	@export DEVKITARM=$(DEVKITARM); \
	export DEVKITPPC=$(DEVKITPPC); \
	$(MAKE) clean-devkitpro

# Beispiel für clean-devkitpro (optional, je nach Verwendung)
clean-devkitpro:
	@echo "Bereinige DevKitPro..."
	$(MAKE) -C 3ds clean
	$(MAKE) -C gamecube clean
	$(MAKE) -C gba clean
	$(MAKE) -C gp32 clean
	$(MAKE) -C nds clean
	$(MAKE) -C wii clean

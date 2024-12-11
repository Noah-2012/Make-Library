# Haupt- Makefile für DevKitPro Projekte
# Setze hier deine devkitpro Pfade ein, falls sie noch nicht gesetzt sind
DEVKITARM ?= /opt/devkitpro/devkitARM  # Stelle sicher, dass dies korrekt ist
DEVKITPPC ?= /opt/devkitpro/devkitPPC  # Stelle sicher, dass dies korrekt ist

# Ziel, um Umgebungsvariablen zu setzen und den Bereinigungsvorgang zu starten
.PHONY: clean

clean:
	@echo "Bereinige alle Projekte..."
	# Bereinigung der einzelnen Projekte
	$(MAKE) -C projects/C_to_Linux_Execute clean
	$(MAKE) -C projects/Cpp_to_Linux_Execute clean
	$(MAKE) -C projects/Assembly clean
	$(MAKE) -C projects/DevKitPro clean

# Bereinigung der DevKitPro Projekte
.PHONY: clean-devkitpro
clean-devkitpro:
	@echo "Bereinige alle devkitpro Projekte..."
	$(MAKE) -C projects/DevKitPro/3ds clean
	$(MAKE) -C projects/DevKitPro/gamecube clean
	$(MAKE) -C projects/DevKitPro/gba clean
	$(MAKE) -C projects/DevKitPro/gp32 clean
	$(MAKE) -C projects/DevKitPro/nds clean
	$(MAKE) -C projects/DevKitPro/wii clean

# Beim Bereinigen für devkitpro sicherstellen, dass die Umgebungsvariablen gesetzt sind
.PHONY: set-devkitpro-vars
set-devkitpro-vars:
	@echo "Setze Umgebungsvariablen für devkitpro"
	@export DEVKITARM=$(DEVKITARM); \
	export DEVKITPPC=$(DEVKITPPC); \
	$(MAKE) clean-devkitpro

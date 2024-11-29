# Haupt-Makefile

# Liste der Unterprojekte
SUBDIRS = projects/Assembly projects/C_to_Linux_Execute

.PHONY: all clean rebuild

# Ziel: Alle Unterprojekte bauen
all:
	@echo "Baue alle Projekte..."
	@for dir in $(SUBDIRS); do \
		echo "Betrete $$dir..."; \
		$(MAKE) -C $$dir; \
	done
	@echo "Alle Projekte erfolgreich gebaut!"

# Ziel: Alle Unterprojekte bereinigen
clean:
	@echo "Bereinige alle Projekte..."
	@for dir in $(SUBDIRS); do \
		echo "Bereinige $$dir..."; \
		$(MAKE) -C $$dir clean; \
	done
	@echo "Alle Projekte bereinigt!"

# Ziel: Komplett neu bauen
rebuild: clean all


# Definiere den Pfad zu den Unterverzeichnissen innerhalb von devkitpro
DEVKITPRO_PROJECTS := $(wildcard */)

# Standardziel (all), das alle Makefiles in den Unterverzeichnissen aktiviert
all:
	@echo "Bauen der Projekte in devkitpro..."
	$(foreach dir, $(DEVKITPRO_PROJECTS), $(MAKE) -C $(dir);)

# Clean-Ziel für alle Projekte
clean:
	@echo "Bereinige alle devkitpro Projekte..."
	$(foreach dir, $(DEVKITPRO_PROJECTS), $(MAKE) -C $(dir) clean;)

# Weitere spezifische Ziele können hier hinzugefügt werden

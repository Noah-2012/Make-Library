# Liste der Unterprojekte
SUBDIRS = projects/C_to_Linux_Execute projects/Cpp_to_Linux_Execute projects/Assembly

# Log-Datei im Debug-Ordner
LOGFILE = debug/build.log

.PHONY: all clean rebuild

# Ziel: Alle Unterprojekte bauen
all: display
	@echo "Baue alle Projekte..." | tee -a $(LOGFILE)
	@for dir in $(SUBDIRS); do \
		echo "Betrete $$dir..." | tee -a $(LOGFILE); \
		$(MAKE) -C $$dir | tee -a $(LOGFILE); \
	done
	@echo "Alle Projekte erfolgreich gebaut!" | tee -a $(LOGFILE)

# Ziel: Alle Unterprojekte bereinigen
clean:
	@echo "Bereinige alle Projekte..." | tee -a $(LOGFILE)
	@for dir in $(SUBDIRS); do \
		echo "Bereinige $$dir..." | tee -a $(LOGFILE); \
		$(MAKE) -C $$dir clean | tee -a $(LOGFILE); \
	done
	@echo "Alle Projekte bereinigt!" | tee -a $(LOGFILE)

# Ziel: Komplett neu bauen
rebuild: clean all

display:
	@echo "███╗   ██╗ ██████╗  █████╗ ██╗  ██╗              ██████╗  ██████╗  ██╗██████╗ ";
	@echo "████╗  ██║██╔═══██╗██╔══██╗██║  ██║              ╚════██╗██╔═████╗███║╚════██╗";
	@echo "██╔██╗ ██║██║   ██║███████║███████║    █████╗     █████╔╝██║██╔██║╚██║ █████╔╝";
	@echo "██║╚██╗██║██║   ██║██╔══██║██╔══██║    ╚════╝    ██╔═══╝ ████╔╝██║ ██║██╔═══╝ ";
	@echo "██║ ╚████║╚██████╔╝██║  ██║██║  ██║              ███████╗╚██████╔╝ ██║███████╗";
	@echo "╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝              ╚══════╝ ╚═════╝  ╚═╝╚══════╝";
	@echo "                                     NOAH - 2012                              ";

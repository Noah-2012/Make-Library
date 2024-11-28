# Variablen
ASM = nasm
LD = ld
OBJCOPY = objcopy
ASM_DIR = asm
BUILD_DIR = build
BIN_DIR = bin
EXE_DIR = exe
DEBUG_DIR = debug
SRC = $(ASM_DIR)/main.asm
OBJ = $(BUILD_DIR)/main.o
OUT = $(EXE_DIR)/main
BIN = $(BIN_DIR)/main.bin
HEX = $(BUILD_DIR)/main.hex
C_SRC = $(BUILD_DIR)/main.c
DEBUG_LOG = $(DEBUG_DIR)/build.log

# Compiler- und Linker-Optionen
ASMFLAGS = -f elf64 -g -F dwarf
LDFLAGS = 


.PHONY: all clean

# Standardziel
all: $(DEBUG_DIR) $(DEBUG_LOG) $(OUT) $(BIN) $(HEX) $(C_SRC)

# Debug-Log erstellen
$(DEBUG_LOG):
	mkdir -p $(DEBUG_DIR)
	echo "Build gestartet: $$(date)" > $@

# Ziel: Executable erstellen
$(OUT): $(OBJ) $(DEBUG_LOG)
	mkdir -p $(EXE_DIR)
	{ $(LD) $(LDFLAGS) -o $@ $(OBJ) && echo "Executable erstellt: $@" >> $(DEBUG_LOG); } || \
	{ echo "Fehler beim Erstellen der Executable: $@" >> $(DEBUG_LOG); exit 1; }

# Ziel: Objektdatei erstellen
$(OBJ): $(SRC) $(DEBUG_LOG)
	mkdir -p $(BUILD_DIR)
	{ $(ASM) $(ASMFLAGS) -o $@ $< && echo "Objektdatei erstellt: $@" >> $(DEBUG_LOG); } || \
	{ echo "Fehler beim Erstellen der Objektdatei: $@" >> $(DEBUG_LOG); exit 1; }

# Ziel: Binärdatei erstellen
$(BIN): $(SRC) $(DEBUG_LOG)
	mkdir -p $(BIN_DIR)
	{ $(ASM) -f bin -o $@ $< && echo "Binärdatei erstellt: $@" >> $(DEBUG_LOG); } || \
	{ echo "Fehler beim Erstellen der Binärdatei: $@" >> $(DEBUG_LOG); exit 1; }

# Ziel: Hex-Datei erstellen
$(HEX): $(BIN) $(DEBUG_LOG)
	mkdir -p $(BUILD_DIR)
	{ xxd -p $< > $@ && echo "Hex-Datei erstellt: $@" >> $(DEBUG_LOG); } || \
	{ echo "Fehler beim Erstellen der Hex-Datei: $@" >> $(DEBUG_LOG); exit 1; }

# Ziel: C-Datei erstellen
$(C_SRC): $(OBJ) $(DEBUG_LOG)
	mkdir -p $(BUILD_DIR)
	{ $(OBJCOPY) -O binary $< $(BUILD_DIR)/main_temp.bin && \
	  xxd -i $(BUILD_DIR)/main_temp.bin $@ && \
	  echo "C-Datei erstellt: $@" >> $(DEBUG_LOG); \
	  rm -f $(BUILD_DIR)/main_temp.bin; } || \
	{ echo "Fehler beim Erstellen der C-Datei: $@" >> $(DEBUG_LOG); exit 1; }

# Debug-Ordner erstellen
$(DEBUG_DIR):
	mkdir -p $(DEBUG_DIR)

# Ziel: Aufräumen
clean:
	rm -rf $(BUILD_DIR) $(BIN_DIR) $(EXE_DIR) $(DEBUG_DIR)

# Ziel: Komplett neu bauen
rebuild: clean all


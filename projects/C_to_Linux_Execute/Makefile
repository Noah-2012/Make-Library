# Variablen
CC = gcc
CFLAGS = -Wall -g
SRC_DIR = c
BUILD_DIR = build
EXE_DIR = exe
SRC = $(SRC_DIR)/main.c
OBJ = $(BUILD_DIR)/main.o
TARGET = $(EXE_DIR)/main

.PHONY: All clean


# Standardziel
all: setup $(TARGET)

# Erstelle die benötigten Verzeichnisse
setup:
	mkdir -p $(BUILD_DIR) $(EXE_DIR)

# Kompiliere die .c-Datei in eine .o-Datei
$(OBJ): $(SRC)
	$(CC) $(CFLAGS) -c $< -o $@

# Linke die .o-Datei zu einer ausführbaren Datei
$(TARGET): $(OBJ)
	$(CC) $(CFLAGS) $< -o $@

# Bereinige generierte Dateien
clean:
	rm -rf $(BUILD_DIR) $(EXE_DIR)

# Erneuere das Build
rebuild: clean all


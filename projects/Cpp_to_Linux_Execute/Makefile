# Variablen
CXX = g++
CXXFLAGS = -Wall -g
SRC_DIR = cpp
BUILD_DIR = build
EXE_DIR = exe

# Quelldatei und Ziel
SRC = $(SRC_DIR)/main.cpp
OBJ = $(BUILD_DIR)/main.o
EXE = $(EXE_DIR)/main

# Standardziel
all: $(EXE)

# Erstellen der ausführbaren Datei
$(EXE): $(OBJ)
	@mkdir -p $(EXE_DIR)
	$(CXX) $(OBJ) -o $(EXE)

# Erstellen der Objektdatei
$(OBJ): $(SRC)
	@mkdir -p $(BUILD_DIR)
	$(CXX) $(CXXFLAGS) -c $(SRC) -o $(OBJ)

# Bereinigung
clean:
	rm -rf $(BUILD_DIR) $(EXE_DIR)

.PHONY: all clean


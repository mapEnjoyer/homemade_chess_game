#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status
set -e

REQUIREMENTS_FILE="requirements.txt"
VENV_DIR="venv"

echo "=== Starting Python Package Installation ==="

# 1. Check if the requirements.txt file exists
if [ ! -f "$REQUIREMENTS_FILE" ]; then
    echo "Error: $REQUIREMENTS_FILE not found in the current directory!"
    exit 1
fi

# 2. Setup a virtual environment if it does not exist
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment in '$VENV_DIR'..."
    python3 -m venv "$VENV_DIR"
else
    echo "Virtual environment '$VENV_DIR' already exists."
fi

# 3. Activate the virtual environment
echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# 4. Upgrade pip to ensure the latest installation features
echo "Upgrading pip..."
pip install --upgrade pip

# 5. Install the Python packages
echo "Installing packages from $REQUIREMENTS_FILE..."
pip install -r "$REQUIREMENTS_FILE"

echo "=== Installation Completed Successfully! ==="
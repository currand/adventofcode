#!/bin/bash

# Check if a parameter is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 XX (where XX is a two-digit number)"
    exit 1
fi

# Validate the parameter (must be a two-digit number)
if ! [[ $1 =~ ^[0-9]{2}$ ]]; then
    echo "Error: Parameter must be a two-digit number."
    exit 1
fi

# Assign the parameter to a variable
X=$1

# Create the directory
mkdir "day$X"

# Create the files inside the directory
cp day_temp.py "day$X/day${X}a.py"
cp day_temp.py "day$X/day${X}b.py"
touch "day$X/day${X}.txt"
touch "day$X/test${X}.txt"

echo "Directory and files created successfully."

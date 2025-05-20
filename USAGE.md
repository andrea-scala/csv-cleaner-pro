# Quick Start Guide for CSV Cleaner Pro

This guide will help you run CSV Cleaner Pro even if you have no experience with Python.

---

## Step 1: Install Python

- Download and install Python from [python.org](https://www.python.org/downloads/)
- Make sure to check the option **Add Python to PATH** during installation

---

## Step 2: Download the Project Files

- Download or clone this repository to your computer

---

## Step 3: Install Required Libraries

- Open a command prompt (Windows) or terminal (Mac/Linux)
- Navigate to the project folder (e.g. `cd path/to/csv-cleaner-pro`)
- Run the following command to install dependencies:

```bash
pip install -r requirements.txt
```

---

## Step 4: Run the Tool

- Use this command format to clean your CSV file:

```bash
python main.py --input yourfile.csv --output cleaned.csv
```

- Replace `yourfile.csv` with your actual file path  
- `cleaned.csv` is the file that will be created with the cleaned data

---

## Optional Flags

- `-e` or `--remove-empty-rows`: remove completely empty rows  
- `-d` or `--remove-duplicates`: remove duplicate rows  
- `-t` or `--trim-header`: trim whitespace from headers  

Example with options:

```bash
python main.py -i yourfile.csv -o cleaned.csv -e -d -t
```

---

If you have any questions, feel free to contact me!

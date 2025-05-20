# csv-cleaner-pro
A simple and flexible Python CLI tool to clean CSV files by removing empty rows, duplicates, and trimming headers. Perfect for data preprocessing and automation tasks.
Main features:

- Removes completely empty rows
- Removes duplicate rows
- Trims whitespace from headers
- Saves a new cleaned CSV file

How to use:

Example command:

python main.py --input examples/dirty_sample.csv --output clean_output.csv

Requirements:

To run the script, install the required packages with:

pip install -r requirements.txt

Supported options:

-i, --input            path to the input CSV file (required)
-o, --output           path to save the cleaned CSV file (required)
-e, --remove-empty-rows    removes completely empty rows (optional)
-d, --remove-duplicates    removes duplicate rows (optional)
-t, --trim-header          trims whitespace from headers (optional)

License:

This project is released under the MIT license.

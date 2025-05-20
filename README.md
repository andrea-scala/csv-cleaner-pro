# CSV Cleaner Pro

CSV Cleaner Pro is a lightweight command-line Python tool designed to quickly clean CSV files.

It helps you:

- Remove completely empty rows
- Remove duplicate entries
- Trim whitespace from headers

This tool is ideal for data analysts, developers, and freelancers who need to automate CSV preprocessing.

Built with simplicity and flexibility in mind, CSV Cleaner Pro can be integrated easily into your workflow or larger automation pipelines.

Feel free to use, modify, and adapt it for your projects!

Licensed under the MIT License.

---

## How to use

Run the script from the command line:

```bash
python main.py --input examples/dirty_sample.csv --output clean_output.csv
```

---

## Requirements

Install the dependencies with:

```bash
pip install -r requirements.txt
```

---

## Supported options

- `-i`, `--input`: path to the input CSV file (required)
- `-o`, --output`: path to save the cleaned CSV file (required)
- `-e`, `--remove-empty-rows`: removes completely empty rows (optional)
- `-d`, `--remove-duplicates`: removes duplicate rows (optional)
- `-t`, `--trim-header`: trims whitespace from headers (optional)

---

## License

This project is released under the MIT license.

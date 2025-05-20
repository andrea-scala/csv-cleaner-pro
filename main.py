import argparse
from cleaner.csv_cleaner import clean_csv

def main():
    parser = argparse.ArgumentParser(description="Clean CSV files quickly via CLI.")
    parser.add_argument("-i", "--input", required=True, help="Path to the input CSV file.")
    parser.add_argument("-o", "--output", required=True, help="Path to save the cleaned CSV file.")
    parser.add_argument("-e", "--remove-empty-rows", action="store_true", help="Remove completely empty rows.")
    parser.add_argument("-d", "--remove-duplicates", action="store_true", help="Remove duplicate rows.")
    parser.add_argument("-t", "--trim-header", action="store_true", help="Trim whitespace from headers.")

    args = parser.parse_args()

    clean_csv(
        input_path=args.input,
        output_path=args.output,
        remove_empty_rows=args.remove_empty_rows,
        remove_duplicates=args.remove_duplicates,
        trim_header=args.trim_header
    )

if __name__ == "__main__":
    main()

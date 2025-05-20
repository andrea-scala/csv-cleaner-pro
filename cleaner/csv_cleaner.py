import pandas as pd

def clean_csv(input_path, output_path, remove_empty_rows=True, remove_duplicates=True, trim_header=True):
    """
    Cleans a CSV file by removing empty rows, duplicates, and trimming headers.

    Args:
        input_path (str): Path to the input CSV file.
        output_path (str): Path to save the cleaned CSV file.
        remove_empty_rows (bool): Whether to remove completely empty rows.
        remove_duplicates (bool): Whether to remove duplicate rows.
        trim_header (bool): Whether to trim whitespace from header names.
    """
    # Read CSV file
    df = pd.read_csv(input_path)

    # Trim header whitespace if requested
    if trim_header:
        df.columns = [col.strip() for col in df.columns]

    # Remove empty rows if requested
    if remove_empty_rows:
        df.dropna(how='all', inplace=True)

    # Remove duplicate rows if requested
    if remove_duplicates:
        df.drop_duplicates(inplace=True)

    # Save cleaned CSV
    df.to_csv(output_path, index=False)
    print(f"Cleaned CSV saved to: {output_path}")

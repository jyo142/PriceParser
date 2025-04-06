import pandas as pd
from price_parser import Price
import argparse

def read_categories_price(csv_name):
    df = pd.read_csv(csv_name)
    # Create the list of dictionaries (each dictionary is an object)
    result = [{"name": row["Name"], "price": row["Price"]} for index, row in df.iterrows()]

    # Print the result
    print(result)
    return result

ignore_columns = ["Lotto"]
column_mapping = {
    "T-General Mercahnt": "T General Mercahnt",
    "Tax": "Taxable"
}
def edit_spreadsheet(categories_price, spreadsheet_name, row_number):
    df = pd.read_csv(spreadsheet_name)

    for item in categories_price:
        name = item["name"]
        name_upper = name.upper()
        price = item["price"]
        
        if name in ignore_columns:
            print(f"Skipping {name} (in ignore list)")
            continue

        mapped_name = column_mapping.get(name)
        if mapped_name:
            name = mapped_name
            name_upper = mapped_name.upper()

        # Case-insensitive matching: Convert both name and columns to uppercase
        matching_columns = [col for col in df.columns if col.upper() == name_upper]
        # If a matching column exists
        if matching_columns:
            column_name = matching_columns[0]  # Take the first match (if multiple matches, but unlikely)
            price_parsed = Price.fromstring(price)
            if price_parsed.amount is not None:
                df.at[row_number - 1, column_name] = float(price_parsed.amount)
                print(f"Set price for {name} to {price} in column {column_name}")
            else:
                print("Could not parse price.")
        else:
            print("No matching column")

    # Save the updated file
    df.to_csv(spreadsheet_name, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script to parse prices in one csv and add it to another")
    parser.add_argument("source", type=str, help="CSV file to parse data from")
    parser.add_argument("dest", type=str, help="CSV file to add prices to")
    parser.add_argument("row", type=int, help="Row number to add to")
    args = parser.parse_args()

    categories_price = read_categories_price(csv_name=args.source)
    edit_spreadsheet(categories_price=categories_price, spreadsheet_name=args.dest, row_number=args.row)

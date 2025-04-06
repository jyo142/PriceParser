import fitz  # PyMuPDF
import csv
import pandas as pd
from price_parser import Price

def read_categories_price(csv_name):
    df = pd.read_csv(csv_name)
    # Create the list of dictionaries (each dictionary is an object)
    result = [{"name": row["Name"], "price": row["Price"]} for index, row in df.iterrows()]

    # Print the result
    print(result)
    return result

column_mapping = {
    "T-General Mercahnt": "T General Mercahnt",
    "Tax": "Taxable"
}
def edit_spreadsheet(categories_price, spreadsheet_name):
    df = pd.read_csv(spreadsheet_name)

    # Iterate through the name_price_list and update values in row 23
    for item in categories_price:
        name = item["name"]
        price = item["price"]
        
        # Case-insensitive matching: Convert both name and columns to uppercase
        matching_columns = [col for col in df.columns if col.upper() == name.upper()]
        # If a matching column exists
        if matching_columns:
            column_name = matching_columns[0]  # Take the first match (if multiple matches, but unlikely)
            price_parsed = Price.fromstring(price)
            if price_parsed.amount is not None:
                df.at[22, column_name] = float(price_parsed.amount) # row 23 in CSV corresponds to index 22 in pandas
                print(f"Set price for {name} to {price} in column {column_name}")
            else:
                print("Could not parse price.")
        else:
            print("No matching column, check if there is a mapping")
            # If no matching column, check if there's a mapping
            mapped_name = column_mapping.get(name).upper()
            if mapped_name and mapped_name in df.columns:
                price_parsed = Price.fromstring(price)
                if price_parsed.amount is not None:
                    df.at[22, column_name] = float(price_parsed.amount)  # row 23 in CSV corresponds to index 22 in pandas
                else:
                    print("Could not parse price.")
                print(f"Set price for {name} to {price} in mapped column {mapped_name}")
            else:
                print(f"No matching column or mapping for {name}, skipping...")
    # Save the updated file
    df.to_csv(spreadsheet_name, index=False)

if __name__ == "__main__":
    # Replace this with your PDF file path
    # pdf_file_path = "test.pdf"
    # extracted_text = extract_text_from_pdf(pdf_file_path)
    
    # # Print or save to a text file
    # print(extracted_text)
    # with open("output.txt", "w", encoding="utf-8") as f:
    #     f.write(extracted_text)
    categories_price = read_categories_price(csv_name="sales_data.csv")
    edit_spreadsheet(categories_price=categories_price, spreadsheet_name="MAR(Sheet1).csv")

# 🧾 PriceParser

**PriceParser** is a Python script that reads category price data from a source CSV file and inserts the corresponding prices into a specific row of a destination CSV file.

---

## 📁 Requirements

- Python 3.6+

---

## 📌 Setup

- Install Python 3
- Install virtual environment
  ```bash
  python3 -m venv .venv
  ```
- Activate virtual environment
  ```bash
  .venv\Scripts\activate
  ```
- Install requirments.txt
  ```bash
  pip install -r requirements.txt
  ```

## 📌 What It Does

- Reads a CSV file with `Name` and `Price` columns.
- Matches category names (e.g. `"Beer/Wine"`, `"Cigarette"`) to columns in a destination spreadsheet.
- Inserts the price values into a specified row number in the destination file.

---

## 🚀 Usage

```bash
python3 priceParser.py {sourceFile} {destFile} {rowNumber}
```

### Arguments:

| Argument     | Description                                                                 |
| ------------ | --------------------------------------------------------------------------- |
| `sourceFile` | CSV file with the `Name` and `Price` columns (e.g. `sales_data.csv`)        |
| `destFile`   | Destination CSV file to which prices will be added (e.g. `MAR(Sheet1).csv`) |
| `rowNumber`  | Row number in the destination file where the prices should be inserted      |

---

## ✅ Example

```bash
python3 priceParser.py "sales_data.csv" "MAR(Sheet1).csv" 23
```

This will:

- Read category names and prices from `sales_data.csv`.
- Match each category name to a column header in `MAR(Sheet1).csv`.
- Insert the price into **row 23** (note: index starts from 1 in CSV but 0 in pandas).

---

## 🧠 Notes

- Column name matching is **case-insensitive**.
- If an exact match isn’t found, a **mapping dictionary** can be used to redirect names to column headers.
- Prices are automatically parsed from strings like `$1,091.70` into numbers.
- Categories can be excluded via an `ignore_columns` list in the script (e.g. to skip `"Lotto"`).

---

## 🛠️ Example Source File (`sales_data.csv`)

| Name      | Price     |
| --------- | --------- |
| Beer/Wine | $1,091.70 |
| Cigarette | $570.08   |
| Lotto     | $80.00    |

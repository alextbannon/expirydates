import csv
from datetime import date

# Introduction
print("""Hello! Welcome to your expiry date log. 
This application helps you to keep track of the expiry dates of perishable items in your kitchen.
-------------------------------------------------------------------------------------------------""")

# Check if all_products.csv exists, create file if doesn't exist
try:
    with open("all_products.csv", "r") as all_products_exists:
        reader = csv.reader(all_products_exists)
except:
    with open("all_products.csv", "w", newline="") as all_products:
        writer = csv.writer(all_products)
        writer.writerow(["Entry date", "Product", "Expiry date"])

# Take user inputs
entry_date = date.today()
product = input("Enter product name: ")
expiry_date = input("Enter expiry date in YYYY-MM-DD format: ")

# Turn expiry date string into date format
year, month, day = map(int, expiry_date.split("-"))
expiry_date = date(year, month, day)

# Insert new data to new row in all_products.csv
with open("all_products.csv", "a", newline="") as all_products:
    writer = csv.writer(all_products)
    writer.writerow([entry_date, product, expiry_date])

import csv
from datetime import date, datetime

expiry_dates = []

# Convert all_products.csv to list
with open("all_products.csv", "r") as data_file:
    reader = csv.reader(data_file)
    for row in reader:
        expiry_dates.append(row)

# Remove header row
expiry_dates.pop(0)

# Append any expired products to new list called expired_products
expired_products = []
i = 0
while i < len(expiry_dates):
    expiry_date_df = datetime.strptime(expiry_dates[i][2], "%Y-%m-%d")
    if expiry_date_df < datetime.today():
        expired_products.append(expiry_dates[i])
    i += 1

# Write expired products to .txt file
with open("expired_products.txt", "w") as expired_products_txt:
        expired_products_txt.write("The following products have expired: \n")
        x = 0
        while x < len(expired_products):
            days_since_expiry = datetime.today() - datetime.strptime(expired_products[x][2], "%Y-%m-%d")
            expiry_delta = days_since_expiry.days
            expired_products_txt.write("Product: " + expired_products[x][1] + "  |  Expired: " + expired_products[x][2] + " (" + str(expiry_delta) + " days ago)\n")
            x += 1
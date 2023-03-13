import csv
import sys
from datetime import date

product_delete = input("Enter the name of the product you'd like to delete: ")
all_products_list = []
all_products_amended = []
all_products_deleted = []


# Import all_products.csv to Python list
with open("all_products.csv", "r") as all_products:
    reader = csv.reader(all_products)
    for row in reader:
        all_products_list.append(row)

# Check that product exists
product_match = 0
product = 0

while product < len(all_products_list):
    if all_products_list[product][1] == product_delete:
        product_match += 1
    product += 1

if product_match == 0:
    sys.exit("Product not found.")

# Delete required row and add to deleted list
i = 0
while i < len(all_products_list):
    product_name = all_products_list[i][1]
    if product_name != product_delete:
        all_products_amended.append(all_products_list[i])
    if product_name == product_delete:
        all_products_deleted.append(all_products_list[i])
    i += 1

# Rewrite to all_products.csv
with open("all_products.csv", "w", newline="") as all_products:
    writer = csv.writer(all_products)
    x = 0
    while x < len(all_products_amended):
        writer.writerow([all_products_amended[x][0], all_products_amended[x][1], all_products_amended[x][2]])
        x += 1

# Check if archived_products.csv exists, create file if doesn't exist
try:
    with open("archived_products.csv", "r") as archived_products_exists:
        reader = csv.reader(archived_products_exists)
except:
    with open("archived_products.csv", "w", newline="") as archived_products:
        writer = csv.writer(archived_products)
        writer.writerow(["Entry date", "Product", "Expiry date", "Archive date"])

# Add archived product to archived_products.csv
with open("archived_products.csv", "a", newline="") as archived_products:
    writer = csv.writer(archived_products)
    writer.writerow([all_products_deleted[0][0], all_products_deleted[0][1], all_products_deleted[0][2], date.today()])
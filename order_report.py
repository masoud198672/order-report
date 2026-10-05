import csv
with open("order.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    orders = list(reader)
    
# Keep only rows with a valid numeric amount
clean_orders = []
skipped = 0

for row in orders:
    try:
        int(row["amount"])
        clean_orders.append(row)
    except (ValueError, TypeError, KeyError):
        skipped = skipped + 1

orders = clean_orders
print("Skipped rows:", skipped)

if not orders:
    print("No valid orders found")
    raise SystemExit

big_orders = []
threshold = int(input("Enter threshold: "))
for order in orders:
    amount = int(order["amount"])
   

    if amount > threshold:
        big_orders.append(order)
big_orders.sort(key=lambda order: int(order["amount"]), reverse=True)

for order in big_orders:
    print(order["customer"], order["amount"])

total = 0

for order in big_orders:
    total = total +int(order["amount"])

print(total)
# Summary of all orders, not only the big ones
print("Number of orders:", len(orders))
print("Number of big orders:", len(big_orders))
big_order_percentage = len(big_orders) / len(orders) * 100
print("Big order percentage:", big_order_percentage, "%")

all_total = 0

for order in orders:
    all_total = all_total + int(order["amount"])
print("Total of all orders:", all_total)
with open("summary.csv", "w", newline="", encoding="utf-8-sig") as out:
    writer = csv.writer(out)

    writer.writerow([
        "total_orders",
        "big_orders",
        "big_order_percentage",
        "total_sales",
        "big_orders_total"
    ])

    writer.writerow([
        len(orders),
        len(big_orders),
        big_order_percentage,
        all_total,
        total
    ])

print("Saved summary.csv")

# Write the big orders to a CSV file that Google Sheets can import
with open("big_orders.csv", "w", newline="", encoding="utf-8-sig") as out:
    writer = csv.writer(out)
    writer.writerow(["customer", "amount"])

    for order in big_orders:
        writer.writerow([order["customer"], order["amount"]])

print("Saved big_orders.csv")

# Total per customer, sorted from highest to lowest
customer_totals = {}

for order in orders:
    name = order["customer"]
    customer_totals[name] = customer_totals.get(name, 0) + int(order["amount"])

sorted_totals = sorted(customer_totals.items(), key=lambda item: item[1], reverse=True)

with open("customer_totals.csv", "w", newline="", encoding="utf-8-sig") as out:
    writer = csv.writer(out)
    writer.writerow(["customer", "total"])
    writer.writerows(sorted_totals)

print("Saved customer_totals.csv")
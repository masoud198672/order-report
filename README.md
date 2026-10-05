# Order Report

A small Python tool that reads a CSV file of orders and builds a sales report.

## What it does
- Skips rows with a missing or invalid amount and reports how many were skipped
- Asks for a threshold and lists the big orders, from highest to lowest
- Shows the number of orders, the number of big orders and their percentage
- Calculates the total per customer
- Saves three files: `summary.csv`, `big_orders.csv` and `customer_totals.csv`

## How to run
1. Put your orders in `order.csv` with two columns: `customer` and `amount`
2. Run: `python order_report.py`
3. Enter the threshold when asked (for example `1000000`)

## Example input
 
    customer,amount
    Ali,1200000
    Reza,2300000
    Sara,450000

## Built with
Python (standard library only: `csv`)

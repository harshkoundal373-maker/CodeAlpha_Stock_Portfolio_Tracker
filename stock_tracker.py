print("=" * 50)
print("      STOCK PORTFOLIO TRACKER")
print("=" * 50)

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300,
    "AMZN": 200,
    "META": 280
}

print("\nAvailable Stocks:")
for stock in stocks:
    print(stock)

stock_name = input("\nEnter Stock Name: ").upper()
quantity = int(input("Enter Quantity: "))

if stock_name in stocks:

    price = stocks[stock_name]
    total = price * quantity

    print("\n" + "=" * 50)
    print("PORTFOLIO SUMMARY")
    print("=" * 50)

    print("Stock Name      :", stock_name)
    print("Price Per Share :", price)
    print("Quantity        :", quantity)
    print("Total Investment:", total)

    if total > 1000:
        print("Investment Level: High")
    else:
        print("Investment Level: Normal")

else:
    print("\nStock not found!")
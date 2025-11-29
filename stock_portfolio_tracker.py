stock_prices = {
    "APPLE": 180,
    "TESLA": 250,
    "ALPHABET": 140,
    "MICROSOFT": 210,
    "AMAZON": 170
}

total_investment = 0
portfolio = {}

print("***************")
print("  WELCOME TO THE STOCK PORTFOLIO TRACKER  ")
print("***************\n")

print("Available Stocks and their Prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")
print("\n")

num = int(input("How many different stocks do you want to add? "))

for i in range(num):
    print(f"\n--- Stock {i+1} ---")
    
    while True:  # Loop until user enters correct stock name
        name = input("Enter the stock name (e.g. APPLE): ").strip().upper()
        if name in stock_prices:
            break
        else:
            print("This stock is not in the list. Please check the name!")
            print("Available Stocks:", ", ".join(stock_prices.keys()))
    
    quantity = int(input("Enter the quantity: "))
    price = stock_prices[name]
    cost = price * quantity
    total_investment += cost
    portfolio[name] = quantity
    
    print(f"✔ {name} added successfully!")
    print(f"   Price per share: ${price}")
    print(f"   Quantity: {quantity}")
    print(f"   Cost for this stock: ${cost}")

print("\n==========================================")
print("           PORTFOLIO SUMMARY              ")
print("==========================================")

for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    print(f"{stock}: {qty} shares  | Value: ${value}")

print("------------------------------------------")
print(f"TOTAL INVESTMENT VALUE = ${total_investment}")
print("==========================================\n")

print("Thank you for using the Stock Portfolio Tracker!")
print("Have a profitable day!")
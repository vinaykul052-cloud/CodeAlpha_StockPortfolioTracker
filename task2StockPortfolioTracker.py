# Task 2: Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 130,
    "MSFT": 310
}

portfolio = {}  # Store user input stocks

# Input loop
while True:
    stock = input("Enter stock name (or DONE to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found in price list. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        if quantity <= 0:
            print("Quantity must be positive.")
            continue
        portfolio[stock] = quantity
    except ValueError:
        print("Invalid input. Enter a number.")
        continue

# Calculate total investment
total_investment = 0
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    total_investment += value
    print(f"{stock}: {qty} × {price} = {value}")

print(f"\nTotal Investment: {total_investment}")

# Optional: Save to text file
save_file = input("\nDo you want to save the portfolio to a file? (yes/no): ").lower()
if save_file == "yes":
    with open("portfolio.txt", "w") as f:
        f.write("Your Portfolio:\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = qty * price
            f.write(f"{stock}: {qty} × {price} = {value}\n")
        f.write(f"\nTotal Investment: {total_investment}\n")
    print("Portfolio saved to portfolio.txt")
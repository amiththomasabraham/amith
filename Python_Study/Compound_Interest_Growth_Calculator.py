amount = float(input("Enter initial investment amount: "))
rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter number of years: "))

print("Year\tAmount")

for year in range(1, years + 1):
    amount = amount + (amount * rate / 100)
    print(year, "\t", round(amount, 2))

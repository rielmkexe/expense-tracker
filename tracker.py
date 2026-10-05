# Project: Expense Tracker - Installment 3
# Author: Kimberly L. Gabriel
# Description: Accepts inputs for expenses, calculates running subtotal, tax, grand total, budget check, and outputs a formatted summary.

# Banners and separator lines using single-character multiplication
banner_equal = "=" * 40
banner_dash = "-" * 40

# Top Banner & Main Menu
print(banner_equal)
print("\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print(banner_dash)

print("MAIN MENU")
print(" [1] Add an expense\t(coming soon)")
print(" [2] View all expenses\t(coming soon)")
print(" [3] Show total spent\t(coming soon)")
print(" [4] Exit\t\t(coming soon)")
print(banner_dash)

# Prompt for user name and print personal greeting
name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

# Initialize running subtotal at 0
subtotal = 0

# Prompt for expenses and update subtotal right after each read
item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

# Calculate average from subtotal
average = subtotal / 2

# Prompt for tax percentage and budget
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

# Calculate tax, grand total, budget status, and remaining budget
tax = subtotal * (tax_percent / 100)
total = subtotal + tax
over_budget = total > budget
left = budget - total

# Summary Section
print(banner_dash)
print("SUMMARY")
print(f" - {item1}:\t\t${amount1}")
print(f" - {item2}:\t\t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Grand total:\t${total}")
print(f"Over budget?\t{over_budget}")
print(f"Left in budget:\t${left}")

# Footer
print(banner_dash)
print("Made by: Kimberly L. Gabriel | Installment 3")
print(banner_equal)
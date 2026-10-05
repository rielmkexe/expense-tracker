# Project: Expense Tracker - Installment 2
# Author: Kimberly L. Gabriel
# Description: Accepts user input for name and expenses, calculates total and average, and prints a summary.

# Banners and separator lines using single-character multiplication
banner_equal = "=" * 40
banner_dash = "-" * 40

# Top Banner & Main Menu
print(banner_equal)
print("\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print(banner_dash)

print("MAIN MENU")
print("[1] Add an expense\t(coming soon)")
print("[2] View all expenses\t(coming soon)")
print("[3] Show total spent\t(coming soon)")
print("[4] Exit\t\t(coming soon)")
print(banner_dash)

# Prompt for user name and print personal greeting
name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

# Prompt for expenses and amounts using required variable names
item1 = input("First expense? ")
amount1 = float(input("Amount? "))

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

# Compute total and average
total = amount1 + amount2
average = total / 2

# Print Summary Section with tab-aligned values and no '+' joining
print(banner_dash)
print("SUMMARY")
print(f"{item1}:\t\t${amount1}")
print(f"{item2}:\t\t${amount2}")
print(f"Total spent:\t${total}")
print(f"Average:\t${average}")

# Footer
print(banner_dash)
print("Made by: Kimberly L. Gabriel | Installment 2")
print(banner_equal)
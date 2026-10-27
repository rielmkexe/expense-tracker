# Project: Expense Tracker - Installment 5
# Author: Kimberly L Gabriel
# Description: Interactive expense tracker featuring a continuous menu loop, expense counting, running subtotal calculation, tax evaluation, and budget verdict checking.

def classify_expense(amount: float) -> str:
    """Classifies an expense amount into its size category with two leading spaces."""
    if amount > 200:
        return "  are you sure?\n  Huge expense."
    elif amount > 100:
        return "  Big expense."
    elif amount > 50:
        return "  Moderate expense."
    else:
        return "  Small expense."


def evaluate_budget_verdict(grand_total: float, budget: float) -> str:
    """Evaluates the grand total against the budget and returns the verdict string."""
    if grand_total > budget:
        over_budget = grand_total - budget
        return f"Over budget by ${over_budget:.1f}!"
    elif grand_total > (0.90 * budget):
        remaining = budget - grand_total
        return f"Careful: only ${remaining:.1f} left."
    else:
        remaining = budget - grand_total
        return f"Within budget. ${remaining:.1f} left."


def run_tracker() -> None:
    """Executes the main interactive menu-driven Expense Tracker application."""
    # Banner printed once at start
    banner_equal = "=" * 40
    banner_dash = "-" * 40

    print(banner_equal)
    print("\tEXPENSE TRACKER")
    print("\tKnow where your money goes.")
    print(banner_dash)

    # Initial Setup - Asked exactly once
    name = input("What's your name? ")
    tax_percent = float(input("Tax rate %? "))
    budget = float(input("Your budget? "))
    print(f"Welcome, {name}!\n")

    # Tracking counters
    subtotal = 0.0
    count = 0

    # Continuous Menu Loop
    while True:
        print("MAIN MENU")
        print("[1] Add an expense")
        print("[2] View all expenses (coming soon)")
        print("[3] Show total spent")
        print("[4] Exit")

        choice = input("Choose 1-4:")

        if choice == "1":
            amount = float(input("Amount? "))
            subtotal += amount
            count += 1
            print(classify_expense(amount))

        elif choice == "2":
            print("Coming soon: the tracker can't remember each item yet.")

        elif choice == "3":
            tax_amount = subtotal * (tax_percent / 100.0)
            grand_total = subtotal + tax_amount

            print(f"Expenses:\t| {count}")
            print(f"Subtotal:\t| ${subtotal:.1f}")
            print(f"Tax ({tax_percent:.1f}%):\t| ${tax_amount:.1f}")
            print(f"Grand total:\t| ${grand_total:.1f}\n")

            verdict = evaluate_budget_verdict(grand_total, budget)
            print(verdict)

        elif choice == "4":
            print(f"Goodbye, {name}!")
            print("Made by: Kimberly L Gabriel | Installment 5")
            break

        else:
            print("Please choose 1, 2, 3 or 4.")

        print()  # Spacer between iterations


if __name__ == "__main__":
    run_tracker()
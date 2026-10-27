"""
# Expense Tracker - Installment 4: The Tracker Makes Decisions
# Made by: Kimberly L. Gabriel | Installment 4
#
# Description:
# Advanced Python implementation for Laboratory 4. Evaluates individual expense
# sizes, checks consecutive high expenses, computes total costs with tax,
# and displays a dynamic budget verdict.
"""

from typing import Tuple


def classify_expense(amount: float) -> str:
    """Classifies an expense amount into its corresponding size category.

    Args:
        amount (float): The cost of the expense.

    Returns:
        str: Formatted exact size message with two leading spaces.
    """
    if amount > 200:
        return "  are you sure?\n  Huge expense."
    elif amount > 100:
        return "  Big expense."
    elif amount > 50:
        return "  Moderate expense."
    else:
        return "  Small expense."


def evaluate_budget_verdict(grand_total: float, budget: float) -> str:
    """Evaluates the grand total against the budget and produces the exact verdict message.

    Args:
        grand_total (float): The calculated total cost including tax.
        budget (float): The user's target budget limit.

    Returns:
        str: exact budget verdict message (never displaying a negative number).
    """
    if grand_total > budget:
        over_budget_amount = grand_total - budget
        return f"Over budget by ${over_budget_amount:.1f}!"
    elif grand_total > (0.90 * budget):
        remaining = budget - grand_total
        return f"Careful: only ${remaining:.1f} left."
    else:
        remaining = budget - grand_total
        return f"Within budget. ${remaining:.1f} left."


def run_tracker() -> None:
    """Executes the main Expense Tracker program sequence."""
    # Main menu header display
    print("EXPENSE TRACKER")
    print("Know where your money goes.")
    print("=========================")
    print("MAIN MENU")
    print("[1] Add an expense\n    (coming soon)")
    print("[2] View all expenses\n    (coming soon)")
    print("[3] Show total spent\n    (coming soon)")
    print("[4] Exit\n    (coming soon)\n")

    # User identification
    user_name = input("What's your name? ")
    print(f"Welcome, {user_name}! Let's log two expenses.\n")

    # Expense 1 Input & Classification
    exp1_name = input("First expense? ")
    exp1_amount = float(input("Amount? "))
    print(classify_expense(exp1_amount))

    # Expense 2 Input & Classification
    exp2_name = input("Second expense? ")
    exp2_amount = float(input("Amount? "))
    print(classify_expense(exp2_amount))

    # Check for consecutive big expenses (> 100)
    if exp1_amount > 100 and exp2_amount > 100:
        print("  slow down!\n  Two big expenses in a row")

    # Tax & Budget Input
    tax_rate = float(input("Tax rate %? "))
    budget = float(input("Your budget? "))

    # Financial Calculations
    subtotal = exp1_amount + exp2_amount
    average = subtotal / 2.0
    tax_amount = subtotal * (tax_rate / 100.0)
    grand_total = subtotal + tax_amount

    # Summary Display (Tab-aligned format matching specification)
    print("\nSUMMARY")
    print(f"{exp1_name}:\t\t| ${exp1_amount:.1f}")
    print(f"{exp2_name}:\t\t| ${exp2_amount:.1f}")
    print(f"Subtotal:\t| ${subtotal:.1f}")
    print(f"Average:\t| ${average:.1f}")
    print(f"Tax ({tax_rate:.1f}%):\t| ${tax_amount:.1f}")
    print(f"Grand total:\t| ${grand_total:.1f}\n")

    # Verdict Line
    verdict = evaluate_budget_verdict(grand_total, budget)
    print(verdict)
    print()

    # Footer
    print("Made by: Kimberly L. Gabriel | Installment 4")


if __name__ == "__main__":
    run_tracker()
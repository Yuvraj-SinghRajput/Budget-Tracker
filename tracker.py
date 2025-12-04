# ----------------------------------------------------
#        PERFECTLY ALIGNED BUDGET TRACKER
# ----------------------------------------------------

def print_header():
    print("\n" + "═" * 60)
    print(" PERSONAL MONTHLY BUDGET TRACKER ".center(60))
    print("═" * 60 + "\n")


def get_positive_int(message):
    while True:
        try:
            value = input(message)
            if value.strip() == "":
                return 0
            value = int(value)
            if value < 0:
                print("   ⚠ Enter a non-negative value.\n")
            else:
                return value
        except ValueError:
            print("   ❌ Numbers only!\n")


def format_currency(amount):
    sign = "-" if amount < 0 else ""
    amount = abs(amount)
    return f"{sign}₹{amount:,}"


def draw_bar(percent):
    """Stable bar width = 12 characters."""
    width = 12
    filled = int((percent / 100) * width)
    return "█" * filled + " " * (width - filled)


def print_expense_table(expenses, income, total, saving):
    print("┌" + "─" * 60 + "┐")
    print("│" + " EXPENSE BREAKDOWN ".center(60) + "│")
    print("├" + "─" * 60 + "┤")

    print(f"│ {'Category':<18} {'Amount':>12}   {'%Income':>8}   {'Usage':<12} │")
    print("├" + "─" * 60 + "┤")

    for cat, amt in expenses.items():
        pct = (amt / income * 100) if income > 0 else 0
        bar = draw_bar(pct)
        print(f"│ {cat:<18} {format_currency(amt):>12}   {pct:>7.1f}%   {bar:<12} │")

    print("├" + "─" * 60 + "┤")
    print(f"│ {'Total Expenditure':<18} {format_currency(total):>12}                     │")
    print(f"│ {'Remaining / Saving':<18} {format_currency(saving):>12}                     │")
    print("└" + "─" * 60 + "┘\n")


def print_saving_analysis(saving, income):
    print("┌" + "─" * 60 + "┐")
    print("│" + " SUMMARY ".center(60) + "│")
    print("├" + "─" * 60 + "┤")

    if saving > 0:
        pct = saving / income * 100
        print(f"│  ✅  Well done — you're under budget!{' ' * 29}│")
        print(f"│      Saved {format_currency(saving)} ({pct:.1f}% of income).{' ' * 23}│")
        print("│" + " " * 60 + "│")

        if pct < 10:
            msg = "Tip: Try to save at least 10% of your income."
        elif pct < 20:
            msg = "Good! Aim for 20% savings if possible."
        else:
            msg = "Excellent! You are saving very well."

        print("│  💡 " + msg.ljust(54) + "│")

    elif saving == 0:
        print("│  ⚠  You broke even — no savings this month.              │")
        print("│  💡 Try cutting small recurring expenses.                │")

    else:
        print(f"│  ❌  Overspent by {format_currency(-saving)}.{' ' * 28}│")
        print("│  💡 Reduce non-essential expenses.                       │")

    print("├" + "─" * 60 + "┤")
    print("│ Note: Press ENTER to enter 0 for any item.               │")
    print("└" + "─" * 60 + "┘\n")


def main():
    print_header()

    income = get_positive_int("Enter your Monthly Income (₹): ")

    print("\nEnter monthly expenses (press Enter for 0):\n")

    expenses = {
        "Rent": get_positive_int("🏠 Rent (₹): "),
        "Clothing": get_positive_int("👕 Clothing (₹): "),
        "Child Education": get_positive_int("📚 Child Education (₹): "),
        "Salon": get_positive_int("💇 Salon (₹): "),
        "Electricity": get_positive_int("💡 Electricity (₹): "),
        "Mobile Recharge": get_positive_int("📱 Mobile Recharge (₹): "),
        "Gas": get_positive_int("⛽ Gas (₹): "),
        "Food": get_positive_int("🍽 Food (₹): "),
    }

    total = sum(expenses.values())
    saving = income - total

    print_expense_table(expenses, income, total, saving)
    print_saving_analysis(saving, income)


if __name__ == "__main__":
    main()

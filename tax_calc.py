def calculate_tax(income):
    if income > 5000000:
        return income * 0.35
    elif income > 2000000:
        return income * 0.3
    elif income > 1000000:
        return income * 0.25
    elif income > 750000:
        return income * 0.2
    elif income > 500000:
        return income * 0.15
    elif income > 300000:
        return income * 0.1
    elif income > 150000:
        return income * 0.05
    else:
        return 0

print(f"Tax = {calculate_tax(235000)} Baht")
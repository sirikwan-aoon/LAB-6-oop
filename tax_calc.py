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

def calculate_deduction(type): #just example, not all type
    if type == "self":
        return 60000
    elif type == "social security":
        return 9000
    elif type == "life insurance":
        return 100000
    elif type == "health insurance":
        return 25000

my_income = 1000000
deductions = [
    calculate_deduction("self"),
    calculate_deduction("social security"),
    calculate_deduction("life insurance")
]

total_deduction = sum(deductions)

net_income = my_income - total_deduction
if net_income < 0: net_income = my_income

print(f"Tax = {calculate_tax(my_income)} Baht")
print(f"Deduction = {total_deduction} Baht")
print(f"Tax after deductions = {calculate_tax(net_income)} Baht")
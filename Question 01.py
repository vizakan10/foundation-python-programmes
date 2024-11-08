gross_salary = float(input("Enter your monthly gross salary: "))

def calculate_tax(gross_salary):
    if gross_salary <= 99999:
        return 0
    elif gross_salary <= 150000:
        return (gross_salary - 99999) * 0.05
    elif gross_salary <= 250000:
        return (50000 * 0.05) + (gross_salary - 150000) * 0.10
    else:
        return (50000 * 0.05) + (100000 * 0.10) + (gross_salary - 250000) * 0.12

tax = calculate_tax(gross_salary)
net_salary = gross_salary - tax
net_salary = float(net_salary)

print("Monthly Net Salary:", net_salary)
 
 

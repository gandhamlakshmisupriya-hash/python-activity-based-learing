
# Employee Payroll and Deduction Analysis

print("=== Employee Payroll System ===")

name = input("Enter employee name: ")
basic = float(input("Enter basic pay: Rs. "))
allowances = float(input("Enter allowances: Rs. "))
overtime_hours = float(input("Enter overtime hours: "))
overtime_rate = float(input("Enter overtime rate per hour: Rs. "))
incentives = float(input("Enter incentives: Rs. "))

if (basic < 0 or allowances < 0 or overtime_hours < 0
        or overtime_rate < 0 or incentives < 0):
    print("Invalid salary details.")

else:
    overtime = overtime_hours * overtime_rate

    gross = basic + allowances + overtime + incentives

    # Progressive deductions
    if gross <= 20000:
        deduction = gross * 0.05
    elif gross <= 50000:
        deduction = 20000 * 0.05 + (gross - 20000) * 0.10
    else:
        deduction = (
            20000 * 0.05
            + 30000 * 0.10
            + (gross - 50000) * 0.15
        )

    net_salary = gross - deduction

    print("\n========== SALARY STATEMENT ==========")
    print("Employee Name       :", name)
    print("Basic Pay           : Rs.", round(basic, 2))
    print("Allowances          : Rs.", round(allowances, 2))
    print("Overtime Pay        : Rs.", round(overtime, 2))
    print("Incentives          : Rs.", round(incentives, 2))
    print("--------------------------------------")
    print("Gross Salary        : Rs.", round(gross, 2))
    print("Total Deduction     : Rs.", round(deduction, 2))
    print("Net Salary          : Rs.", round(net_salary, 2))
    print("======================================")

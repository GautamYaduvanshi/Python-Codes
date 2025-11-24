def calc_tax(taxable):
    tax = 0
    if taxable <= 250000:
        tax = 0
    elif taxable <= 500000:
        tax = (taxable - 250000) * 0.05
    elif taxable <= 1000000:
        tax = 250000 * 0.05 + (taxable - 500000) * 0.20
    else:
        tax = 250000 * 0.05 + 500000 * 0.20 + (taxable - 1000000) * 0.30
    return tax

gross = float(input("Enter gross income: "))

print("\nEnter amounts invested/deducted:")
mf = float(input("Mutual funds: "))
nps = float(input("NPS: "))
shares = float(input("Shares: "))
loan = float(input("House loan interest: "))
fd = float(input("Fixed deposits: "))
ulip = float(input("ULIP: "))
ins = float(input("Insurance: "))
nsc = float(input("NSC: "))
ppf = float(input("PPF: "))

total_deduction = mf + nps + shares + loan + fd + ulip + ins + nsc + ppf

taxable_income = gross - total_deduction
if taxable_income < 0:
    taxable_income = 0

tax = calc_tax(taxable_income)

print("\nTotal Deductions:", total_deduction)
print("Taxable Income:", taxable_income)
print("Income Tax Payable: Rs.", tax)

# Name: Jamaica C. Palillo
# Section: BSCPE 1-5

# Exercise 12: Calculate income tax for the given income by adhering to the rules below

income = 65000
tax_payable = 0

if income <= 10000:
    tax_payable=0

elif income <= 20000:
    x = income - 10000
    tax_payable = x *10 / 100

else:
    tax_payable = 0 
    tax_payable = 1000 * 10/ 100
    tax_payable += (income - 20000) * 20/100

print ("Total Income: ", "₱",  income)
print ("Tax Payable:  ", "₱", tax_payable)

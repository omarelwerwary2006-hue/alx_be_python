monthlyincome = float(input("Enter your monthly income: "))
monthlyexpenses = float(input("Enter your total monthly expenses: "))

monthlysavings = monthlyincome-monthlyexpenses

print(f"Your monthly savings are: {monthlysavings}")

Projected_savings = monthlysavings*12+monthlysavings*12*0.05

print(f"Projected savings after one year, with interest, is: {Projected_savings}")

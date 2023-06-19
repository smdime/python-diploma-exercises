#storing numbers - making a loan calculator
#Have the user enter the cost of the loan,
#interest rate, and the number of years for the loan
Loan = float(input("Enter loan amount : "))

#interest rate is converted from a percentage to a decimal number
interestRate = float(input("Enter interest rate (in percent) : ")) / 100.0
numberOfPayments = int(input("Enter number of payments : "))

#Calculate monthly payments with the ff formula: M = L[i(1+i)n] / [(1+i)n-1]
monthlyPayment = Loan*(interestRate*(1+interestRate)*numberOfPayments) / ((1+interestRate)*numberOfPayments-1)

#Convert interestRate to a float number
print("Your monthly payment would be : %.2f" % monthlyPayment)

#re-input monthlyPayment using the updated format syntax
print("Your monthly payment would be : {0:.2f}" .format(monthlyPayment))
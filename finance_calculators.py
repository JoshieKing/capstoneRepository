import math

# Asking the user whether they want to select an investment calculation or a bond calculation
print("Choose either 'investment' or 'bond' from the menu below to proceed:\n")
print("investment     - to calculate the amount of interest you'll earn on interest.")
calculating = input("bond           - to calculate the amount you'll have to pay on a home loan.\n").lower()

# If 'investment' is selected
# Ask the user for their deposit amount, interest rate, number of years they're investing for and what interest they want
# Divide the rate variable to get the interest rate for the calculation and store it in the variable r
# P = deposit, t = years

# If 'simple' is selected will then use the inputs received from the user to calculate the total amount at simple interest
# Will use the simple interest calculation to calculate it: A = P(1+r*t)

# If 'compound' is selected will then use the inputs received from the user to calculate the total amount at compound interest
# Will use the compound interest calculation to calculate it with the help of the power function from the math module: A = P(1+r)^t

# If the input for the interest variable is not the set ones it will give an error

if calculating == "investment":
    deposit = float(input("Enter the amount you will be depositing: R"))
    rate = float(input("Enter the interest rate without the % symbol: "))
    years = float(input("Enter the amount of years you will be investing for: "))
    interest = input("Do you want to use simple interest or compound interest? ").lower()
    r = rate / 100

    if interest == "simple" or interest == "simple interest":
        total_amount = deposit * (1 + r * years)
        print(f"\nThe total amount you will have at the end of your investment with simple interest will equal to R{round(total_amount, 2)}.")

    elif interest == "compound" or interest == "compound interest":
        total_amount = deposit * math.pow((1 + r), years)
        print(f"\nThe total amount you will have at the end of your investment with compound interest will equal to R{round(total_amount, 2)}.")

    else:
        print("\nError! Interest type unacceptable. Please try again")

# If 'bond' is selected
# Ask the user for the house's value, interest rate and the number of months it will take to repay the bond
# Will use the bond repayment formula: x = (i*P)/(1 - (1+i)^(-n))
# P = house_value, n = months
# to get i will divide the rate by 100 and then divide that amount by 12 for the monthly interest
elif calculating == "bond":
    house_value = float(input("Enter the current value of the house: R"))
    rate = float(input("Enter the interest rate without the % symbol: "))
    months = float(input("Enter the number of months it will take to repay the bond: "))
    i = (rate / 100) / 12

    monthly_repayment = (i * house_value) / (1 - math.pow((1 + i), -months))
    print(f"\nThe amount you will have to pay each month is equal to R{round(monthly_repayment, 2)}.")

else:
    print("\nError! Invalid selection. Please try again.")

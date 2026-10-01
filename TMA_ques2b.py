def deposit_input():
    # Ask for initial deposit, return value if greater than 0, else None
    deposit = int(input("Enter initial deposit amount: "))
    if deposit < 0:
        return None
    return deposit

def age_input():
    # Ask for the age at deposit, return value if within 1 to 100, else None
    age = int(input ("Enter age of initial deposit: "))
    if age < 1 or age > 100:
        return None
    return age 

def rate_input():
    # Ask for the interest rate in %, return value within 0 to 10, else None
    rate = int(input("Enter interest rate in %: "))
    if rate < 0 or rate > 10:
        return None
    return rate

def calc_interest(balance, rate):
    # Calculate the interest of the deposit with varying rate depending on the amount
    if balance <= 30000:
        # Initial deposit <= 30000, use default rate calculation
        interest = balance * rate / 100 # Sum of the interest
    elif balance <= 60000:
        # Initial deposit <= 60000,use default rate calculation for initial 30000 the rest 1% less than initial rate
        tier1 = 30000 * rate / 100 # First 30000
        tier2 = (balance - 30000) * (rate - 1) / 100 # Remainder, rate -1
        interest = tier1 + tier2 # Sum of the interest
    else:
        # Initial deposit greater than 60000, First 30000 default rate, Next 30000 rate -1, Remainder rate -2
        tier1 = 30000 * rate / 100 # First 30000
        tier2 = 30000 * (rate - 1) / 100 # Second 30000, rate -1
        tier3 = (balance - 60000) * (rate - 2) / 100 # Remainder, rate -2
        interest = tier1 + tier2 + tier3 # Sum of the interest
    return (interest)

def planA_output(deposit, age, rate):
    # Print each year's balance, interest and end-of-year balance up to age 70.
    print("Year           Balance  +  Interest  =  End of Year")
    balance = deposit
    while age <= 70:
        interest = calc_interest(balance, rate)
        eoy = balance + interest # Total sum of the balance and interest per year
        print(f"At age {age}    {round(balance):>8,}    {round(interest):>8,}    {round(eoy):>14,}")
        balance = eoy # The current year balance is next year starting balance
        age += 1 # Increment age to output the planA output till 70

def main():
    # Read and validate the inputs, stopping at the first error, then print the output table.
    deposit = deposit_input()
    if deposit is None:
        print("Error! Amount must be within 0 to $30,000") #Error message for initial deposit input
        return

    age = age_input()
    if age is None:
        print("Error! Age must be within 1 to 100")#Error message for age input
        return

    rate = rate_input()
    if rate is None:
        print("Error! Interest rate must be within 0 to 10%")#Error message for interest rate input
        return

    planA_output(deposit, age, rate)

if __name__ == "__main__":
    main()
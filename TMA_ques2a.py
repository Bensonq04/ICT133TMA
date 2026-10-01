def deposit_input():
    # Ask for initial deposit, return value if within 0 to 30000, else None
    deposit = int(input("Enter initial deposit amount: "))
    if deposit < 0 or deposit > 30000: 
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

def planA_output(deposit, age, rate):
    # Print each year's balance, interest and end-of-year balance up to age 70.
    print("Year           Balance  +  Interest  =  End of Year")
    balance = deposit
    while age <= 70:
        interest = balance * rate / 100 # Interest calculation 
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
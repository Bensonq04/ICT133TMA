def start_payout_age_input():
    # Ask for age of first payout, return value if within 65 to 70, else None
    start_age = int(input("Enter age of first payout: "))
    if start_age < 65 and start_age >70:
        return None
    return start_age

def yearly_payout_amount_input():
    # Ask for the yearly payout amount, return value if greater than 0, else None
    yearly_payout = int(input("Enter yearly payout amount: "))
    if yearly_payout <0:
            return None
    return yearly_payout

def deposit_input():
    # Ask for initial deposit, return value if within 0 to 30000, else None
    deposit = int(input("Enter initial deposit amount: "))
    if deposit < 0:
        return None
    return deposit

def age_input():
    age = int(input ("Enter age at initial deposit: "))
    if age < 1 or age > 100:
        return None
    return age 

def rate_input():
    rate = int(input("Enter interest rate in %: "))
    if rate < 0 or rate > 10:
        return None
    return rate

def calc_interest(balance, rate):
    if balance <= 30000:
        interest = balance * rate / 100
    elif balance <= 60000:
        tier1 = 30000 * rate / 100
        tier2 = (balance - 30000) * (rate - 1) / 100
        interest = tier1 + tier2
    else:
        tier1 = 30000 * rate / 100
        tier2 = 30000 * (rate - 1) / 100
        tier3 = (balance - 60000) * (rate - 2) / 100
        interest = tier1 + tier2 + tier3
    return interest

def planA_output(deposit, age, rate,start_age):
    print("Year           Balance  +  Interest  =  End of Year")
    balance = deposit
    while age <= 70 and age < start_age:
        interest = calc_interest(balance, rate)
        eoy = balance + interest
        print(f"At age {age}    {round(balance):>8,}    {round(interest):>8,}    {round(eoy):>14,}")
        balance = eoy
        age += 1
    return balance, age 

def planA_payout(balance, age, rate, yearly_payout):
    print("Year           Payout   Start of Year   Interest")
    while balance >= yearly_payout:
        remaining = balance - yearly_payout
        interest = calc_interest(remaining, rate)
        print(f"At age {age}    {yearly_payout:>8,}    {round(remaining):>8,}    {round(interest):>11,}")
        balance = remaining + interest
        age += 1
    print(f"Last payout is ${round(balance):,} at age {age}")
    
def main():
    start_age = start_payout_age_input()
    if start_age is None:
        print("Error! Age must be within ages 65 to 70")
        return
    
    yearly_payout = yearly_payout_amount_input()
    if yearly_payout is None:
        print("Error! Yearly payout must greater than $0 ")
        return
        
    deposit = deposit_input()
    if deposit is None:
        print("Error! Amount must be within 0 to $30,000")
        return

    age = age_input()
    if age is None:
        print("Error! Age must be within 1 to 100")
        return

    rate = rate_input()
    if rate is None:
        print("Error! Interest rate must be within 0 to 10%")
        return
    balance, age = planA_output(deposit, age, rate, start_age)
    print(f"\nStarting payout with ${round(balance):,}")
    planA_payout(balance, age, rate, yearly_payout)

if __name__ == "__main__":
    main()
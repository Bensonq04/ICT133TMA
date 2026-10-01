#Question 1
charger_type = input ("Enter charger type (DC/AC): ") # get charger type from user

if charger_type == "DC":
    # DC Fast flat charging rate
    energy = float(input("Energy delivered (kWh): "))
    amount = 0.68 * energy
    print (f"Please pay ${amount:.2f}")
    
elif charger_type == "AC":
    # AC Standard tiered base on energy usage
    energy = float(input("Energy delivered (kWh): "))
    
    if energy < 20: 
        amount = 0.56 * energy # Tier 1 below 20 
    elif energy <= 50: 
        amount = 0.54 * energy # Tier 2 includes 20 to 50
    else: 
        amount = 0.52 * energy # Tier 3 above 50
    print (f"Please pay ${amount:.2f}")
else:
    # Wrong charger type entered
    print ("Wrong charger type, please run the program again")
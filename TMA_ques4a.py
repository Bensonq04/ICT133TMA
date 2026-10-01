import random 

def rancoins() -> int:
    # return a value from range -1 to 6 excluding 0 as dice does not have 0
    return random.choice([-1,1,2,3,4,5,6])    

def openMysteryBox():
    total = 0
    count = 0 
    print (f"Gold Coins: {total}")
    
    while total < 25:
        count = count + 1
        coin = rancoins()
        
        if coin == -1:
            # Reset the total value to 0 
            total = 0
            print("Chest contains: Bomb! Total reset to 0")
            
        elif total + coin > 25:
            # Reset as the total coin is above the maximum range
            print(f"Chest contains: {coin} ... Discarded, try again")
            
        else:
            total += coin
            # Outputs the results 
            print(f"Chest contains: {coin} ... Total now: {total}")
            
    print("Treasure Chest Full!")
    return count
        
if __name__ == "__main__":
    boxes_opened = openMysteryBox()
    print(f"< function returns {boxes_opened} >")
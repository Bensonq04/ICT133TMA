import random 

def rancoins() -> int:
    return random.choice([-1,1,2,3,4,5,6])   

def openMysteryBox():
    total = 0
    count = 0 
    print (f"Gold Coins: {total}")
    
    while total < 25:
        count = count + 1
        coin = rancoins()
        
        if coin == -1:
            total = 0
            print("Chest contains: Bomb! Total reset to 0")
            
        elif total + coin > 25:
            print(f"Chest contains: {coin} ... Discarded, try again")
            
        else:
            total += coin
            print(f"Chest contains: {coin} ... Total now: {total}")

    print("Treasure Chest Full!")    
    return count


def game(boxesOpened):
    for player in range (3): 
        # For each player run the function until is able to fill up the value 
        for chest in range (1,3):
            print (f"---{boxesOpened[player][0]}: Chest {chest}---")
            boxesOpened[player][chest] = openMysteryBox()
            
def show_results(boxesOpened):
    print ("Game Results:")
    totals =[]
    for player in range (3):
        # Addition of the individual chest value according to the players index
        total = boxesOpened[player][1]+boxesOpened[player][2]
        print (f"{boxesOpened[player][0]}: Chest 1 = {boxesOpened[player][1]}, Chest 2 = {boxesOpened[player][2]}, Total = {total}")
        totals.append(total)
    return totals

def find_winners(boxesOpened,totals):
    total_min = min(totals)
    winners = [] 
    for player in range (3):
        if totals[player] == total_min : 
            winners.append(boxesOpened[player][0])
    return winners, total_min

def main():
    boxesOpened = [ ["Lara", 0, 0], ["Nico", 0, 0], ["Zane", 0, 0] ]
    
    game(boxesOpened)
    totals = show_results(boxesOpened)
    winners, total_min = find_winners(boxesOpened, totals)
    
    if len(winners) == 1:
        # Output one winner
        print (f"Winner: {winners[0]} with {total_min} boxes!")
    else:
        # Output multiple winner if there is a draw
        print (f"It's a draw between: {', '.join(winners)} with {total_min} boxes!")

if __name__ == "__main__":
    main()
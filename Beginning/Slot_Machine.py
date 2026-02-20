import random

def spin_Row():
    symbols = ['🍉','🍇','🍓','🍎','🍋']
    results = []
    for x in range(3):
        results.append(random.choice(symbols))
    return results    
    
def Print_Row(row):
    print("**************************")
    print("   ".join(row))
    print("**************************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍉':
            return bet * 2
        elif row[0] == '🍇':
            return bet * 5
        elif row[0] == '🍓':
            return bet * 10
        elif row[0] == '🍎':
            return bet * 15
        elif row[0] == '🍋':
            return bet * 20
    return 0  # Dedented: Now returns 0 for non-matches
        
def main():
    balance = 100
    print("--------------------")
    print("-----Welcome to Python slots-----")
    print("Symbols : 🍉 🍇 🍓 🍎 🍋") 
    print("--------------------")   
    while balance > 0:  
        print(f"Current Balance : ${balance}") 
    
        bet = input("Place your bet : ")  # Added space after =
    
        if not bet.isdigit():
            print("Please enter a valid number")
            continue
    
    
        bet = int(bet)
    
        if bet > balance:
            print("Insufficient Balance..")
            continue
        if bet <= 0:
            print("Bet must be greater than zero!")
            continue
    
        balance -= bet    
        row = spin_Row()
        print("Spinning....")
        Print_Row(row)
        
        payout = get_payout(row, bet)
        
        if payout > 0:
            print(f"You Won ${payout}")
        else:
            print("sorry you lost this round")   
            
        balance += payout     
        play_again = input("do you want to spin(Y/N):").upper()
        
        if play_again != 'Y':
            break

    # Moved these outside the loop: Now print only once at the end
    print(f"Your final Balance : ${balance}")
    print("-------------------- GAME-OVER ------------------")    
    
if __name__ == "__main__":
    main()

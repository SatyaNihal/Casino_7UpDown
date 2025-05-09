import random

def welcome_screen():
    print("\nWELCOME TO SATYA'S CASINO - 7 UP OR DOWN\n")

def display_dice(dice1, dice2):
    total = dice1 + dice2
    print(f"Dice 1 = {dice1}, Dice 2 = {dice2}")
    print(f"Dice total: {total}")
    
    if total > 7:
        print("Result: UP (over 7)")
    elif total < 7:
        print("Result: DOWN (under 7)")
    else:
        print("Result: SEVEN (exactly 7)")

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    return dice1, dice2, total

def front_desk():
    welcome_screen()
    print("I am Ella (front desk), welcome to Satya's Casino!")
    
    while True:
        try:
            deposit = input("How much cash would you like to deposit? $")
            if deposit.lower() == 'q':
                return 0
            
            deposit = float(deposit)
            if deposit <= 0:
                print("Please enter a positive amount.")
                continue
            
            print(f"Awesome, your transaction of ${deposit:.2f} has been approved - here are your poker chips!")
            return deposit
        except ValueError:
            print("Please enter a valid number.")

def game_table(balance):
    print("\nBob (Dealer): Welcome to the 7 Up or Down table!")
    print("The rules are:")
    print("  - If you bet 'up' and the dice total > 7, you win")
    print("  - If you bet 'down' and the dice total < 7, you win")
    print("  - If you bet '7' and the dice total = 7, you win big (3x your bet)")
    print("  - Type 'q' at any time to cash out and exit")
    
    while balance > 0:
        print(f"\nYour current balance: ${balance:.2f}")
        
        while True:
            bet_amount = input("Bob: How much would you like to bet? $")
            if bet_amount.lower() == 'q':
                return balance
            
            try:
                bet_amount = float(bet_amount)
                if bet_amount <= 0:
                    print("Please enter a positive amount.")
                    continue
                if bet_amount > balance:
                    print("Insufficient funds. Please enter a smaller amount.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        
        while True:
            bet_type = input("Bob: Would you like to bet 'up', 'down', or '7'? ").lower()
            if bet_type == 'q':
                return balance
            
            if bet_type in ['up', 'down', '7']:
                break
            else:
                print("Please enter 'up', 'down', or '7'.")
        
        balance -= bet_amount
        print(f"\nBet placed: ${bet_amount:.2f} on {bet_type.upper()}")
        
        print("Bob: Rolling the dice...")
        dice1, dice2, total = roll_dice()
        display_dice(dice1, dice2)
        
        won = False
        payout_multiplier = 2
        
        if bet_type == 'up' and total > 7:
            won = True
        elif bet_type == 'down' and total < 7:
            won = True
        elif bet_type == '7' and total == 7:
            won = True
            payout_multiplier = 3
        
        if won:
            winnings = bet_amount * payout_multiplier
            balance += winnings
            print(f"Bob: Congratulations! You won ${winnings:.2f}!")
        else:
            print("Bob: Sorry, better luck next time!")
    
    print("\nBob: Looks like you're out of chips!")
    return balance

def main():
    balance = front_desk()
    
    if balance > 0:
        final_balance = game_table(balance)
        
        print("\nBob: Thanks for playing at our table!")
        print(f"Ella: Thanks for coming to Satya's Casino! Your final balance is ${final_balance:.2f}.")
        print("We hope to see you again soon!")
    else:
        print("Ella: Maybe next time. Have a great day!")

if __name__ == "__main__":
    main()


import random

emojis = ["😋", "🤑", "✨", "💸", "🍔", "🍕", "💰", "🧾"]
print("\n🌟 Welcome to the Emoji Tip Calculator! 🌟")

try:  

    bill_str = input("What is the total bill amount? ")
    bill = float(bill_str)  
   
    if bill < 0:
        print("Your bill cannot be a negative number.🚫")
    else:  
             
        tip_str = input("What percentage would you like to tip? (e.g., 15) ")
        tip_percentage = int(tip_str)        
        
        if tip_percentage < 0:
            print("Tip percentage cannot be a negative number.🚫")
        else:            
            tip_amount = bill * (tip_percentage / 100)
            total_bill = bill + tip_amount            
            random_emoji = random.choice(emojis)
            
            print(f"\n{random_emoji}The breakdown of your bill:{random_emoji}")
            print(f"💰 Bill Total: ${bill:.2f}")
            print(f"✨ Tip ({tip_percentage}%): ${tip_amount:.2f}")
            print(f"💸 Final Total: ${total_bill:.2f}")
            print("\nTip Calculator! May the Force be with you. 😉")

except ValueError:    
    print("That doesn't seem to be a valid number. The mission has failed. ❌")
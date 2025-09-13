# 🎰 Cantina Hyperreels — Star Wars themes

import random, time

# This is the list of universal symbols for all spins.
BASE = ["🛸", "⭐", "🗡️", "🪐", "👽", "💎"] 

# This dictionary holds the symbols specific to each theme.
THEMES = {
    "jedi":    ["✨", "🧘", "🔷"], 
    "sith":    ["🔥", "⚡", "🔴"], 
    "rebel":   ["🚀", "🎖️", "🌟"], 
    "empire":  ["🛰️", "🛡️", "⚙️"], 
    "mando":   ["🥷", "🪙", "🛡️"], 
    "droid":   ["🤖", "🔩", "🔧"], 
    "cantina": ["🍸", "🎶", "🎲"], 
}

def spin(reels=3, cycles=14, speed=0.06, *bonus, **opts):
    """
    Simulates a single spin of the Cantina Hyperreels.
    
    Args:
        reels (int): The number of reels to spin.
        cycles (int): The number of animation cycles.
        speed (float): The speed of the animation.
        *bonus (tuple): A variable number of extra symbols to add.
        **opts (dict): Optional keyword arguments for 
                       special features like theme or rigging.
    """
    theme_symbols = THEMES.get(opts.get("theme"), [])
    symbols = BASE + list(bonus) + theme_symbols
    
    for _ in range(cycles):
        roll = [random.choice(symbols) for _ in range(reels)]
        print("\r" + " | ".join(roll), end="", flush=True); time.sleep(speed)
    print()

    # This is the corrected rigging logic. It selects a symbol
    # from the theme's list if a theme is specified, otherwise from the full list.
    if opts.get("rig") == "jackpot":
        if theme_symbols:
            jackpot_symbol = random.choice(theme_symbols)
        else:
            jackpot_symbol = random.choice(symbols)
        roll = [jackpot_symbol] * reels 
        print("🔧 Rigged:", " | ".join(roll))
    
    # This line assigns a rarity value to each symbol.
    rarity = {s:i+1 for i,s in enumerate(dict.fromkeys(symbols))}
    
    # This line checks for a Kyber crystal bonus.
    kyber_bonus = (lambda r: 2 if {"💎","🔷","🔴"} & set(r) else 1)(roll)
    
    # This is the core payout logic.
    payout = (100 if len(set(roll)) == 1 else 25 if len(set(roll)) == 2 
              else sum(rarity[s] for s in roll)) * kyber_bonus
              
    return roll, payout


# This block runs automatically when the script is executed.
if __name__ == "__main__":

    print("--- Test Case 1: Standard Spins ---")
    for t in ("jedi", "sith", "rebel"):
        print(f"\n🌌 Cantina Hyperreels — theme: {t}")
        r, c = spin(3, 16, 0.05, "🧿", theme=t) 
        print("➡️", " ".join(r), "→", c, "credits")


################ --- TEST SUITE --- #################
    
    # # Test Case 1: Standard Spins
    # # This shows the default behavior for a few themes.
    # print("--- Test Case 1: Standard Spins ---")
    # for t in ("jedi", "sith", "rebel"):
    #     print(f"\n🌌 Cantina Hyperreels — theme: {t}")
    #     r, c = spin(3, 16, 0.05, "🧿", theme=t) 
    #     print("➡️", " ".join(r), "→", c, "credits")

    # # Test Case 2: Jackpot Payout with Rigging
    # # We use the 'rig' option to force a jackpot for a predictable test.
    # print("\n\n--- Test Case 2: Forced Jackpot ---")
    # roll, credits = spin(reels=3, cycles=10, rig="jackpot", theme="jedi")
    # print(f"Final roll: {roll}")
    # print(f"Payout: {credits} credits")

    # # Test Case 3: Kyber Bonus Multiplier with Rigging
    # # The 'sith' theme includes a red Kyber crystal, 
    # # which should double the payout.
    # print("\n\n--- Test Case 3: Kyber Bonus ---")
    # roll, credits = spin(reels=3, cycles=10, rig="jackpot", theme="sith")
    # print(f"Final roll: {roll}")
    # print(f"Payout: {credits} credits")
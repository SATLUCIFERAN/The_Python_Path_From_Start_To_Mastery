
# --- Data (tiny & readable) ---

bounties = [
    {"name":"Boba Fett",    "faction":"Bounty", 
     "planet":"Tatooine",  "threat":5, "reward":12000},
    {"name":"Cad Bane",     "faction":"Bounty", 
     "planet":"Nal Hutta", "threat":4, "reward": 9000},
    {"name":"Darth Maul",   "faction":"SITH",   
     "planet":"Mandalore", "threat":5, "reward":20000},
    {"name":"Hondo Ohnaka", "faction":"Pirate", 
     "planet":"Florrum",   "threat":3, "reward": 4000},
    {"name":"DJ",           "faction":"Smuggler",
     "planet":"Canto",    "threat":2, "reward": 1500},
]

# 1) List comprehension (+ conditional expression): make poster lines
posters = [
    f"{'🚨 DANGER' if b['threat']>=4 else '🟡 Wanted'} — "
    f"{b['name']} on {b['planet']} ({'⭐'*b['threat']})"
    for b in bounties
]

# 2) Set comprehension: unique planets
planets = {b["planet"] for b in bounties}

# 3) Dict comprehension (+ conditional expression): adjusted rewards
#    SITH ×1.8, others ×1.2 (rounded)

adjusted = {
    b["name"]: int(b["reward"] * (1.8 if b["faction"]=="SITH" else 1.2))
    for b in bounties
}


# 4) Tiny nested list comp: flatten words from all posters (for a “word cloud”)
words = [w for line in posters for w in line.split()]

# --- Display Board ---

print("🪧 Posters:")
for line in posters: print(" •", line)

print("\n🪐 Planets:", planets)
print("💰 Adjusted rewards:", adjusted)
print("☁️  Word cloud sample:", words[:12], "…")

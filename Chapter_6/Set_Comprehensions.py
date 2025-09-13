
codes = ["RED-1", "RED-2", "GOLD-1", "RED-2"]

# Get a set of all unique squadron colors from the codes

squadrons = {c.split("-")[0] for c in codes}
print(f"Unique squadrons: {squadrons}")
# Output: Unique squadrons: {'RED', 'GOLD'}


for c in codes:
    print(c.split("-"))

'''    
['RED', '1']
['RED', '2']
['GOLD', '1']
['RED', '2']

'''
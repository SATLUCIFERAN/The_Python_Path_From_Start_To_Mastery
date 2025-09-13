
# Jedi master
jedi = ["Yoda", "Obi-Wan", "Ahsoka"]
name_len = {name: len(name) for name in jedi}
print(f"Jedi name lengths: {name_len}")
# Output: Jedi name lengths: {'Yoda': 4, 'Obi-Wan': 6, 'Ahsoka': 6}





# reverse a mapping to find a name from a score
rank = {"Yoda": 10, "Obi-Wan": 9, "Ahsoka": 8}
reverse = {score: name for name, score in rank.items()}
print(f"Scores to names: {reverse}")


# Output: Scores to names: {10: 'Yoda', 9: 'Obi-Wan', 8: 'Ahsoka'}
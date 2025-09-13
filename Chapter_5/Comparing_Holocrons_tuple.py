
# Compare two tuples to see if they hold the same secrets
secrets_a = ("rebel base", "hiding spot")
secrets_b = ("rebel base", "hiding spot")
secrets_c = ("death star", "plans")

print(f"Are secrets A and B identical? {secrets_a == secrets_b}")
# Output: Are secrets A and B identical? True
print(f"Are secrets A and C different? {secrets_a != secrets_c}")
# Output: Are secrets A and C different? True
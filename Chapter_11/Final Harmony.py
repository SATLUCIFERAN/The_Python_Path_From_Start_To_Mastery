
import unicodedata

# A character with two different representations
s1 = "Jedi R\u00e9sum\u00e9" # 'e' with an accent as a single character
s2 = "Jedi Re\u0301sume\u0301" # 'e' followed by a combining accent mark

print(f"Strings are equal without normalization: {s1 == s2}")

# NFD (Normalization Form D) separates characters from accents
s1_normalized = unicodedata.normalize('NFD', s1)
s2_normalized = unicodedata.normalize('NFD', s2)

print(f"Strings are equal with normalization:{s1_normalized == s2_normalized}")

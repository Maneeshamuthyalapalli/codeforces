word = input()
uppercase_count = sum(1 for char in word if char.isupper())
lowercase_count = len(word) - uppercase_count
if uppercase_count > lowercase_count:
    corrected_word = word.upper()
else:
    corrected_word = word.lower()
print(corrected_word)

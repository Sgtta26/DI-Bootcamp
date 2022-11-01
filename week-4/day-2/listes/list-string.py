a_string = 'This is some string here'

# Separate all characters into a list
list(a_string)

# Separate words
separated_string = a_string.split(' ')
print(separated_string)

separated_string.append('again!')

print(separated_string)

separated_string
# Convert list into a String
modified_string = " ".join(separated_string)
print(modified_string)

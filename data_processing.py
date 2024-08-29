str1_in = input("Enter a sentence: ")
str1_in_up = str1_in.upper()
print(str1_in_up)

str2_in = input("Enter a para: ")
str2_in_co = str2_in.split()
print(str2_in_co) 
str2_co = len(str2_in_co)
print(str2_co)

# Prompt the user to enter a string
user_input = input("Please enter a string: ")

# Check if all characters in the string are digits
is_all_digits = user_input.isdigit()

# Output the result
print(f"All characters are digits: {is_all_digits}")


str4_in = input("Enter a sentence: ")
str4_in_re = str4_in.replace('a','o')
print(str4_in_re)

str5_in = input("Enter a sentence: ")
str5_in_le = len(str5_in)
print(str5_in_le)

# Prompt the user to enter their full name
full_name = input("Please enter your full name: ")

# Split the full name into individual names
name_parts = full_name.split()

# Extract the first letter of each name part and convert it to uppercase
initials = ''.join([name[0].upper() for name in name_parts])

# Print the initials
print(f"Your initials are: {initials}")

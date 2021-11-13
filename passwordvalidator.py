password = input('Password: ')

capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 
'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

# Check everything
has_eight = number_in_password = capital_in_password = lower_in_password = special_in_password = False
for c in password:
    if c in capital_letters: # Capital letters
        capital_in_password = True
    if c in lower_letters: # Lower letters
        lower_in_password = True
    if c in numbers: # Numbers
        number_in_password = True
    if c not in numbers and c not in lower_letters and c not in capital_letters:
        special_in_password = True
if len(password) >= 8:
    has_eight = True

if number_in_password:
    print('\033[0;32m', end='')
else:
    print('\033[0;31m', end='')
print('- Has at least 1 number')

if lower_in_password:
    print('\033[0;32m', end='')
else:
    print('\033[0;31', end='')
print('- Has at least 1 lower letter')

if capital_in_password:
    print('\033[0;32m', end='')
else:
    print('\033[0;31m', end='')
print('- Has at least 1 capital letter')

if special_in_password:
    print('\033[0;32m', end='')
else:
    print('\033[0;31m', end='')
print('- Has at least 1 special character')

if has_eight:
    print('\033[0;32m', end='')
else:
    print('\033[0;31m', end='')
print('- Has at least eight characters')

print('\033[0m')

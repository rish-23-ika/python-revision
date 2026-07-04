#8. Password Strength Checker
#Problem:
#Check if a password is "Weak", "Medium", or "Strong".

#Criteria:
#- Less than 6 characters      → Weak
#- 6 to 10 characters          → Medium
#- More than 10 characters     → Strong

password = input("Enter your password: ")

if len(password) < 6:
    strength = "Weak"
elif 6 <= len(password) <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print(f"Password strength is: {strength}")
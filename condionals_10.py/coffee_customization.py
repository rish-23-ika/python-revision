#7. Coffee Customization

#Problem:
#Customize a coffee order:
#- Choose a size: "Small", "Medium", or "Large"
#- Optionally add an "Extra shot" of espresso

size = input("Choose size (Small/Medium/Large): ").strip().lower()
extra_shot = input("Do you want an extra shot? (yes/no): ").strip().lower()

if extra_shot == "yes":
    print("You have ordered a", size, "coffee with an extra shot.")
else:
    print("You have ordered a", size, "coffee.")
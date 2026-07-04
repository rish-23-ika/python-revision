#10. Pet Food Recommendation

#Problem:
#Recommend a type of pet food based on the pet's species and age.

#Examples:
#- Dog:
#  - Age < 2 years  → Puppy food
#  - Age ≥ 2 years  → Adult dog food

#- Cat:
#  - Age > 5 years  → Senior cat food
#  - Age ≤ 5 years  → Regular cat food

species = input("Enter the pet's species (dog/cat): ").strip().lower()
if species == "dog":
    age = int(input("Enter the dog's age in years: "))
    if age < 2:
        print("Recommended food: Puppy food")
    else:
        print("Recommended food: Adult dog food")
elif species == "cat":
    age = int(input("Enter the cat's age in years: "))
    if age > 5:
        print("Recommended food: Senior cat food")
    else:
        print("Recommended food: Regular cat food")
else:
    print("Unknown species. Please enter 'dog' or 'cat'.")
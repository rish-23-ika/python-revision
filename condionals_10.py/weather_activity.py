#5. Weather Activity Suggestion
#Problem:
#suggest an activity based on the weather.

#Examples:
#- Sunny → Go for a walk
#- Rainy → Read a book
#- Snowy → Build a snowman

weather = input("Enter the weather (sunny, rainy, snowy): ").strip().lower()
if weather == "sunny":
    print("Go for a walk.")
elif weather == "rainy":
    print("Read a book.")
elif weather == "snowy":
    print("Build a snowman.")
else:
    print("Unknown weather condition.")
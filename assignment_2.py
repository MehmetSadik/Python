age = input("Are you a cigarette addict older than 75 years old? ").title().strip() == "Yes"
chronic = input("Do you have a severe chronic disease? ").title().strip() == "Yes"
immune = input("Is your immune system too weak? ").title().strip() == "Yes"

if age or chronic or immune == True:
    print("You are in risky group")
else:
    print("You are not in risky group")

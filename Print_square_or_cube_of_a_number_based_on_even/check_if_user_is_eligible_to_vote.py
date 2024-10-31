def check_voting_eligibility(age):
    return age >= 18


age = int(input("Enter your age: "))
print(check_voting_eligibility(age))
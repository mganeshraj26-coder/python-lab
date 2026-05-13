name = input ("enter a name")
birth_year = int (input("enter year of birth:"))

current_year = 2026
age = current_year-birth_year

print("/n name:",name)
print("age:",age)

if age >=60:
    print("the person is a seniorcitizen")
else:
    print("the person is not a senior citizen")
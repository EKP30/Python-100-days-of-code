age = input("What is your current age?")
full_life = 90
age = int(age)
int(full_life)
yrs_to_live = full_life - age
months_to_live = yrs_to_live * 12
weeks_to_live = yrs_to_live * 52
days_to_live = yrs_to_live * 365
print(f"You have {days_to_live} days, {weeks_to_live} weeks, and {months_to_live} months left.")
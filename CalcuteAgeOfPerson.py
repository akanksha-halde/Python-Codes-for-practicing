#Calculate Age of a person

import datetime as dt
current_date=dt.date.today()
#print(type(x))
def agecalculator(birthd):
    age=(current_date.year-birthd.year)-((current_date.month,current_date.day)<(birthd.month,birthd.day))   
    return age
    
    
birth_year=int(input("Enter the birth year:"))
birth_month=int(input("Enter the birth month:"))
birth_day=int(input("Enter the birth day:"))
birth_date=dt.date(birth_year,birth_month,birth_day)
# print(type(bd))
print("Your age is:",agecalculator(birth_date))

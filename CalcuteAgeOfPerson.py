#Calculate Age of a person
#Datetime module is used
import datetime as dt
#date.today() tells us todays date
current_date=dt.date.today()
#print(type(x))
def agecalculator(birthd):
    #In here the comparison operation returns True/False and according to that if it id true 1 is taken and vice versa
    age=(current_date.year-birthd.year)-((current_date.month,current_date.day)<(birthd.month,birthd.day))   
    return age
    
    
birth_year=int(input("Enter the birth year:"))
birth_month=int(input("Enter the birth month:"))
birth_day=int(input("Enter the birth day:"))
birth_date=dt.date(birth_year,birth_month,birth_day)
# print(type(bd))
print("Your age is:",agecalculator(birth_date))

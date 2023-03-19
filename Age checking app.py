
current_year = 2023
average_age = 18
name_of_student = input("Enter name: --")

def age_cal():
    age_calculation = int(input("enter years of birth: "))
    if age_calculation < 2006 :
     final_age = current_year - age_calculation
     print ("hello you are", final_age, "years old")
    else:
     final_age = current_year - age_calculation
     print('Sorry you are', final_age, 'years,expected age is 18 and above')

age_cal()
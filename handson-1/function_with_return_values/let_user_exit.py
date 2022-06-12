from cgitb import text


calculation_to_units = 24 

name_of_units = "hours"

def days_to_units(num_of_days): 
   
    return f"{num_of_days} days are  { num_of_days * calculation_to_units } {name_of_units} "
      
       
def validate_and_execute():
    try:
        user_input_number = int(user_input)
        if user_input_number > 0:
 
          calculated_value = days_to_units(user_input_number)

          print(calculated_value)
        
        elif user_input_number == 0:
       
           print("you enter 0 please Enter valid postive ")      
           
        else:
            print("you enter negative number please Enter valid postive ")      

           
       
    except ValueError:
    
       print("your input is not a valid number, don't ruin my program! ")

user_input = ""
while user_input != "exit":    
       user_input = input("Hey user Enter number of days I will concert into days!\n")   

       validate_and_execute()
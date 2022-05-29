calculation_to_units = 24 *60

name_of_units = "minutes"

def days_to_units(num_of_days,custom_message):

    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}")
    
    print(custom_message)
    
    
def scope_check(num_of_days):
    my_var = "variable inside function"
   
    print(name_of_units)
    
    print(num_of_days)
    
    print(my_var)
   
scope_check(20)   
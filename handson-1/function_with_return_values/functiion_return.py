calculation_to_units = 24 

name_of_units = "hours"

def days_to_units(num_of_days): 

    return f"{num_of_days} days are  { num_of_days * calculation_to_units } {name_of_units} "
    
my_var = days_to_units(30)

print(my_var)
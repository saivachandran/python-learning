calculation_to_units = 24 *60

name_of_units = "minutes"

def days_to_units(num_of_days):

    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}")
    
    print("All good!")
    
days_to_units(40)
days_to_units(60)
"""This is the entry point of the program."""


def highest_number_cubed(limit):
    
    cubed = 0
    i = 0    
    while cubed < limit:
        i += 1
        cubed = i**3
        
    result = i - 1
    
    return result

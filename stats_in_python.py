import sys
import math

def load_data(filepath:str, column:int)->tuple[list, int]:
    # TODO - Complete the function so it loads the data from the file into a list
    # The function returns a tuple that contains the list of values and the total number 
    # of values in the column
    with open(filepath, 'r') as file:
        for line_number, line in enumerate(file, start =0):
            stripped_line = line.strip()
            if not stripped_line:
                continue
    pass

def calculate_average(numbers:list)->float:
    # TODO - Complete the function to return the average of the list of numbers
    if not isinstance(numbers,list):
        raise ValueError("input must be a list")
    valid_numbers_ = [n for n in numbers if isinstance(n,(int,float))]
    return sum(valid_numbers_/len(valid_numbers_))
    pass

def get_max_and_min(numbers:list)->tuple[float, float]:
    # TODO - Complete the function to return a tuple with the maximum and minimum
    # values in the list, in that order
    try: 
        max_value = max(numbers)
        min_value = min(numbers)
    except ValueError:
        raise ValueError("The elements listed are not comparable.")
    return max_value, min_value
    pass

def calculate_variance(numbers:list)->float:
    # TODO - Complete the function to return the variance of the numbers in the list

    pass

def calculate_std_dev(numbers:list)->float:
    # TODO - Complete the function to return the standard deviation of the numbers in the list
    std =math.sqrt
    pass


def calculate_median(number:list)->float:
    # TODO - Complete the function to return the median of the numbers in the list
    sorted_list = sorted(number)
    if len(number)%2 == 0:
        median =(sorted_list[(len(number))//2-1] + sorted_list[n//2]/2)
    else:
        median = (sorted_list[((len(number)) //2])
        
    return median
    
    pass


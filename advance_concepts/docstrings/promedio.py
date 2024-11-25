def calculate_average(numbers) -> float:
    """
    Calculate average in number list.

    Parameters:
    numbers(list): a number list integers or floats

    Return:
    float: The average to number list
    """
    return sum(numbers) / len(numbers)

# Print the result of function
print(calculate_average([1,2,3,4,5,6,7,8,9,10]))

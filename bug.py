def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage (this will cause ZeroDivisionError)
my_list = []
result = calculate_average(my_list)
print(f"The average is: {result}")

#Example usage 2 (this will run successfully)
my_list = [10,20,30,40,50]
result = calculate_average(my_list)
print(f"The average is: {result}")
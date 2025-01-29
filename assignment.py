
"""
assignment.py

This module contains utility functions including:
1. A function to format strings using f-strings.
2. A function to check conditions for numbers.
3. A function to calculate the sum of numbers using a loop.
"""

def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    return f"My name is {name} and I am {age} years old"

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    if number == 10:
        return 'Equal'
    if number > 10:
        return 'Greater'
    return 'Lesser'

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    total = 0
    for x in range(n + 1):
        total += x
    return total

def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    if not numbers:
        return (0, None, None)  # Handle the case for empty list

    # Initialize sum, max, and min with appropriate values
    total_sum = 0
    max_num = numbers[0]
    min_num = numbers[0]

    # Iterate through the list and calculate sum, max, and min
    for num in numbers:
        total_sum += num
        if num > max_num:
            max_num = max(max_num, num)
        if num < min_num:
            min_num = min(min_num, num)

    return (total_sum, max_num, min_num)

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    # Initialize an empty list to store the names of students with scores > 80
    result = []
    # Use a for loop to iterate over the dictionary
    for student, score in students_dict.items():
        if score > 80:
            result.append(student)
    return result

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    return set(list1) & set(list2) # common elements

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    return{
        "sum": a+b,
        "difference": a-b,
        "product": a*b,
        "quotient": a/b
    }

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    return {
        "and": x and y,   # Logical AND
        "or": x or y,     # Logical OR
        "not_x": not x    # Logical NOT
    }

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    return {
        "and": a & b,   # Bitwise AND
        "or": a | b,    # Bitwise OR
        "xor": a ^ b    # Bitwise XOR
    }

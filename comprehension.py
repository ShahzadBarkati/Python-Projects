# **List comprehensions**: a concise and efficient way to create lists in python. Generate lists in a single line of code, 
# making your code more readable and Pythonic.

# Basic Syntax 

# [expression for item in iterable]

# expression → The operation to perform on each item
# item → The variable representing each element in the iterable
# iterable → The data structure being iterated over (list, range, etc.)


# 1. Square of 1 - 5 numbers
print(f"\nSquare of 1 - 5 numbers are: {[x**2 for x in range(1,6)]}")
print("____________________________")

# 2. Using if Condition in List Comprehension

l2 = [x for x in range(1,11) if x%2==0]
print(f"\nFilter even numbers from 1 - 10 are: {l2}")
print("____________________________")

# 3. Using if-else Condition in List Comprehension

l3 = [{x:'Even'} if x%2==0 else {x:'Odd'} for x in range(1,6)]
print(f"\nMarking 'Even'/'Odd' numbers from 1 - 5 are: {l3}")
print("____________________________")

# 4. Nested Loops in List Comprehension

pairs = [(x, y) for x in range(2) for y in range(3)]
print(f"\nPair of two list are: {pairs}")
print("____________________________")

# 5. List Comprehension with Functions

words = ["hello", "world", "python"]
print(f"\nConverting a word to upper case from a list are: {[x.upper() for x in words]}")
print("____________________________")

# 6. Nested List Comprehension

matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print(f"\nFlattening a 2D list: {flattened}")
print("____________________________")

##### ------------------------------------------------------------------------ #####

# 7. Set Comprehensions

unique_numbers = {x for x in [1, 2, 2, 3, 4, 4, 5]}
print(f"\nSet: Unique numbers: {unique_numbers}")
print("____________________________")

# 8. Dictionary Comprehension

squared_dict = {x: x**2 for x in range(5)}
print(f"\nDictionary: Number 0 - 4 with thier Square: {squared_dict}")
print("____________________________")
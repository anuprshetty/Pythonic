# Lambda function is meant to be short function which doesn't have a name (anonymous function) and is only used to return a value. They are almost never used to perform actions.

# Normal function
def double_it(x):
    return x * 2

print(double_it(3))


# Lambda function
# Syntax: lambda <para_1>, <para_2>: <return_expression>

# Assigning lambda definition to a variable.
double_lambda = lambda x: x * 2
print(double_lambda(5))

# Calling a lambda function
result = (lambda x: x * 2)(10)
print(result)

# Lambda function usage
numbers = [4, 6, 3, 9, 5]

# Calling normal function
doubles = [double_it(x) for x in numbers]
print(doubles)

# Calling lambda function
doubles = [(lambda x: x * 2)(x) for x in numbers]
print(doubles)

# Lambda function with if-else
# Syntax: lambda <para_1>, <para_2>: <if_return_expression> if(condition) else <else_return_expression>
square = lambda x : x*x if(x > 0) else None
print(square(4))

# NOTE: Since a lambda function must have a return value for every valid input, we cannot define it with if but without else as we are not specifying what will we return if the if-condition will be false i.e. its else part.


# map() Function:
# map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

# The resultant list in list(map()) always points to newly created memory location even though it has same values of the source list. 
# The resultant list never points to source list memory location.

# Calling normal function using map() function
map_object = map(double_it, numbers)
print(map_object) # <map object at 0x0000016AB80F7FA0>
print(list(map_object)) # [8, 12, 6, 18, 10]

# Calling lambda function using map() function
print(list(map(lambda x: x * 2, numbers))) # [8, 12, 6, 18, 10]


# Generator functions:
# - A function or method which uses the yield statement is called a generator function.
# - Such a function, when called, always returns an iterator object which can be used to execute the body of the function: calling the iterator’s iterator.__next__() method will cause the function to execute until it provides a value using the yield statement.
# - When the function executes a return statement or falls off the end, a StopIteration exception is raised and the iterator will have reached the end of the set of values to be returned.

# yield keyword:
# - Yield is a keyword in Python that is used to return from a function without destroying the states of its local variable and when the function is called, the execution starts from the last yield statement.
# - Any function that contains a yield keyword is termed a generator.

# List holds entire results in the memory.
# But Generator object don't hold entire results in the memory. It yields one result at a time. i.e., Later when we ask for a result, it will compute and give it to us.
# Advantages of Generators:
# - Generators are better with performance. It's not holding all the values in memory. Also it speeds up the computation time to some extent compared to list.


def get_square_numbers(nums):
	squares = []
	for num in nums:
		squares.append(num * num)

	return squares


def yield_square_numbers(nums):
	for num in nums:
		yield num * num

	return -1  # We can return a value when the StopIteration exception is thrown.


numbers = [1, 2, 3, 4, 5]

print('Via List')
square_numbers = get_square_numbers(numbers)
# square_numbers = [number * number for number in numbers]  # List comprehension - creates and assigns a new list.
print(square_numbers)  # [1, 4, 9, 16, 25]

print()
print('Via Generator')
print('With next() function')
square_numbers = yield_square_numbers(numbers)
# square_numbers = (number * number for number in numbers)  # Generator comprehension - creates and assigns a new generator.
print(square_numbers)  # <generator object yield_square_numbers at 0x7f60927628e0>

for _ in range(len(numbers)):
	print(f'next: {next(square_numbers)}')

try:
	print(f'next: {next(square_numbers)}')
except StopIteration as e:
	print(f'return: {e.value}')

# print(f'error: {next(square_numbers)}')  # StopIteration exception
print(f'default: {next(square_numbers, 0)}')  # default: 0

print('Without next() function')
# square_numbers = yield_square_numbers(numbers)
square_numbers = (number * number for number in numbers)  # Generator comprehension - creates and assigns a new generator.
print(square_numbers)  # <generator object <genexpr> at 0x7f60927628e0>

for square in square_numbers:
	print(f'value: {square}')

print('Generator to List conversion:')
# NOTE:
# Generators can't be rewound.
# But you have the following options:
# 1. Run the generator function again, restarting the generation.
# 2. Store the generator results in a data structure on memory or disk which you can iterate over again.
# - The downside of option 1 is that it computes the values again. If that's CPU-intensive you end up calculating twice.
# - On the other hand, the downside of 2 is the storage. The entire list of values will be stored on memory. If there are too many values, that can be unpractical.
# --> So you have the classic memory vs. processing tradeoff.
# --> So ways of rewinding the generator are either storing the values or calculating them again.
print(list(square_numbers))  # []
square_numbers = (number * number for number in numbers)
print(list(square_numbers))  # [1, 4, 9, 16, 25]

print()
# 'yield from' statement:
# - shorthand notation for using a generator inside a generator.
# - Also it's used for implementing coroutines in Python.

print("yield from:")


def gen1():
	yield 1
	yield 2
	yield 3


def gen2():
	yield 100
	yield from gen1()
	yield 200

# above gen2() is same as below gen2()


# def gen2():
# 	yield 100
# 	for num in gen1():
# 		yield num
# 	yield 200


for num in gen2():
	print(num)  # 100, 1, 2, 3, 200

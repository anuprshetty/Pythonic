# Iterable:
# - Something that can be looped over. Ex: List
# - If something is iterable, then it needs to have a special method called __iter__().
# - So a for loop will call the __iter__() method on an object and return an iterator that it can loop over.

# Iterator:
# - Iterator is an object with a state so that it remembers where it is during iteration.
# - And iterator also know how to get the next value. They get their next value with a __next__() method.
# NOTE:
# - The iterator can only go forward.
# - So there is no going backwards, resetting it or making a copy of it.
# - You can only go forward by calling next().
# - If you need to start from scratch, then you can simply create a new iterator object from scratch and just start that over.

print("Iterable")
nums = [1, 2, 3]
print(nums)
print(dir(nums))

print("Iterator")
nums_iter = iter(nums)  # Same as --> nums_iter = nums.__iter__()
print(nums_iter)  # <list_iterator object at 0x7f6900c2ee10>
# Iterator will have 2 main functions.
# 1. __iter__(): Iterator is also an iterable. So it will have __iter__() method. It basically returns self. i.e., Iterator object itself.
# 2. __next__():
print(dir(nums_iter))

print("Iterator Next Values")
print(next(nums_iter))  # Same as --> nums_iter.__next__()
print(next(nums_iter))
print(next(nums_iter))
# print(next(nums_iter))  # StopIteration exception

print("Internal working of for loop with iterator:")
nums_iter = iter(nums)
while True:
	try:
		item = next(nums_iter)
		print(item)
	except StopIteration:
		break

# The above code is equivalent of below for loop:
# for item in nums:
# 	print(item)

print("Iterator in action: (Practical Example by mimicking built-in range() method.)")


class MyRange:

	def __init__(self, start, end):
		self.value = start
		self.end = end

	def __iter__(self):
		return self

	def __next__(self):
		if self.value >= self.end:
			raise StopIteration

		current_value = self.value
		self.value += 1
		return current_value


nums = MyRange(0, 5)

for num in nums:
	print(num)

print("Generators are also Iterators:")
# Generators:
# - Generators are Iterators as well.
# - __iter__() and __next__() methods are created automatically.


def yield_range(start, end):
	while start < end:
		current_value = start
		start += 1
		yield current_value


nums = yield_range(0, 5)

for num in nums:
	print(num)

# print(next(nums))  # StopIteration exception is automatically thrown by generator object. It is handled by generator.__next__() method.

# NOTE: Iterator don't actually need to end. It can simply go on forever. So as long as there is a next value, then the iterator will keep getting each next value one at a time.


def yield_range(start):
	while True:
		current_value = start
		yield current_value
		start += 1


nums = yield_range(0)

# for num in nums:  # Infinite loop
# 	print(num)

# Difference between Iterator vs Generator:

# Iterator:
# 1. Class is used to implement an iterator
# 2. Local Variables aren’t used here.
# 3. Iterators are used mostly to iterate or convert other objects to an iterator using iter() function.
# 4. Iterator uses iter() and next() functions
# 5. Every iterator is not a generator

# Generator:
# 1. Function is used to implement a generator.
# 2. All the local variables before the yield function are stored.
# 3. Generators are mostly used in loops to generate an iterator by returning all the values in the loop without affecting the iteration of the loop
# 4. Generator uses yield keyword
# 5. Every generator is an iterator

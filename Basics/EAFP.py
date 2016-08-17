# EAFP --> Easier to Ask Forgiveness than Permission. (Pythonic Way)
# - Try to do something. If it works, then great. If not, then just handle that error.

# EAFP use cases:
# - It's slightly faster in situations where we don't expect a lot of exceptions.
# - It is more readable.
# - It avoids race conditions in certain situations.

nums = [1, 2, 3, 4, 5]

# Non-Pythonic:
index = 6
if index < len(nums):
	print(f"{index} - {nums[index]}")
else:
	print(f"Index {index} does not exists")

# Pythonic:
try:
	print(f"{index} - {nums[index]}")
except IndexError:
	print(f"Index {index} does not exists")

# EAFP avoids race conditions in certain situations:

import os

file_path = './tmp/test.txt'

# Race Condition:
# Problem here is
if os.access(file_path, os.R_OK): # when this check passes, that means file is accessible,
	with open(file_path) as fd: # then by the time we get to this line, in this short period of time, the file might not be accessible due to some reason like access permissions changed by other programs, etc. In that case, this line will throw an error saying file is not accessible. So there is a chance of race condition.
		print(fd.read())
else:
	print(f"{file_path} file can not be accessed")

# No Race Condition:
try:
	f = open(file_path)
except IOError:
	print(f"{file_path} file can not be accessed")
else:
	with f:
		print(fd.read())

# Type Hinting don't stop you from running the code and don't raise any errors.
# It's just there to help you as a developer.

from typing import List # List, Tuple, Set etc.


def list_avg(sequence: List[int]) -> float:
    return sum(sequence) / len(sequence)

print(list_avg([1, 3, 4]))


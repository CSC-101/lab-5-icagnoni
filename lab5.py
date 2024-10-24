import data
from typing import Optional
import math
# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
def time_add(time1: data.Time, time2: data.Time) -> data.Time:
    new_second = time1.second + time2.second
    new_minute = time1.minute + time2.minute + (new_second // 60)
    new_second = new_second % 60
    new_hour = time1.hour + time2.hour + (new_minute // 60)
    new_minute = new_minute % 60
    new_hour = new_hour % 24

    return data.Time(new_hour, new_minute, new_second)

# Part 4
def is_descending(lst: list[float]) -> bool:
    return all(lst[n] > lst[n+1] for n in range(len(lst) - 1))

# Part 5
def largest_between(lst: list[int], lower: int, upper: int) -> Optional[int]:
    if lower > upper:
        return None
    if lower < 0:
        lower = 0
    if upper >= len(lst):
        upper = len(lst) - 1
    if lower > upper:
        return None
    largest_index = lower
    for n in range(lower, upper + 1):
        if lst[n] > lst[largest_index]:
            largest_index = n

    return largest_index

# Part 6
def furthest_from_origin(points: list[data.Point]) -> Optional[int]:
    if not points:
        return None
    furthest_index = 0
    max_distance = math.sqrt(points[0].x ** 2 + points[0].y ** 2)
    for n in range(1, len(points)):
        distance = math.sqrt(points[n].x ** 2 + points[n].y ** 2)
        if distance > max_distance:
            furthest_index = n
            max_distance = distance

    return furthest_index

"""
Помилки (номери рядків через пробіл, цей рядок - №2): !!!
"""


def non_negatives(nums):
    """Удалить из списка чисел 'nums' отрицательные элементы и вернуть
    измененный список."""
    result = nums.copy()
    for number in nums:
        if number < 0:
            result.remove(number)
    return result

import random

n = 10
nums = [round(random.uniform(-10, 10), 2) for i in range(n)]
print(nums)

non_negatives(nums)
print(nums)

"""
Помилки (номери рядків через пробіл, цей рядок - №2): !!!
"""


def non_negatives(nums):
    """Удалить из списка чисел 'nums' отрицательные элементы и вернуть
    измененный список."""
    for i in range(len(nums)):
        if nums[i] < 0:
            del nums[i]

    return nums

# import random
#
# n = 10
# nums = [round(random.uniform(-10, 10), 2) for i in range(n)]
# print(nums)
#
# non_negatives(nums)
# print(nums)

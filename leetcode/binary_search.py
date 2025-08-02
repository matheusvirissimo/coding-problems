"""Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""


def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1 # não estoura o limtie

        while left <= right:

            middle_value = nums[right//2]

            if middle_value == target:
                return target
            elif target < middle_value:
                right = middle_value
            else:
                left = middle_value 

        return -1


nums = [-1,0,3,5,9,12]
target = 9

left = 0
right = len(nums) - 1 # não estoura o limtie

middle_value = nums[right//2]

if middle_value == target:
    print(middle_value)
elif target < middle_value:
    right = middle_value
else:
    left = middle_value

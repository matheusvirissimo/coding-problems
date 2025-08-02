"""
Escreva um algoritmo com complexidade O(log n) que procure um elemento numa lista e retorne a posição dele
Caso ele não exista, informe a posição dele na lista ordenada
"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return binary_search(nums,target)
    
def binary_search(nums, target): 
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (right + left)//2
        mid_val = nums[mid]

        if target == mid_val:
            return mid
        elif target > mid_val:
            left = mid + 1
        else:
            right = mid - 1

    return left

## ESTUDOS E TESTE
# O(log n) -> busca binária

def binary_search(nums, target): 
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (right + left)//2
        mid_val = nums[mid]

        if target == mid_val:
            return mid
        elif target > mid_val:
            left = mid + 1
        else:
            right = mid - 1

    return left

    ## o valor não está no array, então devemos saber onde inserir
    # if target > nums[len(nums) - 1]:
    #     return left
    # else:
    #     if right < 0:
    #         right = 0 
    #         return right

    

## ESTUDOS E TESTES 

def remove_element(nums, val):

    # algoritmo é in-place, então não posso criar uma variável auxiliar

    count = 0

    for i in range(len(nums)):
        if nums[i] != val:
            # fazer um swap
            nums[count] = nums[i]
            count += 1

    return count


nums=[3,2,2,3]
val=3


print(remove_element(nums, val))
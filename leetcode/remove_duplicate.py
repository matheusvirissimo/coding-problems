def removeDuplicate(nums: list):
    k = 1 # segundo iterador

    # O(n) 
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]: # não tem duplicatada
            nums[k] = nums[i]
            k += 1
        

    return k, nums


nums = [0,0,1,1,1,2,2,3,3,4]


print(removeDuplicate(nums))


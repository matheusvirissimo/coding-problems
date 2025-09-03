def findClosestNumber(nums):

    # primeiro valor sempre é o mais próximo 
    close_to_zero = nums[0]
    
    for i in nums:
        if abs(i) < abs(close_to_zero): 
            close_to_zero = i

    # caso tenham dois valores iguais em lados opostos, retornamos o positivo
    if close_to_zero < 0 and abs(close_to_zero) in nums:
        close_to_zero = abs(close_to_zero)

    return close_to_zero 

nums = [2,-1,1]

print(findClosestNumber(nums))
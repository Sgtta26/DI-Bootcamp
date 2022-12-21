def subset_first_solution(nums , target):
    for n in nums: # n action
        for second_n in nums:
            if second_n+n==target:
                return True
    return False


def bruteforce_subsetsum(nums , target):
    #search for two compatible numbers
    for n in nums: # n action
        if (target - n) in nums:   # n action
           return True  # n*n = n^2 

    return False
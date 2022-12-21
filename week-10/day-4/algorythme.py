def binarySearch(arr,target): 
    while len(arr) > 0:
        middle = len(arr)//2

        if arr[middle] == target:
            return True

        elif arr[middle] > target:
            arr = arr[0 : middle ] 

        elif arr[middle] < target:
            arr = arr[middle+1 : len(arr)]
    
    return False


arr = [1,2,5,7,9,10,14,17,20,22,26,30,35,38]
print(binarySearch(arr , 26))







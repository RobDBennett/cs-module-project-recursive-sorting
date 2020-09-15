# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if end >= start: #Checks for sorting.
        mid = start + (end - 1) // 2 #Finds middle.
        if arr[mid] == target:
            return mid #If the middles is the target.
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid+1) #If middle is bigger than target, disregard everything to the right of the middle
        else:
            return binary_search(arr, target, mid+1, end) #If middle is smaller than target, disregard to left of the middle.
    else:
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    if arr[0] < arr[1]: #determines if Ascending
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            guess = arr[mid] #The middle of the array is our baseline guess.
            if target == guess:
                return mid
            else:
                if guess > target: #If the middle is bigger than target, remove everything to the right of middle.
                    high = mid -1
                else:
                    low = mid +1 #If the middle is smaller than the target, remove everything to the left of the middle.
        return -1
    else: #For Descending, perform the same tests but largely reverse the values.
        low = len(arr) - 1
        high = 0
        while low >= high:
            mid = (low + high) // 2
            guess = arr[mid]
            if target == guess:
                return mid
            else:
                if guess < target:
                    low = mid -1
                    
                else:
                    high = mid +1
        return -1


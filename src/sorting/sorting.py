# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    
    j = 0 #Starting index for arrA
    i = 0 #Starting index for arrB
    k = 0 #Merged index
    while j < len(arrA) and i < len(arrB):
        if arrA[j] < arrB[i]: #Compares first element of two arrays
            merged_arr[k] = arrA[j] #Makes the first element of merged array from A if smaller.
            j += 1 #Raises the arrA index so will point to next element
        else:
            merged_arr[k] = arrB[i] #Makes first element of the merged array from B if smaller
            i += 1 #Raises the arrB index so will point to the next element.
        k += 1 #Outside the If, this raises the merged Index.
    while j < len(arrA): #Continues while the arrA index is less than the length of arrA (only occurs if B goes first)
        merged_arr[k] = arrA[j] #Adds next element from A to merged.
        k += 1 #Raises merged index
        j += 1 #Raises arrA index
    while i < len(arrB): #Continues while arrB index is less than the length of arrB (only occurs if A goes first)
        merged_arr[k] = arrB[i] #Adds next element from B to merged
        k += 1 #Raises merged index
        i += 1 #Raises arrB index
        
    return merged_arr

"""
Sasana's solution- Much cleaner.
def merge(arrA, arrB):
    merged_arr = []
    while (arrA and arrB):
        if (arrA[0] <= arrB[0]):
            item = arrA.pop(0)
            merged_arr.append(item)
        else:
            item = arrB.pop(0)
            merged_arr.append(item)
    merged_arr.extend(arrA if arrA else arrB)
    return merged_arr

Instructor's solution-
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a = 0
    b = 0
    for i in range(elements):
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1

    return merged_arr

"""

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) > 1: #Checks that array is more than single item.
        right = len(arr) #High
        left = 0 #Low
        middle = (right+left) // 2 #Middle.
        left_merge_arr = merge_sort(arr[:middle]) #Recursively breaks array into two parts 
        right_merge_arr = merge_sort(arr[middle:]) #Recursively breaks array into two parts.
        final_arr = merge(left_merge_arr, right_merge_arr) #Runs helper function on array broken into two parts.
        return final_arr #Returns final product.
    return arr #Returns if array is single element.

"""
Instructor solution-
def merge_sort(arr):
    if len(arr) > 1:
        left = merge_sort(arr[0 : len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        arr = merge(left, right)
    return arr

"""
# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    start2 = mid + 1 #A second mid point to compare
    if (arr[mid] <= arr[start2]): #Checks if the direct merge is already sorted
        return
    while (start <= mid and start2 <= end): #Two pointers to maintain start of both arrays to merge
        if (arr[start] <= arr[start2]): #If element 1 is in right place
            start += 1
        else:
            value = arr[start2]
            index = start2
            # Shift all the elements between element 1 to element 2 right by 1.
            while (index != start):
                arr[index] = arr[index - 1]
                index -= 1
            
            arr[start] = value
            #Update all pointers and repeat.
            start += 1
            mid += 1
            start2 +=1

    
    """
    Rob's original solution. Very cumbersome.
    # Start with two halves
    n1 = mid - start + 1
    n2 = end - mid
    # Create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[start + i]
    for j in range(0, n2):
        R[j] = arr[mid + 1 + j]
    # Merge the temp arrays back into arr[l..r]
    i = 0   #Initial index for first subarray
    j = 0   #Initial index for second subarray
    k = start  #Initial index for merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    #Copy the remaining elements of L[], if there are any.
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    #Copy the remaining elements of the R[], if there are any.
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    """

def merge_sort_in_place(arr, l, r):
    # l is the left index, r is the right index.
    if l < r:
        #Same as (l+r) //2, but avoids overflow for large l.
        m = (l+(r-1)) //2
        #Sort first and second halves.
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m+1, r)
        merge_in_place(arr, l, m, r)


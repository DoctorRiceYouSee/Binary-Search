#binary_search.py
#A program that demonstrates how binary search works
#Program only works if given a SORTED array. If array is not sorted, maybe use quicksort to sort?


def binarySearch(array, left_index, right_index, find_me):

    if right_index >= left_index:
        middle_index = left_index + (right_index-left_index)

        # If element is present at the middle
        if array[middle_index] == find_me:
            return middle_index

        # If element is smaller than the middle_index, then it
        # can only be present in left subarray
        elif array[middle_index] > find_me:
            return binarySearch(array, left_index, middle_index-1, find_me)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(array, middle_index + 1, right_index, find_me)

    else:
        return -1


if __name__=="__main__":
    array = [3,7,12,34,56,67,76,81,90,153]
    find_me = 81 #which is at index 7
    left_index = 0
    right_index = len(array)-1
    result = binarySearch(array, left_index, right_index, find_me)
    if result != -1:
        print ("Element is present at index % d" % result)
    else:
        print ("Element is not present in array") 

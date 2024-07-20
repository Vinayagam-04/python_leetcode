def remove_duplicates(nums):
    if not nums:
        return 0
    i = 0  # Pointer for the position of unique elements

    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1 

input_str = input("Enter sorted array elements: ")
nums = list(map(int, input_str.split()))
length = remove_duplicates(nums)
print("Length of array:", length)
print("Array with unique elements:", nums[:length])

""" 
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k. 
"""

def removeElement(nums, val):
        def swap(index1, index2, arr):
            temp = arr[index1]
            arr[index1] = arr[index2]
            arr[index2] = temp
        position_to_swap = -1
        count_of_val = 0
        for index, each_element in enumerate(nums):
            l = index + abs(position_to_swap)
            if l == len(nums):
                print(f"{index}, {position_to_swap} is a common point and breaking out of loop ....")
                break
            print(f" Element: {each_element} to be removed ... ",end=" ")
            curr = each_element
            if curr == val:
                print(f" YES")
                print(f"\t Finding the index to swap ...")
                while curr == nums[position_to_swap]:
                    l = index + abs(position_to_swap)
                    if l == len(nums):
                        print(f"\t{index}, {position_to_swap} is a common point and breaking out of loop ....")
                        common_point = True
                        break
                    common_point = False
                    position_to_swap = position_to_swap - 1
                    count_of_val += 1
                if not common_point:
                    print(f"\t Found index {position_to_swap} which has value {nums[position_to_swap]} , swapping . . .")
                    swap(index, position_to_swap, nums)
                    count_of_val += 1
                else:
                    break
            else:
                print("No, Going to Next Element . . .")
        val_of_k = len(nums) - count_of_val
        return val_of_k

nums = [3,3]
val = 3

print(removeElement(nums, val))
print(nums)

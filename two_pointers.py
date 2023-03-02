# Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
def twoSum(nums, target):
    for i in range(len(nums)):
        other_num = target - nums[i]
        for j in range(len(nums)):
            if nums[j] == other_num and j != i:
                return [i, j]
            
def twoSumPointers(nums, target):
    left, right = 0, len(nums)-1
    nums = sorted(nums)
    while left < right:
        total = nums[right] + nums[left]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1


# 2 Sum with Sorted Input Array
def twoSum2(numbers, target):
    # this problem assumes the array is already sorted but if not
    # numbers = sorted(numbers)
    # we want to use 2 pointers here one starting at the beginning and end of the array
    left, right = 0, len(numbers)-1
    while left < right:
        # start at the smallest and largest number and check if they equal total
        total = numbers[left] + numbers[right]
        if total == target:
            return [left+1, right+1]
        elif total < target:
            # if the current total is less than target move the left pointer right
            left += 1
        else:
            # if the current total is greater than target move the right pointer left
            right -= 1
            
    # this problem assumes there will always be one right solution
    # but if there is none, then this will execute when the two pointers cross
    # return [-1, -1]
    
def threeSum(numbers, target):
    # in this case it is optimal to sort the list first in O(nlogn)
    sorted_nums = sorted(nums)
    result = []
    
    # enumerate will provide us with an index value for each list item
    for index, value in enumerate(sorted_nums):
        # first we will identify the first number, and ignore duplicate elements
        if index > 0 and value == sorted_nums[index - 1]:
            # continue will return us to the top of the loop
            continue
        
        # once we identify the first element, we will use 2sum2 with pointers
        left, right = index + 1, len(sorted_nums)-1
        while left < right:
            total = value + sorted_nums[left] + sorted_nums[right]
            if total > target:
                right -= 1
            elif total < target:
                left += 1
            else:
                # once we find the result, append the whole array to the index
                result.append([value, sorted_nums[left], sorted_nums[right]])
                
                # this checks for cases where the next element is the same
                # for example [0, -2, -2, -1, 1, 2, 2] where duplicates might be added
                # the condition below will increment the left pointer based on dups
                left += 1
                while sorted_nums[left] == sorted_nums[left - 1] and left < right:
                    left += 1
    return result
                
def max_area_water_bucket_brute_force(height):
    # this solution exceeded the time limit in leetcode
    current_max = 0
    # the idea here is we will brute force check every line against each following one starting at index 0 and 1
    for i in range(len(height)):
        # check every line after index i to see if the height exceeds the current max height, replace if it is
        for j in range(i+1, len(height)):
            # get the area by subtracting index j from i (length) and getting the smaller bar
            product = min(height[i], height[j]) * (j - i)
            if product > current_max:
                current_max = product

    return current_max

def max_area_water_bucket_2ptr(height):
    # instantiate 2 pointers and a placeholder for max value
    current_max = 0
    left, right = 0, len(height)-1
    # starting at the ends we will move the smaller bar inward after checking if the max value can be replaced
    while left < right:
        # obtain width by subtracting indices
        width = right - left
        # obtain height by getting the minimum of the 2 bars
        max_height = min(height[left], height[right])
        # multiply for area
        height_product = max_height * width
        # check area against current max and replace
        current_max = max(current_max, height_product)
        # move the pointer of the smaller bar closer to the middle
        if height[left] <= height[right]:
            left += 1
        else:
            right -=1
        
    return current_max
    
def rainfall_trap(height):
        # given a list of integers, we want to form buckets that trap the rainfall
        # instantiate 2 pointers at start and end
        left, right = 0, len(height)-1
        # these will represent the current max size for bars of start and end
        leftMax, rightMax = 0, 0
        # represents final volume/answer
        volume = 0
        
        # so long as rightMax > leftMax then the volume depends on the left bar
        # the reverse is true: if rightMax < leftMax then the volume depends on the right bar
        
        while left < right:
            leftMax, rightMax = max(leftMax, height[left]), max(rightMax, height[right])
            if leftMax < rightMax:
                volume += leftMax - height[left]
                left += 1
            else:
                volume += rightMax - height[right]
                right -= 1
        return volume

    
def main():
    nums = [2,7,11,15]
    target = 9
    
    print("\nProblem 1: Two Sum with Sorted Array")
    print("Answer: " + str(twoSumPointers(nums, target)))
    
if __name__ == '__main__':
    main()
    
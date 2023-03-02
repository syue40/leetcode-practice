import math

# Longest Consecutive Sequence
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
def Question_1(nums):
    sorted_nums = sorted(set(nums))
    streak = 1
    longest_streak = 1
    if len(nums) > 0:
        for i in range(len(sorted_nums)-1):
            if sorted_nums[i] + 1 == sorted_nums[i + 1]:
                streak += 1
            else:
                longest_streak = max(streak, longest_streak)
                streak = 1
    else:
        return 0
    return max(streak, longest_streak)

# Running Sum of 1d Array
# Given an array nums. We define a running sum of an array as runingSum[i] = sum(nums[0]...nums[i]). Return the running sum of nums
def Question_2(nums):
    new_nums = []
    if not nums:
        return []
    
    else:
        new_nums.append(nums[0])
        for i in range(1, len(nums)):
            running_sum = nums[i] + new_nums[i-1]
            new_nums.append(running_sum)
        return new_nums

# Find Pivot Index
# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
# Return the leftmost pivot index. If no such index exists, return -1.
def Question_3(nums):
    sum_nums = sum(nums)
    running_sum = 0
    for i in range(len(nums)):
        if running_sum == (sum_nums - nums[i] - running_sum):
            return i
        running_sum += nums[i]
    return -1

# Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
def Question_4(nums, target):
    for i in range(len(nums)):
        other_num = target - nums[i]
        for j in range(len(nums)):
            if nums[j] == other_num and j != i:
                return [i, j]


# Isomorphic Strings
# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
def Question_5(string_s, string_t):
    container_s = {}
    container_t = {}
    for i in range(len(string_s)):
        if string_s[i] not in container_s.keys():
            container_s[string_s[i]] = string_t[i]
        if string_t[i] not in container_t.keys():
            container_t[string_t[i]] = string_s[i]
        
        if container_s[string_s[i]] != string_t[i]:
            return False
        if container_t[string_t[i]] != string_s[i]:
            return False
    return True

def main():
    print("\nQuestion 1: Largest Consecutive Sequence")
    print(f"Input: {[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]}\n"
          f"Output: {Question_1([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])}")
    print("--------------------")
    
    print("Question 2: Running Sum of 1d Array")
    print(f"Input: {[3, 1, 2, 10, 1]}\n"
          f"Output: {Question_2([3, 1, 2, 10, 1])}")
    print("--------------------")
    
    print("Question 3: Find Pivot Index")
    print(f"Input: {[1, 7, 3, 6, 5, 6]}")
    print(f"Output: {Question_3([1, 7, 3, 6, 5, 6])}")
    print("--------------------")
    
    print("Question 4: Two Sum")
    print(f"Input: {[2, 7, 11, 15], 9}")
    print(f"Output: {Question_4([2, 7, 11, 15], 9)}")
    print("--------------------")
    
    print("Question 5: Isomorphic Strings")
    print(f"Input: ('abab', 'abdc')")
    print(f"Output: {Question_5('abab', 'abdc')}")
    print("--------------------")

if __name__ == '__main__':
    main()
import collections
# This file will cover leetcode problems to do with Arrays and Hashing

# one liner answer to validity questions
def contains_duplicate(nums):
    # for checking the duplicate, we can check if len(nums) == set(len(nums)) 
    # using a set eliminates duplicate elements in O(N) time
    return len(set(nums)) != len(nums)

def is_anagram(stri, targ):
    # in python the sorted function has time complexity of O(NlogN)
    return sorted(stri) == sorted(targ)

def is_palindrome(s):
    # string slicing relies on copying 
    return s == s[::-1]

def group_anagrams(strs):
    # base case, if the length of strs is 1, then return the original string in a list
    if len(strs) == 1:
        return list(strs)
    
    # instantiate a default dict object (looks like defaultdict(<class 'list'>, {}))
    # we want to append items that are anagrams to the same list
    # to do this we set a sorted tuple of the string as the key
    container = collections.defaultdict(list)
    for item in strs:
        
        # a list cannot be used here because of its mutable nature it cannot be used as a key
        # a tuple is immutable so can be used as a key
        container[tuple(sorted(item))].append(item)
        
    return container.values()

def top_k_frequent_elements(nums, target):
    # base case if nums contains k item then we return that
    if len(nums) == target:
        return nums
    
    # the counter built-in counts number of occurrences of each element
    counted_items = collections.Counter(nums)
    
    # using sorted lambda sorts the items from greatest to least by value
    # using orderedDict preserves the order (if we transform it just by using Dict() the ordering is lost)
    container = collections.OrderedDict(sorted(counted_items.items(), key = lambda item:item[1], reverse=True))
    
    # return the first k items in a slice from the keys of our container
    return list(container.keys())[:target]

def longest_consecutive_sequence(nums):
    # get a sorted sequence of nums
    # here a clause is that all items are unique
    nums_sorted = sorted(nums)
    
    # we want to keep track of BOTH the streak and longest streak
    streak = 1
    longest_streak = 1
    if len(nums) > 0:
        # check the current element againt the next element (look ahead)
        for i in range(len(nums_sorted)-1):
            # if the next item is 1 greater than the previous, increment streak
            if nums_sorted[i] + 1 == nums_sorted[i+1]:
                streak += 1
            else:
                # else compare the 2 streaks and get the longest one, assign it to longest streak
                longest_streak = max(streak, longest_streak)
                streak = 1
    else: 
        return 0

    return max(streak, longest_streak)

def product_of_array_except_self(nums):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
         # The length of the input array 
        length = len(nums)
        
        # The left and right arrays as described in the algorithm
        L, R, answer = [0]*length, [0]*length, [0]*length
        
        # L[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the L[0] would be 1
        L[0] = 1
        for i in range(1, length):
            
            # L[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all 
            # elements to the left of index 'i'
            L[i] = nums[i - 1] * L[i - 1]
        
        # R[i] contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R[length - 1] would be 1
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            
            # R[i + 1] already contains the product of elements to the right of 'i + 1'
            # Simply multiplying it with nums[i + 1] would give the product of all 
            # elements to the right of index 'i'
            R[i] = nums[i + 1] * R[i + 1]
        
        # Constructing the answer array
        for i in range(length):
            # For the first element, R[i] would be product except self
            # For the last element of the array, product except self would be L[i]
            # Else, multiple product of all elements to the left and to the right
            answer[i] = L[i] * R[i]
        
        return answer


def main():
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print("\nProblem 1: Contains Duplicate")
    print("Answer: " + str(contains_duplicate(nums)))
    
    s, t = "anagram", "nagaram"
    print("\nProblem 2: Valid Anagram")
    print("Answer: " + str(is_anagram(s, t)))
    
    s = "racecar"
    print("\nProblem 3: Is Palindrome")
    print("Answer: " + str(is_palindrome(s)))
    
    strs = ["eat","tea","tan","ate","nat","bat"]
    print("\nProblem 4: Group Anagrams")
    print("Answer: " + str(group_anagrams(strs)))
    
    nums = [3, 4, 5, 5, 6, 1, 1, 1, 1, 2, 2, 2, 3, -1, -1]
    target = 2
    print("\nProblem 5: Top K Elements")
    print("Answer: " + str(top_k_frequent_elements(nums, target)))
    
    nums = [0,3,7,2,5,8,4,6,0,1]
    print("\nProblem 6: Longest Conesecutive Sequence")
    print("Answer: " + str(longest_consecutive_sequence(nums)))
    
if __name__ == "__main__":
    main()
def bestTimeBuySellStock(prices):
    left = 0
    result = 0
    # we would move the left pointer if the right one is less than it's value
    # because it would mean that profit is impossible buying at that price
    for right in range(len(prices)):
        while prices[left] > prices[right]:
            # move the left pointer
            left += 1
        # so long as the price of the right index is higher than the left, calculate the difference
        # check it against the current max profit
        result = max(result, prices[right] - prices[left])
    return result

def lengthOfLongestSubstring(s):
    left = 0
    result = 0
    unique_char_set = set()
    
    # we will move the right pointer to change the length of the sliding window here
    for right in range(len(s)):
        # if the current character is already in the set, remove the left-most element, move the left pointer
        while s[right] in unique_char_set:
            unique_char_set.remove(s[left])
            left += 1
        unique_char_set.add(s[right])
        result = max(result, right - left + 1)
    
    return result

def main():
    s = "aabbccdefghi"
    print("\nQuestion 1: Length of Longest Substring (no dups)")
    print("Answer: " + str(lengthOfLongestSubstring(s)))

if __name__ == '__main__':
    main()
# This file will cover using stacks

def valid_parentheses(s):
    # create a mapping of closing brackets to opening brackets
    mapping = {
        ")": "(", 
        "}": "{", 
        "]": "["
        }

    stack = []
    # for each character in the input string
    for char in s:
        # if the character is a closing bracket
        if char in mapping:
            # and the stack is longer than 0
            if len(stack) > 0:
                # then pop the top element in the stack
                top_element = stack.pop()
                # if the top element is not equal to the current one that means the parenthese can't close
                if mapping[char] != top_element:
                    # return cfalse
                    return False
            # if a closing bracket is the first item it's always invalid
            # by appending # the stack is never empty
            else:
                stack.append("#")
        else:
            # else if the character is an opening parentheses append it to the stack
            stack.append(char)
    
    # check if all parentheses have been closed --> empty stack
    return not stack
    
def main():
    s = "()()()()()"
    s1 = "]][[[]]]"
    print("\nProblem 1: Valid Parentheses")
    print("Answer: " + str(valid_parentheses(s1)))
    
if __name__ == '__main__':
    main()
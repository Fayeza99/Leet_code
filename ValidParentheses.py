class Solution(object):
    def isValid(self, s):
        matching_brackets = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:
            if char in matching_brackets.values():  # If it's an opening bracket
                stack.append(char)
            elif char in matching_brackets:         # If it's a closing bracket
                if stack and stack[-1] == matching_brackets[char]:  # Check for matching opening
                    stack.pop()
                else:
                    return False
            else:
                return False  # Invalid character

        return len(stack) == 0

def main():
    solution = Solution()
    test_strings = ["{}", "[]", "(())", "(()))", "(()", ")("]
    for test in test_strings:
        result = solution.isValid(test)
        print(f"isValid('{test}') = {result}")

if __name__ == "__main__":
    main()
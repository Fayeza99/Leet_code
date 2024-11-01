
class Solution(object):
    def mergeAlternately(self, word1, word2):
        new_string = ''.join(char1 + char2 for char1, char2 in zip(word1, word2))
        new_string += word1[len(new_string)//2:] + word2[len(new_string)//2:]
        return new_string


def main():
    # Create an instance of the Solution class
    sol = Solution()

    # Test cases
    word1 = "Hello"
    word2 = "World"
    result = sol.mergeAlternately(word1, word2)
    print("Result for Hello + World:", result)

    # Another test case with different length strings
    word1 = "ab"
    word2 = "pqrs"
    result = sol.mergeAlternately(word1, word2)
    print("Result for ab + pqrs:", result)

    # Additional test case
    word1 = "abcde"
    word2 = "pqr"
    result = sol.mergeAlternately(word1, word2)
    print("Result for abcde + pqr:", result)

# Execute the main function
if __name__ == "__main__":
    main()
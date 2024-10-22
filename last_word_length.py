
class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.split()
        return len (words[-1]) if words else 0
            
        

# def main():
#     # Create an instance of the Solution class
#     solution = Solution()
    
#     # Test cases
#     test_cases = [
#         "Hello World",
#         "   Fly me   to   the moon   ",
#         "   Coding is fun!   ",
#         "",
#         "   SingleWord   ",
#         "Trailing spaces    "
#     ]
    
#     # Iterate through each test case and print the result
#     for sentence in test_cases:
#         length = solution.lengthOfLastWord(sentence)
#         print(f'Length of the last word in "{sentence}" is: {length}')

# # Call the main function
# if __name__ == "__main__":
#     main()
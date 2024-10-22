
class Solution(object):
    def strStr(self, haystack, needle):
        index = haystack.find(needle)
        return index


# def main():
#     # Create an instance of the Solution class
#     solution = Solution()
    
#     # Example strings
#     haystack = "Hello, world!"
#     needle = "world"
    
#     # Call the strStr method
#     index = solution.strStr(haystack, needle)
    
#     # Print the result
#     if index != -1:
#         print(f"The substring '{needle}' found at index {index} in '{haystack}'.")
#     else:
#         print(f"The substring '{needle}' not found in '{haystack}'.")

# # Call the main function
# if __name__ == "__main__":
#     main()
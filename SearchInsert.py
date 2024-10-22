class Solution(object):
    def searchInsert(self, nums, target):
        for index, value in enumerate(nums):
            if value == target or value > target:
                return index
        return len (nums)



def main():
    # Create an instance of the Solution class
    solution = Solution()
    
    # Example list and target
    nums = [1, 3, 5, 6]
    target = 5
    
    # Call the searchInsert method
    index = solution.searchInsert(nums, target)
    
    # Print the result
    print(f"Target {target} should be inserted at index {index} in the list {nums}.")

    # Test with different target values
    targets = [2, 7, 0]
    for target in targets:
        index = solution.searchInsert(nums, target)
        print(f"Target {target} should be inserted at index {index} in the list {nums}.")

# Call the main function
if __name__ == "__main__":
    main()
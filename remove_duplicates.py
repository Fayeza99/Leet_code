

class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        k = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        
        return k
    

def main():
    # Create an instance of the Solution class
    solution = Solution()
    
    # Example list with duplicates
    nums = [1, 1, 2, 2, 3, 4, 4, 5, 6]
    
    # Call the removeDuplicates method
    result = solution.removeDuplicates(nums)
    
    # Print the result
    print("List after removing duplicates:", result)

# Call the main function
if __name__ == "__main__":
    main()

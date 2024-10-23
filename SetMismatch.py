class Solution(object):
    def findErrorNums(self, nums):
        x = -1
        nums.sort()
        expected_sum = sum(range(1, len(nums) + 1))
        actual_sum = sum(nums)
        for index in range(len(nums) - 1):
            if nums[index] == nums[index + 1]:
                x = nums[index]
        
        y = expected_sum - (actual_sum - x) 
        return [x, y]



def main():
    solution = Solution()

    nums = [1, 2, 2, 4]  # Expected output: [2, 3]

    # Call the findErrorNums method and print the result
    result = solution.findErrorNums(nums)
    print(f"Input: {nums} -> Output: {result}")

# Call the main function
if __name__ == "__main__":
    main()

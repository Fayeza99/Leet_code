class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits

def main():
    solution = Solution()
    
    digits = [1, 2, 3]
    print("Input:", digits)
    result = solution.plusOne(digits)
    print("Output:", result)

if __name__ == "__main__":
    main()

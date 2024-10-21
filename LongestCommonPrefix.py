class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # Start with the first string as the initial prefix
        prefix = strs[0]
        
        # Compare the prefix with each string in the list
        for s in strs[1:]:
            # Reduce the prefix length until it matches the start of s
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                # If the prefix is reduced to an empty string, return ""
                if not prefix:
                    return ""
        return prefix

def main():
    solution = Solution()
    test_cases = [
        ["apple", "application", "apricot"],
        ["flower", "flow", "flight"],
        ["dog", "racecar", "car"],
        ["", "b", "c"],
        ["a"],
        [],
        ["interspecies", "interstellar", "interstate"],
    ]
    
    for strs in test_cases:
        result = solution.longestCommonPrefix(strs)
        print(f"Strings: {strs}")
        print(f"Longest Common Prefix: '{result}'\n")

if __name__ == "__main__":
    main()

class Solution(object):
    def roman_to_int(self, s):
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        prev_value = 0
    
        for char in reversed (s):
            value = roman_dict[char]
            if value < prev_value:
                total -= value
            else:
                total += value
                prev_value = value
        return total


def main():
    solution = Solution()

    numerals = [
        'I', 'II', 'III', 'IV', 'V', 'IX', 'X', 'XL',
        'L', 'XC', 'C', 'CD', 'D', 'CM', 'M', 'MCMXCIV'
    ]

    for numeral in numerals:
        result = solution.roman_to_int(numeral)
        print("{} => {}".format(numeral, result))

if __name__ == '__main__':
    main()

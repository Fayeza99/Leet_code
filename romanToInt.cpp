#include <string>
#include <iostream>

class Solution {
public:
int deci(char roman_np_value) {
	switch (roman_np_value) {
	case 'M':
		return 1000;
		break;
	case 'D':
		return 500;
		break;
	case 'C':
		return 100;
		break;
	case 'L':
		return 50;
		break;
	case 'X':
		return 10;
		break;
	case 'V':
		return 5;
		break;
	case 'I':
		return 1;
		break;
	default:
		return -1;
	}
}
int romanToInt(std::string s) {
	int res = 0;
	for (int i = 0; i < s.size(); i++) {
		if (i + 1 < s.size() && deci(s[i]) < deci(s[i + 1])) {
			res -= deci(s[i]);
		}
			else {
				res += deci(s[i]);
			}
		}
		return res;
	}
};



// class Solution {
// public:
// 	int romanToInt(std::string s) {
// 		int total = 0;
// 		int prev_value = 0;
// 		for (int i = s.length() - 1; i >= 0; i--)
// 		{
// 			int value = 0;
// 			switch (s[i]){
// 				case 'I': value = 1; break;
// 				case 'V': value = 5; break;
// 				case 'X': value = 10; break;
// 				case 'L': value = 50; break;
// 				case 'C': value = 100; break;
// 				case 'D': value = 500; break;
// 				case 'M': value = 1000; break;
// 			}
// 			if (value < prev_value)
// 				total -= value;
// 			else
// 				total += value;
// 			prev_value = value;
// 		}
// 		return total;
// 	}
// };

int main() {
	Solution solution;
	std::string roman;
	std::cout << "Enter a Roman numeral: ";
	std::cin >> roman;

	int integer = solution.romanToInt(roman);
	std::cout << "The integer value is: " << integer << std::endl;

	return 0;
}
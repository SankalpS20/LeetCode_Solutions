from typing import List

class Solution:
	def letterCombinations(self, digits: str) -> List[str]:
		if not digits:
			return []
		
		phone_map = {
			'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
			'6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
		}
		
		def backtrack(combination: str, next_digit_index: int):
			if next_digit_index == len(digits):
				combinations.append(combination)
				return
			current_digit = digits[next_digit_index]
			for letter in phone_map[current_digit]:
				backtrack(combination + letter, next_digit_index + 1)
		
		combinations = []
		backtrack("", 0)
		return combinations
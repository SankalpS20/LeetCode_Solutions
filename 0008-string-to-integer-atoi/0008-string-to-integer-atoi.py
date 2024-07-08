class Solution:
	def myAtoi(self, s: str) -> int:
		s = s.lstrip()
		if not s:
			return 0

		sign = 1
		if s[0] == '-':
			sign = -1
			s = s[1:]
		elif s[0] == '+':
			s = s[1:]

		result = 0
		for char in s:
			if char.isdigit():
				result = result * 10 + int(char)
			else:
				break
		result *= sign

		INT_MIN, INT_MAX = -2**31, 2**31 - 1
		if result < INT_MIN:
			return INT_MIN
		if result > INT_MAX:
			return INT_MAX

		return result
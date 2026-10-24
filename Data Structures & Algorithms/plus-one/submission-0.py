class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        newDigits = digits.copy()
        cur = len(digits) - 1
        while cur >= 0 and digits[cur] == 9:
            newDigits[cur] = 0
            cur -= 1
        if cur >= 0:
            newDigits[cur] += 1
        else:
            newDigits.insert(0, 1)
        
        return newDigits
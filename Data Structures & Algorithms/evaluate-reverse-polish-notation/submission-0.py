import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b)  # LeetCode usually requires truncation toward zero
        }

        nums = []
        for val in tokens:
            if val in ops:
                b = nums.pop()
                a = nums.pop()
                nums.append(ops[val](a,b))
            else:
                nums.append(int(val))
        return nums[0]

        
                
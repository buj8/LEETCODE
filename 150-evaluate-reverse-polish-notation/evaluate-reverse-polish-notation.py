class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {
            "+": lambda y, x: x + y,
            "-": lambda y, x: x - y,
            "*": lambda y, x: x * y,
            "/": lambda y, x: int(x / y)
        }
        for t in tokens:
            if t[-1].isnumeric():
                stack.append(int(t))
            else:
                stack.append(op[t](stack.pop(), stack.pop()))
        return stack[0]          
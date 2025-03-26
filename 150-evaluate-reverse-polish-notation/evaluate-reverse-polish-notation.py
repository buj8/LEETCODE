class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y)
        }
        for t in tokens:
            if t[-1].isnumeric():
                stack.append(int(t))
            else:
                a = stack.pop()
                b = stack.pop()
                #print(f"{b} {t} {a} = {op[t](b, a)}")
                stack.append(op[t](b, a))
                #print(stack)
        return stack[0]          
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = 0
        stack = []

        for token in tokens:
            if token == '+':
                new = stack.pop() + stack.pop()
            elif token == '-':
                new = -stack.pop() + stack.pop()
            elif token == '*':
                new = stack.pop() * stack.pop()
            elif token == '/':
                denominator = stack.pop()
                new = int(stack.pop()/denominator)
            else:
                new = int(token)
            stack.append(new)
        return stack[-1]
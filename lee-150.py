class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            match item:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    y, x = stack.pop(), stack.pop()
                    stack.append(x - y)
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "/":
                    y, x = stack.pop(), stack.pop()
                    stack.append(int(x/y))
                case default:
                    stack.append(int(item))

        return stack[0]
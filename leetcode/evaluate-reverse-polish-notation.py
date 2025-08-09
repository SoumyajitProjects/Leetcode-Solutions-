class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # use a stack to store intermediate values

        for c in tokens:
            if c == "+":                  # addition: pop top 2, push sum
                stack.append(stack.pop() + stack.pop())
                
            elif c == "-":                # subtraction: order matters (b - a)
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            
            elif c == "*":                # multiplication: pop top 2, push product
                stack.append(stack.pop() * stack.pop())
            
            elif c == "/":                # division: order matters (b / a)
                a, b = stack.pop(), stack.pop()
                # int(b / a) truncates toward 0 per problem spec (e.g., -3/2 -> -1)
                stack.append(int(b / a))
            
            else:                         # number: push onto stack
                stack.append(int(c))
        
        return stack[0]  # final result remains on the stack
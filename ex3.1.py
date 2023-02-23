class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
def tokenize(expr):
    for p in ['(',')','[',']','{','}']:
        expr = expr.replace(p, f' {p} ')
    return expr.split()

def evaluate(expr):
    tokens = tokenize(expr)
    
    stack = Stack()
    
    for token in tokens:
        if token == '(':
            pass
        elif token in ['+', '-', '*', '/']:
            op = token
        elif token.isdigit():
            e2 = int(token)
            e1 = int(token)
        
            if op == '+':
                result = e1 + e2
            elif op == '-':
                result = e1 - e2
            elif op == '*':
                result = e1 * e2
            elif op == '/':
                result = e1 / e2
            stack.push(result)
        elif token == ')':
            pass
        else:
            stack.push(int(token))
    
    return stack.pop()

input = input()
output = evaluate(input)
print(output)

#print(evaluate("(+ 1 2)"))

#print(evaluate("(* 3 (- 4 2))"))

#print(evaluate("(/ 10 (+ 2 3))"))




class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        return popped_node.data

    def is_empty(self):
        return self.top is None

def tokenize(expression):
    tokens = []
    i = 0
    while i < len(expression):
        if expression[i] == '(' or expression[i] == ')':
            tokens.append(expression[i])
            i += 1
        elif expression[i] == ' ':
            i += 1
        else:
            j = i
            while j < len(expression) and expression[j] != ' ' and expression[j] != '(' and expression[j] != ')':
                j += 1
            tokens.append(expression[i:j])
            i = j
    return tokens

def evaluate(expression):
    tokens = tokenize(expression)
    stack = Stack()
    for token in tokens:
        if token == ')':
            operand = stack.pop()
            operand2 = stack.pop()
            operator = stack.pop()
            if operator == '+':
                result = float(operand2) + float(operand)
            elif operator == '-':
                result = float(operand2) - float(operand)
            elif operator == '*':
                result = float(operand2) * float(operand)
            elif operator == '/':
                result = float(operand2) / float(operand)
            stack.push(str(result))
        elif token in ('+', '-', '*', '/'):
            stack.push(token)
        elif token == '(':
            pass
        else:
            stack.push(token)
    return stack.pop()



input = input()
output = evaluate(input)
print(output)




def prefix_to_postfix(prefix_expression):
    def is_operator(char):
        return char in "+-*/^"

    def reverse_expression(expression):
        return expression[::-1]

    stack = []
    prefix_expression = reverse_expression(prefix_expression)
    
    for char in prefix_expression:
        if char.isalnum():  # Operand
            stack.append(char)
        elif is_operator(char):
            operand1 = stack.pop()
            operand2 = stack.pop()
            result = operand1 + operand2 + char
            stack.append(result)

    postfix_expression = reverse_expression(stack[0])
    return postfix_expression

# Example usage:
prefix_expression = "*+AB-CD"
postfix_expression = prefix_to_postfix(prefix_expression)
print("Prefix Expression:", prefix_expression)
print("Postfix Expression:", postfix_expression)

def perform_operation(num1, num2, operation):
    if operation == '+' :
        return num1 + num2
    elif operation == '-' :
        return num1 - num2
    elif operation == '*' :
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "You cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid operation"
    
print(perform_operation(2,3,'*'))
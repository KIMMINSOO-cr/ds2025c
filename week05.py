
def check_parentheses(a_string : str) -> bool:
    stack =[]
    for c in a_string:
        if c=="(":
            stack.append("c")
        if c ==")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0
check_parentheses("(2+3)")
check_parentheses("(2+(2+3))")
check_parentheses("(2+(2+3)")
check_parentheses("+2_(2+3)(")

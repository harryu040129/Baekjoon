while True:
    input_str = input()
    if input_str == ".":
        break  
    
    stack = []
    res = "yes"

    for x in input_str:
        if x in ["(", "["]:
            stack.append(x)
        elif x in [")", "]"]:
            if not stack:
                res = "no"
                break
            elif stack[-1] == "(" and x == ")":
                stack.pop()
            elif stack[-1] == "[" and x == "]":
                stack.pop()
            else:
                res = "no"
                break

    if stack:  
        res = "no"

    print(res)

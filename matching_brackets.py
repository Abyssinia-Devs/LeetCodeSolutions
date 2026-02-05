def isValid(s):
    matching_brackets = {")": "(", "}": "{", "]": "["}
    stack = []
    for bra in s:
        if bra in matching_brackets:
            if stack:
                top_element=stack.pop()
            else:
                top_element='#'
            if matching_brackets[bra] != top_element:
               return False
        else:
            stack.append(bra)
    return len(stack)==0
print(isValid('{[()]}'))

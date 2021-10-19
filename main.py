# balanced parentheses in an expression
open_list = ["[","{","("]
close_list = ["]","}",")"]
  
# Function to check parentheses
def check(myStr):
    stack= []
    for i in myStr:
        stack.append(i)
    print(len(stack))
          
    while not (len(stack)==0):
        if stack[len(stack)-1] in open_list:
            poso =open_list.index(stack[len(stack)-1])
            if close_list[poso] in stack:
                stack.pop(stack.index(close_list[poso]))
                pos=stack.index(open_list[poso])
                stack.pop(pos)
            else:
                return "Unbalnced"
        elif stack[len(stack)-1] in close_list:
            poso =close_list.index(stack[len(stack)-1])
            if open_list[poso] in stack:
                stack.pop(stack.index(open_list[poso]))
                pos=stack.index(close_list[poso])
                stack.pop(pos)
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"
  
  
# Driver code
string = "{[}()]}{"
print(check(string))
  

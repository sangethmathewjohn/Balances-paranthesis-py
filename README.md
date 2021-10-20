# Balances-paranthesis-py

     # balanced parentheses in an expression
      open_list = ["[","{","("]
      close_list = ["]","}",")"]

      # Function to check parentheses
      def check(myStr):
          stack= []
          # converting string into a stack
          for i in myStr:
              stack.append(i)
          print(len(stack))
          if len(stack)%2==1:
              return "Unbalanced"
          while not (len(stack)==0):
              i=len(stack)-1
              x=stack[i]
              if x in open_list:
                  poso =open_list.index(x)
                  if close_list[poso] in stack:
                      stack.pop(stack.index(close_list[poso]))
                      pos=stack.index(open_list[poso])
                      stack.pop(pos)
                  else:
                      return "Unbalnced"
              elif x in close_list:
                  poso =close_list.index(x)
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



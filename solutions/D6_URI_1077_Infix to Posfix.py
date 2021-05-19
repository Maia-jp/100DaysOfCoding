"""
    Solution by Joao P Maia 
    Problem-> https://www.urionlinejudge.com.br/judge/en/problems/view/1077
    Online compiler -> https://onlinegdb.com/P8f6bdvBM
    Day 6
"""
##
def priority(c):
    if(c == '^'):
        return 3
    elif(c == '*' or c == '/'):
        return 2
    elif(c == '+' or c == '-'):
        return 1;
    else:
        return -1;
##
def transform(string):
    stack = []
    result = ""
    for char in string:
        if char.isalpha() or char.isdigit():
            result += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while result[-1] != '(':
                result += stack.pop()
                if(len(stack)==0): break;
            result = result[:-1]
            
        else:
            if(len(stack)==0):
                stack.append(char)
            else:
                while(len(stack)>0) and (priority(char) <= priority(stack[-1])):
                     result += stack.pop()
    
                stack.append(char);
                
            
    for rest in stack:
        result += rest
    
    print(result)

##
testCases = int(input())
for t in range(testCases):
    transform(input())

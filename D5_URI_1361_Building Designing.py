"""
    Solution by Joao P Maia 
    Problem-> https://www.urionlinejudge.com.br/judge/en/problems/view/1244
    Online Compiler-> https://www.urionlinejudge.com.br/judge/en/problems/view/1361
    Day 5
"""
cases = int(input())

for i in range(cases):
    floors = int(input())
    blue = [1000000]
    red = [-1000000]
    
    for f in range(floors):
        ipt = int(input())
        if(ipt<0): red.append(ipt)
        if(ipt>0): blue.append(ipt)
    
    
    blue.sort(reverse = True);
    red.sort()

    
    build = []
    if(abs(red[-1]) < blue[-1]):
        build.append(red.pop())
    elif(abs(red[-1]) > blue[-1]):
        build.append(blue.pop())
    
    
    while(abs(red[-1]) != blue[-1]):
        #print(build,red,blue)
        if(abs(red[-1]) < blue[-1]):
            if(build[-1]>0):
                build.append(red.pop())
            else: red.pop()
        elif(abs(red[-1]) > blue[-1]):
            if(build[-1]<0):
                build.append(blue.pop())
            else: blue.pop()
        
    print(len(build))

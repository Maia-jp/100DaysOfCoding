"""
    Solution by Joao P Maia 
    Problem-> https://www.urionlinejudge.com.br/judge/en/runs/code/22778119
    Online compiler -> https://onlinegdb.com/Syh5p9u__
    Day 2
"""
blocking = ""

def checkDirection(lst,N):
    stackStation = [0]
    stackDirection = []
    originalLen = len(lst)
    while(len(lst)>0):
        insertion = True
        #opt 1 -> go to b
        if(int(lst[-1]) == N):
            stackDirection.insert(0,int(lst.pop()))
            N -= 1
            insertion = False
        #opt 2 -> come from station
        if(stackStation[-1] == N):
            stackDirection.insert(0,stackStation.pop())
            N -= 1
            insertion = False
        #opt 3 -> go to station
        if(len(lst) == 0):
            break
        if(insertion):
            stackStation.append(int(lst.pop()))

    stackStation.reverse()
    for train in stackStation:
        stackDirection.insert(0,train)
        if(stackDirection[1]<stackDirection[0]):
            return "No"
        
    return "Yes"

def isNumber(s):
    try:
        return int(s)
    except ValueError:
        pass
 
    return -1


N = 0
while(True):
    ipt = input()
    ipt = ipt.strip();
    if(isNumber(ipt) != -1 and isNumber(ipt) == 0):
        blocking += "0"
        N = 0
        if(len(blocking)>1): 
            exit()
        else:
            print()
    elif(len(ipt.split(" "))<2):
        N = int(ipt.strip())
        blocking = ""
    else:
        ipt = ipt.split(" ")
        
        print(checkDirection(ipt,N))
            

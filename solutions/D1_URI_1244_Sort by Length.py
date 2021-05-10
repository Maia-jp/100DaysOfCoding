"""
    Solution by Joao P Maia 
    Problem-> https://www.urionlinejudge.com.br/judge/en/problems/view/1244
    Online compiler -> https://www.mycompiler.io/view/3JSedzE
    Day 1
"""

def inLinePrint(lst):
    str =""
    for i in lst:
        str += i + " "
    print(str[:-1])
    return

inputSize = int(input())

for i in range(0,inputSize):
    ipt = input()
    ipt = ipt.split(" ")
    ipt.sort(key=len,reverse=True)
    inLinePrint(ipt)

'''

Solution by Joao P Maia 
    Problem-> https://www.urionlinejudge.com.br/judge/en/problems/view/3152
    Online compiler -> https://onlinegdb.com/2xJsHpRs8
    Day 7

'''
import math
#Functions
def dist(p1x,p1y,p2x,p2y):
    return math.sqrt(pow((p1x-p2x),2)+pow((p1y-p2y),2));
def area(sideA,sideB,sideC,sideD,diagonalE,diagonalF):
    s = (sideA+sideB+sideC+sideD)/2
    t = (s-sideA)*(s-sideB)*(s-sideC)*(s-sideD)-((1/4)*(sideA*sideC+sideB*sideD+diagonalF*diagonalE)*(sideA*sideC+sideB*sideD-diagonalF*diagonalE))
    return math.sqrt(t)

#main
vert1 = []
vert2 = []
for i in range(8):
    if i<4:
        ipt = input()
        ipt = ipt.split(" ")
        vert1.append([int(ipt[0]),int(ipt[1])])
    else:
        ipt = input()
        ipt = ipt.split(" ")
        vert2.append([int(ipt[0]),int(ipt[1])])

side1 = []
side2  = []

#Terrain 1 sides
px = vert1[0][0]
py = vert1[0][1]

for point in vert1:
    side = dist(px,py,point[0],point[1])
    px = point[0] 
    py = point[1]
    side1.append(side)

side1[0] = dist(vert1[0][0],vert1[0][1],vert1[-1][0],vert1[-1][1]) #Fixing "dead" side
side1.append(dist(vert1[0][0],vert1[0][1],vert1[2][0],vert1[2][1])) #Diagonals
side1.append(dist(vert1[1][0],vert1[1][1],vert1[3][0],vert1[3][1])) #Diagonals

#Terrain 2 sides
px = vert2[0][0]
py = vert2[0][1]

for point in vert2:
    side = dist(px,py,point[0],point[1])
    px = point[0] 
    py = point[1]
    side2.append(side)

side2[0] = dist(vert2[0][0],vert2[0][1],vert2[-1][0],vert2[-1][1]) #Fixing "dead" side
side2.append(dist(vert2[0][0],vert2[0][1],vert2[2][0],vert2[2][1])) #Diagonals
side2.append(dist(vert2[1][0],vert2[1][1],vert2[3][0],vert2[3][1])) #Diagonals

#Terrain areas
t1 = area(side1[0],side1[1],side1[2],side1[3],side1[4],side1[5])
t2 = area(side2[0],side2[1],side2[2],side2[3],side2[4],side2[5])

if t1 == t2 or t2>t1:
    print("terreno B")
else:
    print("terreno A")

    

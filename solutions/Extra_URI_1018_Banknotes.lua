--    Solution by Joao P Maia 
--    Problem-> https://www.mycompiler.io/view/IGwnviV
--    Online compiler -> https://onlinegdb.com/-7d_wdAEQ
--    Day extra

total = io.read( "*n" )
answer  = total
notes = {100,50,20,10,5,2,1}
totalNotes = {}
for i=1,7
    do
        totalNotes[i] = answer // notes[i]
        answer = answer - totalNotes[i] * notes[i]
    end

print(total)
print(string.format("%d nota(s) de R$ 100,00",totalNotes[1]))
print(string.format("%d nota(s) de R$ 50,00",totalNotes[2]))
print(string.format("%d nota(s) de R$ 20,00",totalNotes[3]))
print(string.format("%d nota(s) de R$ 10,00",totalNotes[4]))
print(string.format("%d nota(s) de R$ 5,00",totalNotes[5]))
print(string.format("%d nota(s) de R$ 2,00",totalNotes[6]))
print(string.format("%d nota(s) de R$ 1,00",totalNotes[7]))

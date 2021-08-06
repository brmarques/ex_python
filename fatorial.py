#dois exemplos de como fazer fatorial recebendo valor por input

#ex.:1

n = int(input())
count = 1
fatorial = 1
while count <= n:
    fatorial *= count
    count += 1
print(fatorial)

################################

#ex.:2

f = int(input())
fat = 1
for x in range(1, n+1):
    fat = fat * x
print (fat)

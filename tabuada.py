#única diferença entre eles é a sintaxe da saída (print)
#ex.:1
N = int(input())
for i in range(1, 11):
    print ("{} * {} = {}". format(N, i, N * i))

###########################################################
    
#e.:2
N = int(input())
for i in range(1, 11):
    print (f"{N} * {i} = {N * i}")

import random
import time

def sort(v):
    fim = len(v)
    while fim > 0:
        i = 0
        #percorrendo o vetor de 0 ate fim
        while i < fim-1:
            if v[i] > v[i+1]:
                #realizando a troca de posição atual pela proxima
                temp = v[i]
                v[i] = v[i+1]
                v[i+1] = temp
            #print(v)
        i += 1
    fim -= 1

vetor = list(range(0, 10000))
random.shuffle(vetor)

print(vetor)

antes1 = time.time()
sort(vetor)
depois1 = time.time()
total1 = (depois1 - antes1)*1000
random.shuffle(vetor)
antes2 = time.time()
sort(vetor)
depois2 = time.time()
total2 = (depois2 - antes2)*1000
random.shuffle(vetor)
antes3 = time.time()
sort(vetor)
depois3 = time.time()
total3 = (depois3 - antes3)*1000

totalf = ((total1 + total2 + total3) / 3)

print ("A ordenação demorou %0.2f ms" % totalf)